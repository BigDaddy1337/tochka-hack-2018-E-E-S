FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN \
  apt-get -y update && \
  apt-get install -y gettext && \
  apt-get clean

ADD requirements.txt /admin-app/
RUN pip install -r /admin-app/requirements.txt

ADD . /admin-app
WORKDIR /admin-app/lfgDbAdmin

EXPOSE 8000
ENV PORT 8000