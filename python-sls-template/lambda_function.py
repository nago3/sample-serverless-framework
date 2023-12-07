import os
import json

def lambda_handler(event, context):
    print("event", event)

    print("This is a Vlable test.", os.environ["SAMPLE_VALUE"])

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps("This is a serverless API sample.")
    }
