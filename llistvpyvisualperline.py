from vpython import *


# Converts text file to linked list per word


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addnode(self, sll, textarr):
        count = 0
        with open("test.txt", "r") as f:
            line = f.readlines()
            for _ in line:

                if sll.head is None:
                    newnode = Node(_)
                    sll.head = newnode
                    newnode.next = None
                    textarr.append(text(text=_, pos=vector(0, -count, count * 2), color=color.green, height=count))

                    count += 1
                else:
                    cur = sll.head
                    while cur.next is not None:
                        cur = cur.next
                    cur.next = Node(_)
                    textarr.append(text(text=_, pos=vector(0, 0, count), color=color.red))
                    count += 1

    def traversal(self, sll):
        if sll.head is None:
            print("List is empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end="-->")
                cur = cur.next


def main():
    # This happens if savedll.pkl does not exist

    sll = LinkedList()
    textarr = []
    sll.addnode(sll, textarr)
    sll.traversal(sll)
    while True:
        pass


if __name__ == '__main__':
    main()
