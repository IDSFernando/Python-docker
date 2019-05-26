# FROM python:3-alpine
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# COPY . /code/


# RUN apk --update add python py-pip openssl ca-certificates py-openssl wget
# RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
#   && pip install --upgrade pip \
#   && pip install -r requirements.txt \
#   && apk del build-dependencies

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver"]

FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]

#ADD apirest/bin/apicars /usr/src/app/