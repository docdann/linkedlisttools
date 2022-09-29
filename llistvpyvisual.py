from vpython import *
import time


# Converts text file to linked list per word
# displays word as vpython object

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addnode(self, sll, textarr):
        count = 0
        colors = [color.blue, color.red, color.white]
        with open("test.txt", "r") as f:
            line = f.readlines()
            for _ in line:
                for i in _.split():

                    if sll.head is None:
                        newnode = Node(i)
                        sll.head = newnode
                        newnode.next = None
                        textarr.append(text(text=i, pos=vector(0, -count, count * 2), color=color.red))
                        count += 1
                        time.sleep(len(line) / count)
                    else:
                        cur = sll.head
                        while cur.next is not None:
                            cur = cur.next
                        cur.next = Node(i)
                        if count%2 == 0:
                            tempc = colors[0]
                        elif count %3 == 0:
                            tempc = colors[1]
                        else:
                            tempc = colors[2]
                        textarr.append(text(text=i, pos=vector(0, -count, count * 2 + (count / 5)), color=tempc,
                                            height=count / 5))
                        count += 1
                        time.sleep(len(line) / count)

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
