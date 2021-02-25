FROM python:3-alpine

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

RUN ls -la

RUN python marvel-classifier.py

EXPOSE 8008

# CMD ["python", "marvel-classifier.py", "serve"]