FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV ENV local

RUN mkdir -p /app/scripts/
WORKDIR /app
ADD ./requirements /app/requirements/

RUN pip install -U setuptools
RUN pip install urllib3==1.21.1 --force-reinstall
RUN pip install -r /app/requirements/base2.txt

RUN mkdir -p /app/static/
ADD ./manage.py /app/
ADD ./config/ /app/config/
ADD ./scripts/ /app/scripts/
ADD ./v1/ /app/v1/


EXPOSE 8000
CMD ["/app/scripts/server.sh"]
