#import boto3
#import json

#ec2 = boto3.client('ec2')
#def lambda_handler(event, context):
#    response = ec2.describe_availability_zones()
#    return {"statusCode": 200, "body": json.dumps(response)}
#hello hi
import json
import bs4 as bs
from urllib import request
def lambda_handler(event, context):
    # TODO implement
    html_data = request.urlopen("https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/").read()
    soup = bs.BeautifulSoup(html_data,'lxml')
    title = soup.find('h2')
    return {
        "statusCode": 200,
        "body": json.dumps(title.text)
    }
