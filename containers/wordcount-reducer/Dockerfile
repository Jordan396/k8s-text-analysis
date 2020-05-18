FROM python:3

RUN pip install redis

COPY ./wordcount_reducer.py /wordcount_reducer.py
COPY ./rediswq.py /rediswq.py

CMD  python wordcount_reducer.py
