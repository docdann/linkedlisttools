# Converts text file to linked list per word


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addnode(self, sll):
        count = 0
        with open("test.txt","r") as f:
            line = f.readlines()
            for _ in line:
                for i in _.split():

                    if sll.head is None:
                        newnode = Node(i)
                        sll.head = newnode
                        newnode.next = None
                        count += 1
                    else:
                        cur = sll.head
                        while cur.next is not None:
                            cur = cur.next
                        cur.next = Node(i)
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
    sll.addnode(sll)
    sll.traversal(sll)


if __name__ == '__main__':
    main()
