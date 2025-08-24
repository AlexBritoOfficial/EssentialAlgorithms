from collections import deque



class BinaryNode:

    def __init__(self, name):
        self.left_child = None
        self.right_child = None
        self.name = name

    def set_right_child(self, right_child):
        self.right_child = right_child

    def set_left_child(self, left_child):
        self.left_child = left_child

    """ Traversal Operations:         
        Binary Trees has four kinds of traversals preorder, inorder, postorder, and Breadth First
    """

    """
        Pre-Order Traversal ( Depth-First Traversal ) 
        In a preorder traversal, the algorithm processes a node, and then its left child, and then its right-child
    """

    def traverse_pre_order(self):
        print(self.name)
        if self.left_child is not None:
            self.left_child.traverse_pre_order()
        if self.right_child is not None:
            self.right_child.traverse_pre_order()

    """
        In-Order Traversal ( Depth-First Traversal ) 
        In an inorder or symmetric traversal, the algorithm processes a nodes left child, the node, and then the nodes right-child
    """

    def traverse_in_order(self):
        if self.left_child is not None:
            self.left_child.traverse_pre_order()

        print(self.name)

        if self.right_child is not None:
            self.right_child.traverse_pre_order()

    """
        Post-Order Traversal
        In a postorder traversal, the algorithm processes a nodes left child, and then its right-child, and then the node 
    """

    def traverse_post_order(self):
        if self.left_child is not None:
            self.left_child.traverse_pre_order()

        if self.right_child is not None:
            self.right_child.traverse_pre_order()

        print(self.name)

    def bfs(self):

        children = deque()

        children.append(self)

        while children:

            node = children.popleft()
            print(node.name)

            if node.left_child is not None:
                children.append(node.left_child)

            if node.right_child is not None:
                children.append(node.right_child)



if __name__ == "__main__":
    # Constructing a tree:
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6

    root = BinaryNode(1)
    node_2 = BinaryNode(2)
    node_3 = BinaryNode(3)
    node_4 = BinaryNode(4)
    node_5 = BinaryNode(5)
    node_6 = BinaryNode(6)

    # Set children
    root.set_left_child(node_2)
    root.set_right_child(node_3)

    node_2.set_left_child(node_4)
    node_2.set_right_child(node_5)

    node_3.set_right_child(node_6)

    root.bfs()
