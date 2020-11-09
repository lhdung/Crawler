FROM python:3
WORKDIR /apps

RUN pip install scrapy
COPY craw.py /app/test.py

ENTRYPOINT ["scrapy", "runspider", "/app/test.py", "-a"]