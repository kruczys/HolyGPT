FROM python:3.10

WORKDIR /app

EXPOSE 5000

COPY requirements.txt requirements.txt
COPY bible_model bible_model
COPY web_app web_app

RUN pip3 install -r requirements.txt

CMD ["python3", "web_app/server.py"]

