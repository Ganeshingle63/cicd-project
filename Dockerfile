FROM python:3.12-slim-buster

WORKDIR /app
COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt --user
ENV PATH="/home/default/.local/bin:${PATH}"
EXPOSE 8501

COPY ./app /app/

CMD exec gunicorn --bind :8501 --workers 1 --threads 8 --timeout 0 main:app