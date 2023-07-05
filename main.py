class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Linked List is empty!"

        itr = self.head
        to_return = ""

        while itr:
            to_return += str(itr.data) + "-->"
            itr = itr.next
        return to_return[:-3]

    def push_front(self, data):
        node = Node(data, self.head)
        self.head = node

    def push_back(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr.next:
            itr = itr.next
            count += 1

        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.push_front(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.push_back(data)


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert_values(["banana", "mango", "grapes", "orange"])
    linkedlist.insert_at(1, "blueberry")
    linkedlist.remove_at(2)
    print(linkedlist)

    linkedlist.insert_values([45, 7, 12, 567, 99])
    linkedlist.push_front(67)
    print(linkedlist)
