######## Doubly Linked List

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, prev, data, next):
        self.prev = prev
        self.data = data
        self.next = next

class DoublyLL:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(self.head, None, None)
        self.head.next = self.tail
        self.cur = self.tail

    def insert(self, loc, x):
        locprev = loc.prev
        insertx = Node(locprev, x, loc)
        loc.prev = insertx
        locprev.next = insertx

    def delete(self, loc):
        locprev = loc.prev
        locnext = loc.next
        locprev.next = locnext
        locnext.prev = locprev

    def print(self):
        loc = self.head.next
        while loc != self.tail:
            print(loc.data, end = '')
            loc = loc.next

if __name__ == '__main__':
    dl = DoublyLL()
    for i in input().rstrip():
        dl.insert(dl.tail, i)

    for _ in range(int(input())):
        cmd = input().split()

        if cmd[0] == 'L':
            if dl.cur.prev.prev != None:
                dl.cur = dl.cur.prev

        elif cmd[0] == 'D':
            if dl.cur.next != None:
                dl.cur = dl.cur.next

        elif cmd[0] == 'B':
            if dl.cur.prev.prev != None:
                dl.delete(dl.cur.prev)

        else:
            dl.insert(dl.cur, cmd[1])

dl.print()




########## Stack
import sys
input = sys.stdin.readline

l_stack = list(input().rstrip())
r_stack = []
N = int(input())

for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'L':
        if l_stack:
            r_stack.append(l_stack.pop())
        else: continue

    elif cmd[0] == 'D':
        if r_stack:
            l_stack.append(r_stack.pop())
        else: continue

    elif cmd[0] == 'B':
        if l_stack:
            l_stack.pop()
        else: continue

    elif cmd[0] == 'P':
        l_stack.append(cmd[1])

print(''.join(l_stack + r_stack[:: -1]))