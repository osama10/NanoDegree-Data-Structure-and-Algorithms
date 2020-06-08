class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.users_cache = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)
        self.users_cache.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def has_user(self, user):
        if user in self.users_cache:
            return True
        return False


def is_user_in_group(user, group):

    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if len(group.users) < 1:
        return False

    if group.has_user(user):
        return True

    for child_group in group.groups:
        if is_user_in_group(user, child_group):
            return True

    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent))  # print true
print(is_user_in_group("asdasdasd", parent))  # print false
print(is_user_in_group("osama", Group("nanodegree")))  # print false

empty_group = Group("Empty group")
print(is_user_in_group("asda", empty_group))  # print false
print(empty_group.get_groups())  # returns empty
print(empty_group.get_users())  # returns empty
