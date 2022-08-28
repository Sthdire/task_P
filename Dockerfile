FROM python:3.10.6

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /task_P
WORKDIR /task_P
ENTRYPOINT ["python"]
CMD ["app.py"]
