#!/bin/bash
mkdir tmp
cp lambda_function.py tmp/
cp requirements.txt tmp/
cd tmp/
pip3 install --target . -r requirements.txt
zip -r package.zip *
cp package.zip ../
rm -rf tmp/
aws lambda update-function-code --function-name collectrickroll --zip-file fileb://package.zip --region us-west-2