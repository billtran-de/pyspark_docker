FROM billtran2306/spark-py:1.0

USER root

WORKDIR /opt/spark/work-dir

RUN mkdir -p /apps
COPY apps/ ./apps

RUN apt-get update
RUN apt-get --assume-yes --no-install-recommends install python3
# RUN apt-get --assume-yes --no-install-recommends install python3-boto3
# RUN apt-get install python3-pip
# RUN pip3 install boto3

# unchecked dependency issue related to pycairo exists in the base image.
# To resolve them, run the following commands:
# Source: https://github.com/3b1b/manim/issues/751
RUN apt-get --assume-yes --no-install-recommends install pkg-config
RUN apt-get --assume-yes --no-install-recommends install libcairo2-dev