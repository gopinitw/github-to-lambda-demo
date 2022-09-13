import json

def lambda_handler(event, context):
    print("Hello from Lambda gopi!")
    print("Hello from gopi!")
    print("Hello from gv!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
