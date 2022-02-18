FROM python:3.9-slim
# Debian based python image

# Install necessary pacages. Feel free to add your own
RUN apt-get update && apt-get install postgresql-client wait-for-it -y


# Build app here
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt && rm /tmp/requirements.txt
COPY pdf_service /opt/pdf_service
COPY bin /opt/bin

# User and rights
RUN useradd app -u 1000 -g 100
RUN mkdir /data
RUN chown -R app /opt/pdf_service && chown app /data
USER app

# Start in this directory
WORKDIR /opt/pdf_service

