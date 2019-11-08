"""implementation of bloom filter"""
import hashlib
import math

from bitarray import bitarray


class BloomFilter:
    def __init__(self, capacity, prob_false_pos, hash_fn=None):
        self.capacity = capacity
        self.error_rate = prob_false_pos
        self.arraysize = self.calc_arraysize(capacity, prob_false_pos)
        self.hash_fn_num = self.calc_hash_num(capacity, prob_false_pos)
        self.bitarray = bitarray(self.arraysize, endian='little')
        self.bitarray.setall(False)
        if hash_fn is None:
            self.hashing = self.hash_fn()
        else:
            self.hashing = hash_fn

    def add(self, item):
        for i in range(self.hash_fn_num):
            digest = self.hashing(item) % self.arraysize
            if self.bitarray[digest] == False:
                return False
        return True

    def __contains__(self, item):
        digest = list()
        for i in range(self.hash_fn_num):
            digest = self.hashing(item) % self.arraysize
            digest.append(digest)
        return sum(self.bitarray[digest]) == self.hash_fn_num

    def calc_arraysize(self, capacity, prob_false_pos):
        """
        return the bitarray size
        m = n * (-log2(p) / ln2)
        n, the number of items to be stored
        p: false positive probability
        """
        size = -self.capacity * (math.log2(self.error_rate) / math.log(2))
        return int(size)

    def calc_hash_num(self, capacity, prob_false_pos):
        """
        return number of hashing function needed
        k = m/n * ln2
        m, the size of bitarray
        n, the number of items to be stored
        """
        size = self.calc_arraysize
        k = math.log(2) * (size / self.capacity)
        return int(k)

    def hash_fn(self):
        def generate_hash(key):
            m = hashlib.md5()
            m.update(str(key).encode('utf-8'))
            return int(m.hexdigest, 16)
        return generate_hash

    def is_same_cfg(self, other):
        return (self.error_rate == other.error_rate
                and self.arraysize == other.arraysize
                and self.hashing == other.hashing)

    def union(self, other):
        if self.is_same_cfg(other):
            self.bitarray = [a | b for a, b in zip(
                self.bitarray, other.bitarray)]
        else:
            raise ValueError

    def intersection(self, other):
        if self.is_same_cfg(other):
            self.bitarray = [a & b for a, b in zip(
                self.bitarray, other.bitarray)]
        else:
            raise ValueError


if __name__ == '__main__':
    states = '''Alabama Alaska Arizona Arkansas California Colorado Connecticut
        Delaware Florida Georgia Hawaii Idaho Illinois Indiana Iowa Kansas
        Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota
        Mississippi Missouri Montana Nebraska Nevada NewHampshire NewJersey
        NewMexico NewYork NorthCarolina NorthDakota Ohio Oklahoma Oregon
        Pennsylvania RhodeIsland SouthCarolina SouthDakota Tennessee Texas Utah
        Vermont Virginia Washington WestVirginia Wisconsin Wyoming'''.split()
