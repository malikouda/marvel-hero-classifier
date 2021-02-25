FROM python:3

WORKDIR /app
COPY . /app

RUN pip install torch==1.7.1+cpu torchvision==0.8.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt

RUN python marvel-classifier.py

EXPOSE 8008

CMD ["python", "marvel-classifier.py", "serve"]