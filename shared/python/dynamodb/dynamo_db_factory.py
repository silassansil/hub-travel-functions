import boto3


class DynamoDbFactory:
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = boto3.resource('dynamodb')
        return cls._instance
