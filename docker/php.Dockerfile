FROM php:7.4-apache


RUN apt-get update && apt-get install -y git libmcrypt-dev libmagickwand-dev 
RUN docker-php-ext-install bcmath gd intl opcache pdo_mysql sockets 

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
