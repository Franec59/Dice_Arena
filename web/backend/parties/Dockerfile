FROM python:3.9

WORKDIR /usr/src/app

# COPY ./web/backend/parties .
COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./main.py main.py

CMD python main.py