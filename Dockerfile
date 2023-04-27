FROM python:3.9-slim-buster

WORKDIR /myapp

COPY requirements.txt /myapp/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "MVScheckin.py"]
