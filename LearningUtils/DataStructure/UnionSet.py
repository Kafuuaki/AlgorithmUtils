from collections import defaultdict

# https://www.geeksforgeeks.org/linked-list-representation-disjoint-set-data-structures/


class Node:
    def __init__(self, val, item_ptr):
        self.val = val
        self.item_ptr = item_ptr
        self.next = None


class Item:
    def __init__(self, hd, tl):
        self.hd = hd
        self.tl = tl


class ListSet:
    def __init__(self):
        self.node_address = defaultdict(lambda: None)

    def makeset(self, a):
        new_set = Item(Node(a, None), None)
        new_set.hd.item_ptr = new_set
        new_set.tl = new_set.hd
        self.node_address[a] = new_set.hd

    def find(self, key):
        node = self.node_address[key]
        return node.item_ptr

    def union(self, i1, i2):
        cur = i2.hd
        while cur:
            cur.item_ptr = i1
            cur = cur.next
        i1.tl.next = i2.hd
        i1.tl = i2.tl
        del i2


def main():
    a = ListSet()
    a.makeset(13)
    a.makeset(25)
    a.makeset(45)
    a.makeset(65)

    print(f"find(13): {a.find(13)}")
    print(f"find(25): {a.find(25)}")
    print(f"find(65): {a.find(65)}")
    print(f"find(45): {a.find(45)}")
    print()
    print("Union(find(65), find(45))")
    a.union(a.find(65), a.find(45))
    print(f"find(65): {a.find(65)}")
    print(f"find(45): {a.find(45)}")


if __name__ == "__main__":
    main()
