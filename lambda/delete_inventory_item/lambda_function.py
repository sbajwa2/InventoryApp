import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Inventory')

    table.delete_item(
        Key={
            'id': event['id'],
            'location_id': event['location_id']
        }
    )

    return {
        'statusCode': 200,
        'body': f"Item with ID {event['id']} at location {event['location_id']} deleted"
    }
