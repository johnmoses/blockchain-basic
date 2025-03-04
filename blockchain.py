""" 
Blockchain
"""

import hashlib
from time import time
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.create_block(previous_hash='1', nonce=100)

    def create_block(self, previous_hash, nonce):
        block = Block(index=len(self.chain) + 1,
                      timestamp=time(),
                      data=self.current_data,
                      previous_hash=previous_hash,
                      nonce=nonce)
        self.current_data = []
        self.chain.append(block)
        return block

    def add_data(self, sender, recipient, amount):
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block.index + 1

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_block):
        last_nonce = last_block.nonce
        last_hash = last_block.hash
        nonce = 0
        while not self.valid_proof(last_nonce, nonce, last_hash):
            nonce += 1
        return nonce

    @staticmethod
    def valid_proof(last_nonce, nonce, last_hash):
        guess = f'{last_nonce}{nonce}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
