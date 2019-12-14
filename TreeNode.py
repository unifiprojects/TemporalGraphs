class TreeNode:

    def __init__(self, name, time):
        self.name = name
        self.list_of_nodes = []
        self.last_time_of_visit = time

    def set_name(self, name):
        self.name = name

    def add_node(self, node):
        self.list_of_nodes.append(node)

