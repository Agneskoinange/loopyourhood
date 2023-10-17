FROM python:3.11.4

ENV DJANGO_PORT 8000

WORKDIR  /loopyourhood

COPY ./ requirements.txt

RUN pip3 install -r requirements.txt

COPY . /loopyourhood/

EXPOSE 8000

CMD [ "python", "manage.py",  "runserver", "0.0.0.0:8000" ]