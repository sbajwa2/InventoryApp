import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Inventory')

    response = table.scan()

    return {
        'statusCode': 200,
        'body': response.get('Items', [])
    }
