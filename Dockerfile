FROM ubuntu:22.10

RUN apt-get clean all && \
    apt-get update -y && \
    apt-get install -y python3-pip python3-dev

RUN mkdir -p /app/app
COPY requirements.txt /app
COPY wsgi.py /app/
COPY start_app.sh /app/
COPY app /app/app/

WORKDIR /app

RUN pip install -r requirements.txt
ENTRYPOINT ["./start_app.sh"]
