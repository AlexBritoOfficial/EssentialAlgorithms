
class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node

if __name__ == "__main__":
    linked_list = Node(5)
    linked_list.set_next_node(Node(6))
    linked_list.next_node.set_next_node(Node(7))

    while  linked_list is not None:
        print(linked_list.value)
        linked_list = linked_list.next_node
