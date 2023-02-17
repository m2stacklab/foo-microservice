FROM python:3-alpine

WORKDIR /app

RUN echo "Flask==2.1.0" > requirements.txt
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 3000

CMD ["python", "app.py"]