import json
import os
from time import strftime, gmtime
import boto3
from botocore.exceptions import ClientError
from jinja2 import Environment, FileSystemLoader

import pdfkit

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.html")
table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])
s3_client = boto3.client("s3")
def lambda_handler(event, context):
    resp = table.scan()
    template_vars = {"losers": []}
    for i in range(resp["Count"]):
        template_vars["losers"].append({"phonenumber": resp["Items"][i]["phonenumber"], "count": resp["Items"][i]["c"]})
    rendered = template.render(template_vars)
    timestamp = strftime("%Y-%m-%d", gmtime())
    print(timestamp)
    pdfkit.from_string(rendered, '/tmp/'+timestamp+'.pdf')
    print(timestamp+'.pdf')
    upload_to_s3('/tmp/'+timestamp+'.pdf', timestamp+'.pdf')

def upload_to_s3(file_name, obj_name):
    bucket_name = os.environ["BUCKET_NAME"]
    try:
        response = s3_client.upload_file(file_name, bucket_name, obj_name)
    except ClientError as e:
        return e