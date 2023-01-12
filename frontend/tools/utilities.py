import streamlit as st
import requests
from functools import reduce
import operator
from collections import ChainMap


def load_css():
    with open("tools/style.css") as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


def format_search(resp):
    matches = []
    for hit in resp['hits']['hits']:
        matches.append(hit['_source'])

    return matches


APP_URL = 'http://host.docker.internal:3021'


@st.cache(allow_output_mutation=True)
def load():
    ingest_endpoint = '/ingest'
    res = requests.get(APP_URL + ingest_endpoint)
    return res.json()


@st.cache(allow_output_mutation=True)
def make_query(query, fields):
    return {"query": {"multi_match": {"query": str(query), "fields": fields}}}


def getFromDict(dataDict, mapList):
    # dataDict = dict(ChainMap(*listDict))
    return reduce(operator.getitem, mapList, dataDict)
