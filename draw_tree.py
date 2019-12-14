from graphviz import Digraph


def draw_tree(tree_node_root):
    g = Digraph()
    queue = [tree_node_root]
    while queue:
        node = queue.pop(0)
        g.node(node.name)
        for child in node.list_of_nodes:
            queue.append(child)
            g.edge(node.name, child.name, str(child.last_time_of_visit), minlen='2', dir="forward")
    g.view()





