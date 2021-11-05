#!/bin/sh
trap "exit 1" INT

AWS_ENDPOINT_URL=${AWS_ENDPOINT_URL:-http://localhost:9324}

QUEUES="workerQueue workerDLQ"
for QUEUE in $QUEUES
do 
    until aws sqs --endpoint-url ${AWS_ENDPOINT_URL} get-queue-url --queue-name ${QUEUE}  > /dev/null 2> /dev/null
    do
        echo "Creating queue $QUEUE"
        aws sqs --endpoint-url ${AWS_ENDPOINT_URL} create-queue \
            --queue-name ${QUEUE} \
            > /dev/null 2> /dev/null
    done &
    echo "$QUEUE was created"
done


wait

trap - INT