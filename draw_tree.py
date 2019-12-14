from graphviz import Digraph


def updateName(node, omonimi):
    if node.name not in omonimi.keys():
        omonimi[node.name] = 0
        return node.name
    else:
        omonimi[node.name] += 1
        return node.name + str(omonimi[node.name])


def getName(node, omonimi):
    if omonimi[node.name] == 0:
        return node.name
    else:
        return node.name + str(omonimi[node.name])


def draw_tree(tree_node_root):
    omonimi = {}
    g = Digraph()
    g.node(tree_node_root.name)
    updateName(tree_node_root, omonimi)
    queue = [tree_node_root]
    while queue:
        node = queue.pop(0)
        for child in node.list_of_nodes:
            queue.append(child)
            g.node(updateName(child, omonimi))
            g.edge(getName(node, omonimi), getName(child, omonimi), str(child.last_time_of_visit), minlen='2', dir="forward")
    g.view()





