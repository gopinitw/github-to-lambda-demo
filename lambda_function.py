import json

def lambda_handler(event, context):
    print("Hello from Lambda gopi!")
    print("Hello from Lambda gv!")
    print("Hello from Lambda geervani!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
