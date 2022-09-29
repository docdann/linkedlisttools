from vpython import *
import time
import os


# Converts text file to linked list per word
# displays word as vpython object

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # graphics attribute will hold the vpython object to the linked list item
        self.graphics = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addsinglenode(self, sll, count):

        colors = [color.blue, color.red, color.white]

        templine = input("New node: ").strip()
        if len(templine) == 0:
            sll.addsinglenode(sll, count)
        elif templine == "/b":
            sll.traversal(sll)
            sll.addsinglenode(sll, count)
        else:
            if sll.head is None:

                newnode = Node(templine)
                newnode.graphics = text(text=templine, pos=vector(0, -count, count * 2), color=color.red)
                sll.head = newnode
                newnode.next = None
                count += 1
                sll.addsinglenode(sll, count)
            else:
                cur = sll.head
                while cur.next is not None:
                    cur = cur.next
                cur.next = Node(templine)
                if count % 2 == 0:
                    tempc = colors[0]
                elif count % 3 == 0:
                    tempc = colors[1]
                else:
                    tempc = colors[2]
                cur.next.graphics = text(text=templine, pos=vector(0, -count, count * 2 + (count / 5)), color=tempc,
                                         height=count / 5)

                count += 1
                sll.addsinglenode(sll, count)

    def traversal(self, sll):
        if sll.head is None:
            print("List is empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end="-->")
                cur = cur.next
            print("\n")


def main():

    sll = LinkedList()

    count = 0
    sll.addsinglenode(sll, count)
    while True:
        pass


if __name__ == '__main__':
    main()
