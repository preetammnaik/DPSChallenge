FROM python:3.10.5

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

ENV PORT 8080

CMD ["gunicorn", "-b", ":8080", "main:app"]
