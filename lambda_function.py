import json

def lambda_handler(event, context):
    print("Hello from Lambda gopi!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
