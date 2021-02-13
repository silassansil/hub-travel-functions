import json


def _response(_status_code, _body):
    return {
        'statusCode': _status_code,
        'headers': {},
        'body': json.dumps(_body)
    }


def ok(_body):
    return _response(200, _body)


def created(_body):
    return _response(201, _body)


def bad_request(_body):
    return _response(400, _body)


def not_found(_body):
    return _response(404, _body)
