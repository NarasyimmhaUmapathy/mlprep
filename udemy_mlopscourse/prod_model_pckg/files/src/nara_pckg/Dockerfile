FROM python:3.8.10-slim

WORKDIR /app #changing into the app dir in the container

COPY . /app/ #copies all files in current loc to the app dir

RUN pip install -r requirements.txt

CMD ["python","main.py"] #executing commands using the interpreter




