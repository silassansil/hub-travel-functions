from boto3.dynamodb.conditions import Key

from custom_http import https_response as hr
from domain.agency import Agency
from dynamodb.dynamo_db_factory import DynamoDbFactory


def lambda_handler(event, context):
    if 'pathParameters' not in event:
        return hr.bad_request({'message': 'missing params'})

    agency_id = event['pathParameters']['agencyId']
    agency_found = _find_agency_by_id(agency_id)

    return hr.ok(agency_found.__dict__)


def _find_agency_by_id(_agency_id):
    instance = DynamoDbFactory.instance()
    table = instance.Table('Agencies')
    response = table.query(
        KeyConditionExpression=Key('id').eq(_agency_id)
    )
    return Agency(response['Items'][0])
