""" 
Flask App
"""

from flask import Flask, jsonify
from uuid import uuid4
from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    nonce = blockchain.proof_of_work(last_block)
    blockchain.add_data(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )
    previous_hash = last_block.hash
    block = blockchain.create_block(previous_hash, nonce)
    response = {
        'message': "New Block Forged",
        'index': block.index,
        'data': block.data,
        'previous_hash': block.previous_hash,
        'nonce': block.nonce,
        'hash': block.hash,
    }
    return jsonify(response), 200
    
@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': [block.__dict__ for block in blockchain.chain],
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)