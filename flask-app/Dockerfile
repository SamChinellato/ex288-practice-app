FROM docker.io/python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN useradd flask 

RUN chown -R 0 /app

RUN chmod -R g=u /app

RUN chgrp -R 0 /app

USER flask

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
