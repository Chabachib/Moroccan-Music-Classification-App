FROM python:3.11.5-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8989

ENV FLASK_APP=main.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8989"]
