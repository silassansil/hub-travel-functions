import json

from custom_http import https_response as hr
from domain.agency import Agency
from dynamodb.dynamo_db_factory import DynamoDbFactory


def lambda_handler(event, context):
    if 'body' not in event:
        return hr.bad_request({'message': 'invalid body'})

    event = json.loads(event['body'])
    agency = Agency(event)
    _save_agency(agency)

    return hr.created(agency.__dict__)


def _save_agency(_agency):
    instance = DynamoDbFactory.instance()
    table = instance.Table(_agency.table_name())
    table.put_item(Item=_agency.__dict__)
