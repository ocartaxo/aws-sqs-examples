import { SQSEvent, SQSHandler } from "aws-lambda";

// lambda entypoint
export const handler: SQSHandler = async (event: SQSEvent) => {
    try {
        console.log(`Receive a ${event} from SQS`);
        for(const message of event.Records){
            const bodyData = message.body;
            console.log('Message Body -----> ', bodyData);
        }
    } catch(error){
        console.log(error)
    }
}