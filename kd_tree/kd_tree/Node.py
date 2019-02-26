"""
    Class that define a single node in
    a kd_tree. Kd_Tree is similar to Binary
    Search Tree, but in a node there is a
    parameter that define what splits tree.
"""


class Node(object):
    def __init__(self, coord, split):
        """
        :type split: bool
        :type coord: list
        """
        self.coord = coord
        self.split = split
        self.left = None
        self.right = None

    @property
    def coord(self):
        """
        :rtype: list
        """
        return self.__coord

    @coord.setter
    def coord(self, coord):
        self.__coord = coord

    @property
    def split(self):
        """
        :rtype: bool
        """
        return self.__split

    @split.setter
    def split(self, split):
        self.__split = split

    @property
    def left(self):
        """
        :rtype: Node
        """
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        """
        :rtype: Node
        """
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right
