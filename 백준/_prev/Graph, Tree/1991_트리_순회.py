def preorder(tree, start):
    s1, s2 = tree[start]
    print(start, end="")
    if s1 != ".":
        preorder(tree, s1)
    if s2 != ".":
        preorder(tree, s2)


def inorder(tree, start):
    s1, s2 = tree[start]
    if s1 != ".":
        inorder(tree, s1)
    print(start, end="")
    if s2 != ".":
        inorder(tree, s2)


def postorder(tree, start):
    s1, s2 = tree[start]
    if s1 != ".":
        postorder(tree, s1)
    if s2 != ".":
        postorder(tree, s2)
    print(start, end="")


import sys

sys.setrecursionlimit(10 ** 9)
f = sys.stdin.readline

N = int(f())
tree = {}

for i in range(N):
    par, s1, s2 = f().split()
    tree[par] = [s1, s2]


preorder(tree, "A")
print()
inorder(tree, "A")
print()
postorder(tree, "A")
