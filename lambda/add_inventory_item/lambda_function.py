import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Inventory')

    item = {
        'id': event['id'],
        'location_id': event['location_id'],
        'item_name': event['item_name'],
        'item_description': event['item_description'],
        'item_qty_on_hand': event['item_qty_on_hand'],
        'item_price': event['item_price']
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': f"Item {item['item_name']} added successfully"
    }
