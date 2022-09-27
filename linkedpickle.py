# Creating a linked list will require a Node class and LinkedList class
# Nodes
# define __init__ where  self.next = None  and self.data = data
import pickle
import os.path


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addnode(self, sll):
        count = 0
        while count < 5:
            if sll.head is None:
                newnode = Node(input("New node data: "))
                sll.head = newnode
                newnode.next = None
                count += 1
                print(sll.head.data)
            else:
                cur = sll.head
                while cur.next is not None:
                    cur = cur.next
                cur.next = Node(input("New node data: "))
                print(cur.next.data)
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
    if os.path.exists("savedll.pkl"):
        # Checking if there is a linked list pickle file already saved
        with open("savedll.pkl", "rb") as f2:
            # opening the pickle file as f2
            unpickledll = pickle.load(f2)
            if isinstance(unpickledll, LinkedList):
                # Checking if the object saved in savedll.pkl has the same type as LinkedList
                print("linked list")
                sll = unpickledll
                sll.addnode(sll)
                sll.traversal(sll)
                with open("savedll.pkl", "wb") as f:
                    pickle.dump(sll, f)
                    f.close()
            else:

                sll = LinkedList()
                sll.addnode(sll)
                sll.traversal(sll)
                with open("savedll.pkl", "wb") as f:
                    pickle.dump(sll, f)
                    f.close()
    else:
        # This happens if savedll.pkl does not exist

        sll = LinkedList()
        sll.addnode(sll)
        sll.traversal(sll)
        with open("savedll.pkl", "wb") as f:
            pickle.dump(sll, f)
            f.close()


if __name__ == '__main__':
    main()
