import random
from kdtree.Kd_Tree import Kd_Tree
from kdtree.Node import Node

if __name__ == '__main__':
    root = Node([random.randint(-1000, 1001), random.randint(-1000, 1001)], True)
    kd_tree = Kd_Tree(root)

    for i in range(100):
        node = Node([random.randint(-1000, 1001), random.randint(-1000, 1001)], True)
        kd_tree.add_node(node)

    kd_tree.print_tree(root)
