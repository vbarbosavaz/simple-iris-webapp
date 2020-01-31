FROM python:3.7.1

LABEL Author="Vincent/Clea/Dhanashri/Elias"
LABEL version="0.0.1"

ENV FLASK_APP=DSIA5201A_app

#Copy application code
COPY . ./DSIA5201A_app
WORKDIR /DSIA5201A_app

RUN pip install -r requirements.txt

#Expose port
EXPOSE 5000

#Start flask application
CMD flask run --host 0.0.0.0
