from graphviz import Digraph
import copy


def get_new_name(nodes, name):
    name = name.split('-')[0]
    for i in range(1, len(nodes)):
        new_name = name + "-" + str(i)
        if new_name not in nodes:
            return new_name


def change_duplicate_names(copy_tree_node):
    nodes = [copy_tree_node.name]
    queue = [copy_tree_node]
    while queue:
        node = queue.pop(0)
        for child in node.list_of_nodes:
            queue.append(child)
            if child.name not in nodes:
                nodes.append(child.name)
            else:
                child.name = get_new_name(nodes, child.name)
                nodes.append(child.name)


def draw_tree(tree_node_root):
    copy_tree_node = copy.deepcopy(tree_node_root)
    change_duplicate_names(copy_tree_node)

    g = Digraph()
    g.node(copy_tree_node.name)
    queue = [copy_tree_node]
    while queue:
        node = queue.pop(0)
        for child in node.list_of_nodes:
            queue.append(child)
            g.node(child.name)
            g.edge(node.name, child.name, str(child.last_time_of_visit), minlen='2', dir="forward")

    g.view()
