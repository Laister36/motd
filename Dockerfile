FROM python:3.8.12
COPY motd /motd
WORKDIR /motd
RUN pip install flask \
&& chmod -R 700 /motd
ENTRYPOINT [ "/motd/app.py" ]
