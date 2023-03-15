FROM python:3.9-slim-buster

WORKDIR /app

RUN chgrp -R 0 /app && \
    chmod -R u+rw /app && \
    chmod -R g=u /app 


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
