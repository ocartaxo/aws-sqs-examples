# Simple SQS Producer-Consumer using Serverless


## Setup
- Configure your [AWS Credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
- Install dependencies with `npm install`

## Usage
- Run `serverless deploy`
- To send a message to sqs use `serverless receiver:send --body="MESSAGE_HERE"`
- Run `serverless FUNCTION_NAME:logs` to show logs from your lambda function.


## References
- [Serverless-Lift](https://github.com/getlift/lift)
- [Serverless Framework](https://www.serverless.com/framework/docs)
- [AWS SQS using NodeJS+TS](https://github.com/serverless/examples/tree/master/aws-node-typescript-sqs-standard)
