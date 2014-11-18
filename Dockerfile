FROM debian:wheezy
MAINTAINER Andrew Huynh <andrew@productbio.com>

ENV REFRESHED_AT 2014-11-18

ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Install system dependencies
RUN apt-get update && apt-get install -y \
			python-dev python-pip \
			libffi-dev \
			libxml2-dev libxslt1-dev

# Add the dependencies to the container and install the python dependencies
ADD requirements.txt /tmp/requirements.t xt
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

# Expose web GUI
EXPOSE 6800

CMD [ "scrapyd" ]
