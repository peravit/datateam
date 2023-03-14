FROM python:3.7

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# WORKDIR /
WORKDIR /usr/src/app

# COPY . .
COPY . .

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", \
     "--port", "8080", "--reload", \
     "--ssl-keyfile", "/usr/src/app/certs/private_key.pem", \
     "--ssl-certfile", "/usr/src/app/certs/cert.pem"]
# CMD python -m uvicorn main:app --host 0.0.0.0, \
#       --port 8080  --ssl-keyfile "./certs/private_key.pem" \
#       --ssl-certfile "./certs/cert.pem"