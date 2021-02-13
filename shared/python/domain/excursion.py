import uuid

from domain.abstract_domain import AbstractDomain


class Excursion(AbstractDomain):
    def __init__(self, data):
        self.id = data.get('id', str(uuid.uuid4()))
        self.destination = data['destination']
        self.departure = data['departure']
        self.armchairs = data['armchairs']
        self.description = data['description']
        self.owner_id = data['ownerId']

    def to_dict(self):
        return {
            'id': self.id,
            'destination': self.destination,
            'departure': self.departure,
            'armchairs': self.armchairs,
            'description': self.description,
            'ownerId': self.owner_id
        }

    def table_name(self):
        return 'Excursions'
