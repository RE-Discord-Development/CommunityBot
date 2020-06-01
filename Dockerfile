FROM python:3

WORKDIR /usr/src/app
RUN mkdir /var/lib/CommunityBot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]