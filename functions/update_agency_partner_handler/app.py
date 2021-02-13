import json

from boto3.dynamodb.conditions import Key

from custom_http import https_response as hr
from domain.agency import Agency
from dynamodb.dynamo_db_factory import DynamoDbFactory


def lambda_handler(event, context):
    if 'body' not in event:
        return hr.bad_request({'message': 'invalid body'})

    if 'pathParameters' not in event:
        return hr.bad_request({'message': 'missing params'})

    partners_id = json.loads(event['body'])
    agency_id = event['pathParameters']['agencyId']

    agency_found = _find_agency_by_id(agency_id)
    agency_found.add_partner(partners_id)

    _update_agency(agency_found)
    return hr.created(agency_found.__dict__)


def _find_agency_by_id(_agency_id):
    instance = DynamoDbFactory.instance()
    table = instance.Table('Agencies')
    response = table.query(
        KeyConditionExpression=Key('id').eq(_agency_id)
    )
    return Agency(response['Items'][0])


def _update_agency(_agency):
    instance = DynamoDbFactory.instance()
    table = instance.Table(_agency.table_name())
    table.put_item(Item=_agency.__dict__)


if __name__ == '__main__':
    input = {
        'body': {

        },
        'pathParameters': {
            'agencyId': 'b160d0f6-874f-42ce-865c-87b1b4b0579c'
        }
    }

    lambda_handler(json.dumps(input), None)
