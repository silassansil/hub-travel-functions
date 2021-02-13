import uuid

from domain.abstract_domain import AbstractDomain


class Agency(AbstractDomain):
    def __init__(self, data):
        self.id = data.get('id', str(uuid.uuid4()))
        self.name = data.get('agencyName')
        self.cnpj = data.get('cnpj')
        self.partners = [Agency(p) for p in data.get('partners', [])]
        self.representative = {
            'name': data.get('representativeName'),
            'cpf': data.get('cpf'),
            'phone': data.get('phone'),
            'email': data.get('email'),
        }

    def retrieve_partners_id(self):
        return [p.id for p in self.partners]

    def add_partner(self, _new_partners):
        self.partners.extend(_new_partners)

    def table_name(self):
        return 'Agencies'
