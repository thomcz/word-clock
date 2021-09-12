# syntax=docker/dockerfile:1

FROM python:2.7.13
RUN apt-get update && apt-get -y install gcc scons unzip
RUN wget https://github.com/jgarff/rpi_ws281x/archive/master.zip && unzip master.zip && cd rpi_ws281x-master && scons
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]