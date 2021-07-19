# syntax=docker/dockerfile:1

FROM python:3.8.2

WORKDIR .

# install dependancies
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

# run application
ENTRYPOINT  ["python3", "factorial-digits.py"]



