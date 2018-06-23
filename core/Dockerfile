FROM ubuntu

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.21.4.0/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /
RUN apt-get update && \
    apt-get install -y \
      libpq-dev net-tools nano

COPY /root /
COPY /src/bin/core /usr/bin/core

CMD ["/init"]
