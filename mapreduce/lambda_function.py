import os
import json
import boto3
ddb = boto3.resource("dynamodb")
def lambda_handler(event, context):
    print(event)
    if "NewImage" not in event["Records"][0]["dynamodb"]:
        return
    number = event["Records"][0]["dynamodb"]["NewImage"]["number"]["S"]
    resp = ddb.Table(os.environ["TABLE_NAME"]).get_item(
        Key = {
            "phonenumber": number
        }
    )
    print(resp)
    if "Item" not in resp:
        res = ddb.Table(os.environ["TABLE_NAME"]).put_item(
            Item = {
            'phonenumber': number,
            'c': 1
            }
        )
    else:
        ddb.Table(os.environ.get("TABLE_NAME")).update_item(
        Key={
            'phonenumber': number,
        },
        UpdateExpression="set c=:newcount",
        ExpressionAttributeValues={
            ":newcount": int(resp["Item"]["c"])+1
            },
        )