import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Inventory')

    response = table.query(
        IndexName='location_id-id-index',  # Replace with your actual GSI name if different
        KeyConditionExpression=boto3.dynamodb.conditions.Key('location_id').eq(event['location_id'])
    )

    return {
        'statusCode': 200,
        'body': response.get('Items', [])
    }
