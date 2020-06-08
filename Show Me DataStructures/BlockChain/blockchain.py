import hashlib
from datetime import datetime


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = Block.timestamp()
        self.block_data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def __str__(self):
        return "[ " + str(self.block_data) + " - " + self.hash + " ]"

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "{}-{}-{}".format(self.block_data, self.timestamp, self.previous_hash).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    @classmethod
    def timestamp(cls):
        return datetime.timestamp(datetime.now())


class BlockChain(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head is None:
            return "Empty block chain"

        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.block_data) + " -> "
            cur_head = cur_head.next
        return out_string[0:len(out_string)-3]

    def append(self, data):

        if self.head is None:
            self.head = Block(data, None)
            self.tail = self.head
        else:
            prev_hash = self.tail.previous_hash
            block = Block(data, prev_hash)
            self.tail.next = block
            self.tail = block


block0 = Block("block0", None)
block1 = Block("block1", block0.hash)
block2 = Block("block2", block1.hash)
block3 = Block("block3", block2.hash)
block4 = Block("block4", block3.hash)

block_chain = BlockChain()
block_chain.append(block0)
block_chain.append(block1)
block_chain.append(block2)
block_chain.append(block3)
block_chain.append(block4)

print(block_chain)


try:
    block_with_no_params = Block()

except:
    print("No params Error")


try:
    block_with_no_data = Block(previous_hash="")

except:
    print("No data Error")

try:
    block_with_no_prev_hash = Block(data="")

except:
    print("No prev hash Error")

no_block_block_chain = BlockChain()
print(no_block_block_chain)