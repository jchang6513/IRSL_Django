FROM python:3.6.2
LABEL Yi-Wei Chang
ENV PYTHONUNBUFFERED 1 
RUN mkdir /IRSL_Django
WORKDIR /IRSL_Django
COPY . /IRSL_Django 
RUN pip install -r requirements.txt
