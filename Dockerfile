FROM python:3.9-slim-buster

LABEL maintainer="milan.jovic@trickest.com"
 
WORKDIR /app

RUN apt-get update \
    && apt-get install -y ca-certificates git

RUN git clone https://github.com/kljunowsky/get-acq /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "get-acq.py"]
