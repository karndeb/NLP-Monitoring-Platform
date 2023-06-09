import csv
import datetime
import os
from fastapi import FastAPI
import uvicorn
from fastapi.encoders import jsonable_encoder
from elasticsearch import Elasticsearch, NotFoundError, helpers
from elasticsearch.helpers import streaming_bulk
from elasticapm.contrib.starlette import ElasticAPM, make_apm_client


# apm = make_apm_client(
#     {"SERVICE_NAME": "fastapi-app", "SERVER_URL": "http://apm-server:8200"}
# )
es = Elasticsearch(os.environ["ELASTICSEARCH_HOSTS"])
# index_name = 'logsearch'
# app.add_middleware(ElasticAPM, client=apm)
app = FastAPI()


# es = AsyncElasticsearch(host="host.docker.internal", port=9200)
index_name = "logsearch"


@app.on_event("shutdown")
def app_shutdown():
    es.close()


def upload():
    """Reads the file through csv.DictReader() and for each row
        yields a single document. This function is passed into the bulk()
        helper to create many documents in sequence.
        """
    with open("log-data/dts-logs.csv", mode="r") as f:
        reader = csv.DictReader(f, delimiter=",")
        # line = next(reader)
        # len(line)
        # line.keys()

        for row in reader:
            doc = {
                "timestamp": row["Timestamp"],
                "level": row["Log level"],
                "logger": row["Logger"],
                "line_number": row["Line Number"],
                "file": row["File"],
                "request_id": row["Request ID"],
                "correlation_id": row["Correlation ID"],
                "log_message": row["Log message"]
                }
            yield doc


@app.get("/")
def index():
    return es.cluster.health()


@app.get("/ingest")
def ingest():
    if not (es.indices.exists(index=index_name)):
        es.indices.create(index=index_name)

    for _ in streaming_bulk(
        client=es, index=index_name, actions=upload()
    ):
        pass

    return {"status": "ok"}


@app.get("/search/{query}")
def search(query):
    return es.search(
        index=index_name, size=100, body={"query": {"multi_match": {"query": query}}}
    )
# example  - { "query": { "multi_match" : { "query":"DEBUG", "fields": [ "Log level" ] } } }


@app.get("/delete")
def delete():
    return es.delete_by_query(index=index_name, body={"query": {"match_all": {}}})


@app.get("/delete/{id}")
def delete_id(id):
    try:
        return es.delete(index=index_name, id=id)
    except NotFoundError as e:
        return e.info, 404


@app.get("/update")
def update():
    response = []
    docs = es.search(
        index=index_name, body={"query": {"multi_match": {"query": ""}}}
    )
    now = datetime.datetime.utcnow()
    for doc in docs["hits"]["hits"]:
        response.append(
            es.update(
                index=index_name, id=doc["_id"], body={"doc": {"modified": now}}
            )
        )

    return jsonable_encoder(response)


@app.get("/error")
def error():
    try:
        es.delete(index=index_name, id="somerandomid")
    except NotFoundError as e:
        return e.info


@app.get("/doc/{id}")
def get_doc(id):
    return es.get(index=index_name, id=id)

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=9292)
