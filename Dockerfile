FROM python:3.9-buster

EXPOSE 8000

RUN apt-get update && apt-get install -y \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 \
    curl unzip wget \
    libgbm1 \
    xvfb

COPY main.py ./
COPY requirements.txt ./
COPY /bot ./bot

RUN pip3 install -r requirements.txt

ENV PATH="$PATH:/usr/bin/chromedriver"
CMD ["python3", "-u", "main.py", "-v"]