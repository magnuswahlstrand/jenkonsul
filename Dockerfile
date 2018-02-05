FROM python:3.5.4-alpine3.4

ADD ./ /app/
WORKDIR /app

RUN pip install -r /app/requirements.txt

ENTRYPOINT ["ash", "docker-entrypoint.sh"]
CMD []