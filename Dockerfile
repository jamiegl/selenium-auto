FROM python:3.7-slim-buster
RUN pip install --upgrade pip

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt 

RUN apt-get update && apt-get install \
    -yqq --no-install-recommends wget unzip curl gnupg2

COPY src /usr/local/scraper/

RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
