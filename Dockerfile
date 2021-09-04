FROM python:3.9-buster

EXPOSE 8000

COPY main.py ./
COPY requirements.txt ./
COPY /bot ./bot

RUN pip3 install -r requirements.txt

ENV PATH="$PATH:/usr/bin/chromedriver"
CMD ["python3", "-u", "main.py", "-v"]