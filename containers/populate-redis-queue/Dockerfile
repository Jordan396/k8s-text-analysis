FROM python:3
RUN pip install redis
COPY ./rediswq.py /rediswq.py
COPY ./populate-redis-queue.py /populate-redis-queue.py
CMD  python populate-redis-queue.py
