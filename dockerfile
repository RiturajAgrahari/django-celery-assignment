FROM python:3.12.1-alpine
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN chmod +x entrypoint.sh
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]