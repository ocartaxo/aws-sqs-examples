import json
import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

QUEUE_URL = os.getenv('QUEUE_URL')
SQS = boto3.client('sqs')


def producer(event, context):
    status_code = 200
    message = ''

    if not event.get('body'):
        return {'statusCode': 400, 'body': json.dumps({'message': 'No body was found'})}

    try:
        SQS.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=event['body']
        )

        message = 'Message sucelly received!'
    except Exception as e:
        logger.exception('Sending message to SQS queue failed!')
        message = str(e)
        status_code = 500

    return {'statusCode': status_code, 'body': json.dumps({'message': message})}


def consumer(event, context):
    logger.info(f'Receveing {str(event)} from SQS')
    for record in event['Records']:
        logger.info(f'Message body: {record["body"]}')