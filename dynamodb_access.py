import boto3


def get_resource(): # Commented code for security reasons.
    # return boto3.resource('dynamodb',
                          # aws_access_key_id='',
                          # aws_secret_access_key='',
                          # region_name='eu-north-1')


def get_all_readings():
    client = get_resource()
    table = client.Table("kwh_readings")
    response = table.scan()
    return response['Items']