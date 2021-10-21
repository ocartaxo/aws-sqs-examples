import { SQS } from 'aws-sdk'

const sqs = new SQS();

const sendMessage = async (queueUrl, body) => {
    try {
        
        await sqs.sendMessage({
            QueueUrl: queueUrl,
            MessageBody: body,
        }).promise();

    } catch (error) {
        console.log(error);
        return { message: error, statusCode: 500 }
    }

    return { message: 'Message placed in the SQS!', statusCode: 200 }
}

// lambda entrypoint
export const handler = async (event, context) => {

    if (!event.body) {
        return {
            statusCode: 400,
            body: {
                message: "Empty body!"
            }
        }
    }

    const region = context.invokedFunctionArn.split(':')[3];
    const accountId = context.invokedFunctionArn.split(':')[4];
    const queueName: string = 'FilaExemplo';

    const queueUrl:string = `https://sqs.${region}.amazonaws.com/${accountId}/${queueName}`; 

    return await sendMessage(queueUrl, event.body);
}
