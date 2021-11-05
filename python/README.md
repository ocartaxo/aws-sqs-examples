# AWS SQS Example using Python

## Setup
- Configure your [AWS Credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
- Install dependecies running `npm install`

## Deploy
Run `sls deploy`to create the lambdas and sqs. After running it you should output like this:

```bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
........
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service aws-python-sqs.zip file to S3 (12.46 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
................................................
Serverless: Stack update finished...
Service Information
service: aws-python-sqs
stage: dev
region: sa-east-1
stack: aws-python-sqs-dev
resources: 17
api keys:
  None
endpoints:
  POST - https://XXXXXXXXXX.execute-api.sa-east-1.amazonaws.com/dev/produce
functions:
  producer: dev-python-producer
  consumer: dev-python-consumer
layers:
  None

Toggle on monitoring with the Serverless Dashboard: run "serverless"
```


Calling the created API endpoint with `POST` request will invoke `producer` lambda function. See the example below
```
curl --request POST 'https://xxxxxx.execute-api.us-east-1.amazonaws.com/produce' --header 'Content-Type: application/json' --data-raw '{"name": "Paul McCartney"}'
```
In the response you should be able to see output like this:
```
{"message": "Message sucelly received!"}
```


## References
- [Standard Serverless configuration](https://github.com/serverless/examples/blob/master/aws-node-typescript-sqs-standard/serverless.yml)
- [Serverless offline SQS setup](https://github.com/CoorpAcademy/serverless-plugins/tree/master/packages/serverless-offline-sqs)