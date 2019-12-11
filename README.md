# CodingBraga - RabbitMQ

```bash
git clone https://github.com/mpadinhabrandao/codingbraga-rabbitmq

cd docker
docker-compose up -d

docker-compose exec sender composer install
docker-compose exec consumer composer install


docker-compose exec sender php sender.php A 10
docker-compose exec consumer php consumer.php
docker-compose exec consumer-py python /app/consumer.py
```
