FROM python:3.10.14-slim

WORKDIR /usr/local/bin

COPY test-conn.py .

RUN apt-get update && apt-get install python3-pip -y
RUN pip3 install psycopg2-binary && pip3 install pyTelegramBotAPI

ENTRYPOINT ["python", "test-conn.py"] 

