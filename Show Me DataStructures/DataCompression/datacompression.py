from heapq import heappush, heappop
import sys

class PriorityQueue(object):
    def __init__(self):
        self.heap = []

    def insert(self, node):
        heappush(self.heap, node)

    def get_min(self):
        if self.size() > 0:
            return self.heap[0]
        return None

    def extract_min(self):
        if self.size() > 0:
            return heappop(self.heap)
        return Node

    def size(self):
        return len(self.heap)


class Node(object):

    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __str__(self):
        return "Char : " + self.char + " frequency : " + str(self.frequency)

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __lt__(self, other):
        return self.frequency <= other.frequency

    def __eq__(self, other):
        return self.frequency == other.frequency

    def __ne__(self, other):
        return self.frequency != other.frequency

    def __gt__(self, other):
        return self.frequency > other.frequency

    def __ge__(self, other):
        return self.frequency < other.frequency

    def is_leaf(self):
        return self.left is None and self.right is None


class Tree(object):
    def __init__(self, root):
        self.root = root

    def get_root(self):
        return self.root


class DataCompressor(object):

    def get_frequency_table(self, data):
        frequency_table = {}
        for char in data:
            if char in frequency_table:
                frequency_table[char] += 1
            else:
                frequency_table[char] = 1

        return frequency_table

    def get_priority_list(self, frequency_table):

        p_queue = PriorityQueue()

        for key in frequency_table:
            node = Node(key, frequency_table[key])
            p_queue.insert(node)
        return p_queue

    def get_huffman_tree(self, p_queue):

        while p_queue.size() > 1:
            node1 = p_queue.extract_min()
            node2 = p_queue.extract_min()
            freq_sum = node1.frequency + node2.frequency
            root = Node(None, freq_sum)
            root.left = min(node1, node2)
            root.right = max(node1, node2)
            p_queue.insert(root)
        return Tree(p_queue.get_min())

    def get_bin_representation_table(self, huffman_tree, bin_table, bin_code, side):
        if huffman_tree is None:
            return bin_table

        if huffman_tree.is_leaf():
            bin_table[huffman_tree.char] = bin_code
            return bin_table

        bin_table.update(self.get_bin_representation_table(huffman_tree.left, bin_table, bin_code + "0", "left"))
        bin_table.update(self.get_bin_representation_table(huffman_tree.right, bin_table, bin_code + "1", "right"))

        return bin_table


    def encode_data(self, huffman_tree, data):
        result = ""
        bin_table = self.get_bin_representation_table(huffman_tree.root.left, {}, "0", "left")
        bin_table.update(self.get_bin_representation_table(huffman_tree.root.right, {}, "1", "right"))

        if len(bin_table) is 0:
            return 0
        data = self.process_data(data)
        for char in data:
            result += bin_table[char]
        return result


    def huffman_encoding(self, data):
        if self.is_data_valid(data) is False :
            return None, None
        frequency_table = self.get_frequency_table(self.process_data(data))
        p_queue = self.get_priority_list(frequency_table)
        huffman_tree = self.get_huffman_tree(p_queue)
        encoded_data = self.encode_data(huffman_tree, data)
        return encoded_data, huffman_tree

    def huffman_decoding(self, data, tree):
        if self.is_data_valid(data) is False or tree is None or tree.root is None:
            return None
        current = tree.root
        decoded_string = ""

        for bit in data:
            if current.is_leaf():
                decoded_string += " " if current.char == "-" else current.char
                current = tree.root
            current = current.left if bit == "0" else current.right
        decoded_string += " " if current.char == "-" else current.char
        return decoded_string

    def is_data_valid(self, data):
        return data is not None and data.isspace() is False and len(data) > 0

    def process_data(self,data):
        return str(data).replace(" ", "-")


if __name__ == "__main__":

    def show_results(data):
        compression_util = DataCompressor()
        encoded_data, tree = compression_util.huffman_encoding(data)

        if encoded_data is None or tree is None:
            print("Can't compress this data")
            return

        print("The size of the data is: {}\n".format(sys.getsizeof(data)))
        print("The content of the data is: {}\n".format(data))

        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = compression_util.huffman_decoding(encoded_data, tree)

        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))


    show_results(None)  # Can't compress this data
    show_results("      ")  # Can't compress this data
    show_results("")  # Can't compress this data
    show_results("AAB")  # Can't compress this data
    show_results("AAAAAAABBBCCCCCCCDDEEEEEE")  # right results
    show_results("AAB")  # right results
    show_results("The bird is the word")  # right results
    show_results("I will be in google soon :D ")  # right results
    show_results("My name is Osama. I am a software engineer. I like coding, cooking and weight lifting")  #right results

