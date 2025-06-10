class Node:
    """Class representing a node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """Doubly linked list with insert and deletion operations."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a node with specified data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_from_start(self):
        """Delete the first node of the list."""
        if not self.head:
            print("List is empty. No node to delete from start.")
            return
        print(f"Deleting node from start with data: {self.head.data}")
        if self.head.next is None:
            # Only one node
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_from_end(self):
        """Delete the last node of the list."""
        if not self.head:
            print("List is empty. No node to delete from end.")
            return
        last = self.head
        if last.next is None:
            # Only one node
            print(f"Deleting the only node in list with data: {last.data}")
            self.head = None
            return
        while last.next:
            last = last.next
        print(f"Deleting node from end with data: {last.data}")
        # Disconnect last node
        last.prev.next = None

    def delete_by_value(self, data):
        """Delete the first node found with the specified data value."""
        if not self.head:
            print("List is empty. No node to delete by value.")
            return
        current = self.head
        while current:
            if current.data == data:
                print(f"Deleting node with data: {data}")
                # If node to delete is head
                if current.prev is None:
                    self.delete_from_start()
                # If node to delete is last
                elif current.next is None:
                    self.delete_from_end()
                else:
                    # Node in the middle
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return  # Delete only the first occurrence
            current = current.next
        print(f"Node with data {data} not found in the list.")

    def print_list(self):
        """Print the elements of the list."""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        print(" <-> ".join(values))


if __name__ == "__main__":
    # Demonstration of operations
    dll = DoublyLinkedList()
    print("Adding nodes 10, 20, 30, 40, 50 to the list.")
    for val in [10, 20, 30, 40, 50]:
        dll.append(val)
    print("Current list:")
    dll.print_list()

    print("\nDelete node from start:")
    dll.delete_from_start()
    dll.print_list()

    print("\nDelete node from end:")
    dll.delete_from_end()
    dll.print_list()

    print("\nDelete node by value 30:")
    dll.delete_by_value(30)
    dll.print_list()

    print("\nDelete node by value 100 (not in list):")
    dll.delete_by_value(100)
    dll.print_list()

