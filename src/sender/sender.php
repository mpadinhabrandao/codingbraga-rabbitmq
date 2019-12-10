<?php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;
$connection = new AMQPStreamConnection('rabbitmq', 5672, 'rabbitmq', 'rabbitmq');
$channel = $connection->channel();
$channel->queue_declare('task_queue', false, true, false, false);

$msg = new AMQPMessage(
    "${argv[1]} ${argv[2]}",
    array('delivery_mode' => AMQPMessage::DELIVERY_MODE_PERSISTENT)
);
$channel->basic_publish($msg, '', 'task_queue');
echo ' [x] Sent ', $data, "\n";
$channel->close();
$connection->close();