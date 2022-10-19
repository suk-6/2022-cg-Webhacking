# vi Dockerfile_main
FROM python:3
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y iputils-ping net-tools
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 7777
# flag is at /
RUN echo "flag{sample}" > /???? 
CMD ["python", "./main.py"]

