class Error(object):
    invalid_path_or_handler = "Invalid path or handler"


def is_valid(word):
    if word is None or word.isspace() or len(word) == 0:
        return False
    return True


class RouteTrieNode(object):
    not_found_handler = "not found handler"
    root_handler = "root handler"

    def __init__(self):
        self.children = {}
        self.handler = None


class RouteTrie:

    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, paths, handler):
        if paths is None or not is_valid(handler):
            return Error.invalid_path_or_handler

        current = self.root

        for path in paths:
            if path not in current.children:
                current.children[path] = RouteTrieNode()
            current = current.children[path]
        current.handler = handler

    def find(self, paths):
        if paths is None or len(paths) == 0:
            return RouteTrieNode.not_found_handler

        current = self.root

        for path in paths:
            if path not in current.children:
                return RouteTrieNode.not_found_handler
            current = current.children[path]

        return RouteTrieNode.not_found_handler if current.handler is None else current.handler


class Router:

    def __init__(self):
        self.trie = RouteTrie()

    def add_handler(self, path, handler):

        if not self.is_valid_path(path) or not is_valid(handler):
            return Error.invalid_path_or_handler

        paths = self.split_path(path)

        if not self.is_root(paths):
            self.trie.insert(paths, handler)

    def lookup(self, path):
        if not self.is_valid_path(path):
            return Error.invalid_path_or_handler
        paths = self.split_path(path)
        return RouteTrieNode.root_handler if self.is_root(paths) else self.trie.find(paths)

    def split_path(self, path):
        temp_paths = path.split("/")
        paths = []
        for path in temp_paths:
            if is_valid(path):
                paths.append(path)
        return paths

    def is_valid_path(self, path):
        return is_valid(path) and path[0] == "/"

    def is_root(self, paths):
        return len(paths) == 0


router = Router()

print('-x-x-x-x-x- Add handler Examples -x-x-x-x-x-')

router.add_handler("/home/about", "about handler")
router.add_handler("/home/about/osama", "osama handler")
router.add_handler("/google/employees/osama", "google osama handler")
print(router.add_handler(" google/employees/osama", "google osama handler"))  #  Invalid path or handler
print(router.add_handler("/google/employees/osama", ""))  #  Invalid path or handler
print(router.add_handler("", "handler"))  #  Invalid path or handler
print(router.add_handler(None, "handler"))  #  Invalid path or handler
print(router.add_handler(None, None))  #  Invalid path or handler
print(router.add_handler("/abc", None))  #  Invalid path or handler

print('-x-x-x-x-x- Look up Examples -x-x-x-x-x-')

print(router.lookup("/"))  # root handler
print(router.lookup("/                      "))  # root handler
print(router.lookup(" /                      "))  # Invalid path or handler
print(router.lookup("/home"))  # not found handler
print(router.lookup("/home/about"))  # about handler
print(router.lookup("/home/about/"))  # about handler
print(router.lookup("/home/about/me"))  # not found handler
print(router.lookup("home/about/me"))  # Invalid path or handler
print(router.lookup("/home/about/osama"))  # osama handler
print(router.lookup("/google/employees/osama"))  # google osama handler
print(router.lookup("                       "))  # Invalid path or handler
print(router.lookup(""))  # Invalid path or handler
print(router.lookup(None))  # Invalid path or handler
