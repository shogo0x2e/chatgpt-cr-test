FROM python:3.12.0

WORKDIR /src

COPY . /src

RUN python -m pip install -r requirements.txt

CMD ["python", "main.py"]