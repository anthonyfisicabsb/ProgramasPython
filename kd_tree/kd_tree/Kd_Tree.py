class Kd_Tree(object):
    def __init__(self, root):
        self.root = root

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        self.__root = root

    def add_node(self, node):
        no_atual = self.root
        can_insert = True

        while can_insert:
            if no_atual.split:
                can_insert = self.__compare_node(no_atual, node, 0)
            else:
                can_insert = self.__compare_node(no_atual, node, 1)

    def print_tree(self, node):
        if node is not None:
            print(node.coord)
            self.print_tree(node.right)
            self.print_tree(node.left)

    def __compare_node(self, no_atual, node, pos):
        """
        :type pos: int
        :type node: Node
        :type no_atual: Node
        :rtype: bool
        """
        if no_atual.coord[pos] <= node.coord[pos]:
            if no_atual.right is None:
                node.split = not no_atual.split
                no_atual.right = node

                return False

            no_atual = no_atual.right
        else:
            if no_atual.left is None:
                node.split = not no_atual.split
                no_atual.left = node

                return False

            no_atual = no_atual.left

        return True
