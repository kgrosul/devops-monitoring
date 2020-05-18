FROM python:3.6

RUN apt-get update && apt-get install -y vim curl jq
RUN pip3 install requests graphyte
RUN mkdir /monitoring

COPY weather.py /monitoring/weather.py
COPY forecast.py /monitoring/forecast.py
COPY config.py /monitoring/config.py
COPY run.sh /monitoring/run.sh

WORKDIR /monitoring
CMD "./run.sh"