
import os
import json
import boto3

def lambda_handler(event, context):
    client = boto3.resource("dynamodb")
    number = event["Details"]["ContactData"]["CustomerEndpoint"]["Address"]
    lang = event["Details"]["ContactData"]["LanguageCode"]
    uid = event["Details"]["ContactData"]["ContactId"]
    new_rickroll = client.Table(os.environ["TABLE_NAME"]).put_item(
        Item = {
            'uid': uid,
            'number': number,
            'lang': lang
        }
    )
    return new_rickroll