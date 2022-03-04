FROM python:3.9

WORKDIR /usr/src/app

COPY ./web/model/craps .

RUN pip install -r requirements.txt

# COPY ./system_craps.py system_craps.py

# COPY ./craps.py craps.py

CMD python craps.py
