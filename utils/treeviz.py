from graphviz import Digraph
from utils.graphs import BiNode, ltbt


def viz_tree(root: BiNode):
    graf = Digraph()

    q = [root]

    node_id, node_val = get_node_for_graph(root)
    graf.node(node_id, node_val)

    while q:
        now_node = q.pop(0)
        now_node_id, _ = get_node_for_graph(now_node)

        for node in (now_node.left, now_node.right):
            if node is not None:
                node_id, node_val = get_node_for_graph(node)
                graf.node(node_id, node_val)
                graf.edge(now_node_id, node_id)
                q.append(node)

    graf.render(filename='graph_out/result.dot')


def get_node_for_graph(node):
    node_id = str(id(node))
    node_val = str(node.val)
    return node_id, node_val


if __name__ == "__main__":
    test_arr = list(range(10))
    root = ltbt(test_arr)

    print(root)

    viz_tree(root)
