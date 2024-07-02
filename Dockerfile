FROM python:3.10.6-buster

COPY models /models
COPY salary_ranges /salary_ranges
COPY requirements.txt requirements.txt
COPY setup.py setup.py
RUN apt update \
     && apt install -y \
        build-essential \
        python3-dev \
        pkg-config \
        zip \
        zlib1g-dev \
        unzip \
        curl \
        wget \
        git \
        htop \
        openjdk-11-jdk \
        liblapack3 \
        libblas3 \
        libhdf5-dev \
        npm

RUN pip install -r requirements.txt
RUN pip install .

CMD uvicorn salary_ranges.api:app --host 0.0.0.0 --port $PORT