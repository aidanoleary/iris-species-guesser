FROM python:3.8-slim-buster

WORKDIR /iris_app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./iris_app .

EXPOSE 5000
CMD [ "env", "FLASK_APP=app", "python3", "-m" , "flask", "run", "--host=0.0.0.0"]