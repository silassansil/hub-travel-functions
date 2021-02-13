import json

from custom_http import https_response as hr
from domain.excursion import Excursion
from dynamodb.dynamo_db_factory import DynamoDbFactory


def lambda_handler(event, context):
    if 'body' not in event:
        return hr.bad_request({'message': 'invalid body'})

    event = json.loads(event['body'])
    excursion = Excursion(event)
    _save_excursion(excursion)

    return hr.created(excursion.to_dict())


def _save_excursion(_excursion):
    instance = DynamoDbFactory.instance()
    table = instance.Table(_excursion.table_name())
    table.put_item(Item=_excursion.to_dict())
