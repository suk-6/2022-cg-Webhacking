FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install apache2 software-properties-common
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update && apt-get install -y libapache2-mod-php8.1 php8.1 php8.1-cli php8.1-mysql 
RUN a2enmod rewrite

COPY src/ /var/www/html
COPY ./apache2.conf /etc/apache2/apache2.conf
RUN chown www-data:www-data /var/www/html/uploads
RUN rm /var/www/html/index.html
RUN chmod 775 /var/www/html/uploads

EXPOSE 80
CMD apachectl -D FOREGROUND
