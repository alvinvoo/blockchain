from blockchain.common.utils import text_to_bytes, bytes_to_text
from blockchain.common.hash import hash
from blockchain.common.config import config
from Crypto.Signature import pkcs1_15

class Key:
    K = ''

    def __init__(self, name, key, key_file_path, address):
        self.name          = name
        self.key           = key
        self.key_file_path = key_file_path
        self.address       = address
        self.key_format    = config.get('key_format')

    def __prepare_data_for_signing(self, data):
        if isinstance(data, str):
            data = text_to_bytes(data)
        return hash(data)

    def sign(self, unsigned_data):
        signature = pkcs1_15.new(self.key).sign(self.__prepare_data_for_signing(unsigned_data))
        return signature.decode('latin_1')

    def verify(self, unsigned_data, signature):
        try:
            signature = signature.encode('latin_1')
            pkcs1_15.new(self.key).verify(self.__prepare_data_for_signing(unsigned_data), signature)
            return True
        except ValueError as e:
            return False

    def get_public_key(self):
        return bytes_to_text(self.key.publickey().exportKey(self.key_format.upper()))

    def __repr__(self):
        return '{} {}'.format(self.name, self.address)