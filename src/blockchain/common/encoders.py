from blockchain.common.blockchain import Blockchain
from blockchain.common.block import Block
from blockchain.common.transaction import Transaction

import json, pprint

def blockchain_decode(blockchain_json):
    blockchain_dict = json.loads(blockchain_json)

    blockchain = Blockchain()
    for block_dict in blockchain_dict['blocks']:
        block = block_from_dict(block_dict)
        blockchain.add_block(block)

    return blockchain

def blockchain_to_dict(blockchain):
    return {'blocks' : list(map(block_to_dict, blockchain.blocks))}

def blockchain_encode(blockchain):
    blockchain_dict = blockchain_to_dict(blockchain)
    return json.dumps(blockchain_dict, sort_keys=True)

def block_from_dict(block_dict):
    block = Block()
    block.id = block_dict['id']
    block.previous_block_id = block_dict['previous_block_id']
    block.transactions = list(map(transaction_from_dict, block_dict['transactions']))
    block.nonce = block_dict['nonce']
    return block

def block_to_dict(block):
    return {
        'id' : block.id,
        'previous_block_id' : block.previous_block_id,
        'transactions' : list(map(transaction_to_dict, block.transactions)),
        'nonce' : block.nonce
    }

def block_decode(block_json):
    block_dict = json.loads(block_json)
    return block_from_dict(block_dict)

def block_encode(block, include_id = True):
    block_dict = block_to_dict(block)
    if not include_id:
        block_dict['id'] = None
    return json.dumps(block_dict, sort_keys=True)

def block_list_decode(block_list_json):
    block_list = json.loads(block_list_json)
    return list(map(block_from_dict, block_list))

def block_list_encode(block_list):
    return json.dumps(list(map(block_to_dict, block_list)))

def transaction_from_dict(transaction_dict):
    transaction = Transaction(transaction_dict['from_address'], transaction_dict['amount'],
        transaction_dict['to_address'], transaction_dict['public_key'])

    transaction.timestamp = transaction_dict['timestamp']
    transaction.signature = transaction_dict['signature']
    transaction.id        = transaction_dict['id']

    return transaction

def transaction_to_dict(transaction):
    return {
        'from_address' : transaction.from_address,
        'amount'       : transaction.amount,
        'to_address'   : transaction.to_address,
        'timestamp'    : transaction.timestamp,
        'public_key'   : transaction.public_key,
        'signature'    : transaction.signature,
        'id'           : transaction.id
    }

def transaction_decode(transaction_json):
    transaction_dict = json.loads(transaction_json)
    return transaction_from_dict(transaction_dict)

def transaction_encode(transaction):
    return json.dumps(transaction_to_dict(transaction), sort_keys=True)

def transaction_list_decode(transaction_list_json):
    transaction_list = json.loads(transaction_list_json)
    return list(map(transaction_from_dict, transaction_list))

def transaction_list_encode(transaction_list):
    return json.dumps(list(map(transaction_to_dict, transaction_list)))
