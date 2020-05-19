FROM python:3
RUN pip install redis
RUN pip install pandas
COPY ./wordcount_mapper.py /wordcount_mapper.py
COPY ./rediswq.py /rediswq.py

CMD  python -u wordcount_mapper.py
