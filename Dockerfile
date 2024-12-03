FROM python:3.10.15

WORKDIR /bio-in-time
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /bio-in-time/

CMD ["python", "src/main.py"]
