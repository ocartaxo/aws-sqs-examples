import boto3 as boto

import os
import json
import logging
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--create', help='create queue by providade name')
parser.add_argument('-l', '--list', action='store_true', help='list created queues')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


_REGION = 'sa-east-1'
_ENDPOINT_URL = 'http://localhost:9324'
_ACCESS_KEY = 'local'
_SECRET_ACCES_KEY = 'local'
_QUEUE_URL = _ENDPOINT_URL + '/queue/workerQueue'

sqs = boto.client('sqs', region_name=_REGION, endpoint_url=_ENDPOINT_URL,
                  aws_access_key_id=_ACCESS_KEY,
                  aws_secret_access_key=_SECRET_ACCES_KEY
                    )

def producer(event, context):
    status_code = 200
    message = ''

    if not event.get('body'):
        return {'statusCode': 400, 'body': json.dumps({'message': 'No body was found'})}

    try:
        sqs.send_message(
            QueueUrl=_QUEUE_URL,
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


def create(queue_name, attr=None):
    logger.info(f'Creating queue with name {queue_name}')
    sqs.create_queue(QueueName=queue_name)
    logger.info(f'{queue_name} was successfully created!')

def show_created_queues():
    queues = sqs.list_queues()
    print(queues)

if __name__ == "__main__":
    args = parser.parse_args()
    logger.info("Executando ação")
    if args.create:
        create(args.create)
    elif args.list:
        show_created_queues()
