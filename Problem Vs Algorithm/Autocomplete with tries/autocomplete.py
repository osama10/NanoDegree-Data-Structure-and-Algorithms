class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def is_empty(self):
        if len(self.children) == 0 or self.children is None:
            return True

        for key in self.children:
            if self.children[key] is None:
                return True

        return False

    def suffixes(self, suffix=''):
        if self.is_empty():
            return [suffix]
        result = []

        if self.is_word:
            result.append(suffix)

        for child in self.children:
            suffix += child
            result += self.children[child].suffixes(suffix)
            suffix = suffix[:-1]

        return result


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Add `word` to trie
        """
        if word is None or not self.is_valid(word):
            return

        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def remove(self, root, key, depth):
        if root is None or not self.is_valid(key):
            return None

        if len(key) == depth:
            if root.is_word:
                root.is_word = False

            if root.is_empty():
                del root
                root = None
            return root

        if key[depth] not in root.children:
            return None

        root.children[key[depth]] = self.remove(root.children[key[depth]], key, depth + 1)

        if root.is_empty():
            if root.is_word:
                root.children = {}
            else:
                del root
                root = None
        return root

    def find(self, word):
        if not self.is_valid(word) or self.root.is_empty():
            return None

        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node

    def exists(self, word):
        """
        Check if word exists in trie
        """
        result = self.find(word)
        return False if result is None else result.is_word

    def auto_complete(self, prefix):
        if not self.is_valid(prefix):
            return []
       
        resultant_node = self.find(prefix)

        if resultant_node is None:
            return []

        suffixes = resultant_node.suffixes()

        return [prefix + suggestion for suggestion in suffixes] if len(suffixes) > 0 else []

    def is_valid(self, word):
        if word is None or word.isspace() or len(word) == 0:
            return False
        return True


wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

trie = Trie()

for word in wordList:
    trie.insert(word)

print(trie.auto_complete(''))   #  Result = []
print(trie.auto_complete(None))   #  Result = []
print(trie.auto_complete('                             '))   #  Result = []
print(trie.auto_complete('123'))   #  Result = []
print(trie.auto_complete('an'))   #  Result = ['ant', 'anthology', 'antagonist', 'antonym']
print(trie.auto_complete('ant'))   #  Result = ['ant', 'anthology', 'antagonist', 'antonym']
print(trie.auto_complete('anto'))   #  Result = ['antonym']
print(trie.auto_complete('trig'))   #  Result = ['trigger', 'trigonometry']
print(trie.auto_complete('fun'))   #  Result = ['fun', 'function']



