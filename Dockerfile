FROM python

RUN pip install locust

WORKDIR /locust
COPY ./locustfile.py .

CMD ["locust"]
