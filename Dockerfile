FROM python:3.8.0-buster

WORKDIR /application
COPY requirements.txt .
RUN pip install -r requirements.txt 
COPY /app .
EXPOSE 5000
CMD ["python", "index.py"]
