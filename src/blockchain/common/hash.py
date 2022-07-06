from Crypto.Hash import SHA256
from blockchain.common.utils import text_to_bytes

def hash(data):
    return SHA256.new(data)

def hash_to_hex(data):
    return SHA256.new(data).hexdigest()

def hash_string(text):
    return hash(text_to_bytes(text)).digest()

def hash_string_to_hex(text):
    return hash_to_hex(text_to_bytes(text))
