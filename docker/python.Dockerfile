FROM python:3

RUN pip install pika --upgrade

CMD [ "tail", "-f", "/dev/null" ]