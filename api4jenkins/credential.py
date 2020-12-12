# encoding: utf-8


from .item import Item
from .mix import ConfigrationMix, DeletionMix


class Credentials(Item):

    def get(self, id):
        for item in self.api_json(tree='credentials[id]')['credentials']:
            if item['id'] == id:
                return Credential(self.jenkins,
                                  f'{self.url}credential/{id}/')
        return None

    def create(self, xml):
        self.handle_req('POST', 'createCredentials',
                        headers=self.headers, data=xml)

    def __iter__(self):
        for item in self.api_json(tree='credentials[id]')['credentials']:
            yield Credential(self.jenkins,
                             f'{self.url}credential/{item["id"]}/')


class Credential(Item, ConfigrationMix, DeletionMix):
    pass
