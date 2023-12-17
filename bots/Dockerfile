FROM python:3.9

RUN mkdir /telebot

WORKDIR /telebot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]