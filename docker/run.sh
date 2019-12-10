#!/bin/bash
docker-compose up -d --build
docker-compose exec sender composer install
docker-compose exec consumer composer install 


#sender 
php sender.php A 10
#consumer 
php consumer.php
#consumer-py 
php consumer.php