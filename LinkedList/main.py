from unittest.mock import sentinel


class Node:

    def __init__(self, value = None):
        self.value = value
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList:
    def __init__(self, initial_node=None):
        self.sentinel = Node(None)
        self.size = 0

        if initial_node:
            self.sentinel.set_next_node(initial_node)
            self.size = 1

    def iterate_list(self):

        if self.size == 0:
            return

        while self.sentinel is not None:
            print(self.sentinel.value)
            self.sentinel = self.sentinel.next_node

    # This function finds the cell before the target cell and returns it
    def find_cell_before(self, target):
        while self.sentinel.next_node is not None:
            if self.sentinel.next_node.value == target:
                return self.sentinel

            self.sentinel = self.sentinel.next_node

        return None

    # This function adds a new cell at the beginning of the list
    def add_at_beginning(self, element):
        new_node = Node(element)
        new_node.next_node = self.sentinel.next_node
        self.sentinel.next_node = new_node
        self.size = self.size + 1

    # This function adds a new cell at the end of the list
    def add_at_end(self,element):
        top = self.sentinel.next_node
        while top.next_node is not None:
           top = top.next_node

        new_node = Node(element)
        top.set_next_node(new_node)
        new_node.set_next_node(None)

    # This function returns
    def find_cell(self, target):
        top = self.sentinel.next_node

        while top.next_node is not None:
            if target == top.value:
                return top
            top = top.next_node

        return None

    # Insert a element after a specific element that exists within the list
    def insert_cell(self, target, element):
        if self.size == 0:
            self.add_at_beginning(element)
            return

        after_me = self.find_cell(target)
        new_cell = Node(element)
        new_cell.next_node = after_me.next_node
        after_me.next_node = new_cell

    def delete_cell(self, after_me):
        # Find the cell before the target cell
        target = self.find_cell_before(after_me).next_node

        # Set the cell before the target cell to the target cells next node
        self.find_cell_before(after_me).next_node = target.next_node



if __name__ == "__main__":

    linked_list = LinkedList()
    linked_list.add_at_beginning(1)
    linked_list.add_at_beginning(3)
    linked_list.add_at_end(5)
    linked_list.insert_cell(1,2)
    linked_list.delete_cell(3)
    linked_list.iterate_list()



