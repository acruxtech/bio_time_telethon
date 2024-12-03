FROM python:3.10.15

WORKDIR /src
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /src/

CMD ["python", "main.py"]

