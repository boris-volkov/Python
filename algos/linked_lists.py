class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return str(self.data) 

def search_list(L: ListNode, key: int):
    while L and L!= key:
        L = L.next
    return L

def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    node.next = node.next.next

def print_list(L: ListNode):
    while L:
        print(L.data)
        L = L.next

def has_cycle(head: ListNode):
    def cycle_len(end):
        start,step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            #finds start of cycle
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            #both iterators advance in tandem
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it #iter is the start of cycle
    return None #no cycle found

A = ListNode("a")
B = ListNode("b")
C = ListNode("c")
D = ListNode("e")
E = ListNode("d")
F = ListNode("f")

print(F)

insert_after(A,B)
insert_after(B,C)
insert_after(C,D)
insert_after(D,E)
insert_after(E,F)

#print_list(A)

#creating a cycle
G = ListNode("a")
insert_after(F,G)
G.next = C

#print_list(A)
print(has_cycle(A).data)

