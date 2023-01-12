FROM python:3.8

EXPOSE 3021
WORKDIR /
RUN mkdir -p /log-data
ADD ./data /log-data

COPY requirements.txt /
RUN python -m pip cache purge
RUN python -m pip install \
    --no-cache \
    --disable-pip-version-check \
    -r /requirements.txt

COPY main.py /
CMD uvicorn main:app --host=0.0.0.0 --port=3021