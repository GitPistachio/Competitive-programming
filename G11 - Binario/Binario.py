# Project name : SPOJ: G11 - Binario
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-02
# Description  :
# Status       : Accepted (23592215)
# Tags         : python, AVL tree, binary tree
# Comment      : My first AVLtree Yeah!

class Node:
    def __init__(self, data=None, parent=None, left_child=None, right_child=None, balance = 0):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.balance = balance

    def __str__(self):
        return "{} ({})".format(self.data, self.balance)

class AVLTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def search(self, data):
        top = self.root
        while top and top.data != data:
            if data < top.data:
                top = top.left_child
            else:
                top = top.right_child

        return top

    def getBalance(self, node):
        return node.balance

    def inorder(self, top):
        if top is None:
            return []

        order = self.inorder(top.left_child)
        order.append(top.data)
        order.extend(self.inorder(top.right_child))

        return order

    def preorder(self, top):
        if top is None:
            return []

        order = [top.data]
        order.extend(self.preorder(top.left_child))
        order.extend(self.preorder(top.right_child))

        return order

    def postorder(self, top):
        if top is None:
            return []

        order = self.postorder(top.left_child)
        order.extend(self.postorder(top.right_child))
        order.append(top.data)

        return order

    def rotateLeft(self, top):
        if top.right_child:
            node = top.right_child
            top.right_child = node.left_child

            if node.left_child:
                node.left_child.parent = top

            node.parent = top.parent
            if top.parent is None:
                self.root = node
            elif top == top.parent.left_child:
                top.parent.left_child = node
            else:
                top.parent.right_child = node

            node.left_child = top
            top.parent = node

    def rotateRight(self, top):
        if top.left_child:
            node = top.left_child
            top.left_child = node.right_child

            if node.right_child:
                node.right_child.parent = top

            node.parent = top.parent

            if top.parent is None:
                self.root = node
            elif top == top.parent.right_child:
                top.parent.right_child = node
            else:
                top.parent.left_child = node

            node.right_child = top
            top.parent = node

    def updateBalance(self, node, top):
        while node != top:
            parent = node.parent
            if parent.left_child == node:
                parent.balance -= 1
            else:
                parent.balance += 1
            node = parent

    def rebalance(self, top):
        if top.balance == -2:
            right_child = top.right_child
            left_child = top.left_child

            if left_child.balance == -1:
                left_child.balance = 0
                top.balance = 0
                self.rotateRight(top)
            else:
                left_grandchild = left_child.right_child
                self.rotateLeft(left_child)
                self.rotateRight(top)

                if left_grandchild.balance == -1:
                    left_child.balance = 0
                    top.balance = 1
                elif left_grandchild.balance == 0:
                    left_child.balance = 0
                    top.balance = 0
                else:
                    left_child.balance = -1
                    top.balance = 0

                left_grandchild.balance = 0

        elif top.balance == 2:
            right_child = top.right_child
            left_child = top.left_child

            if right_child.balance == 1:
                right_child.balance = 0
                top.balance = 0
                self.rotateLeft(top)
            else:
                right_grandchild = right_child.left_child
                self.rotateRight(right_child)
                self.rotateLeft(top)

                if right_grandchild.balance == 1:
                    right_child.balance = 0
                    top.balance = -1
                elif right_grandchild.balance == 0:
                    right_child.balance = 0
                    top.balance = 0
                else:
                    right_child.balance = 1
                    top.balance = 0

                right_grandchild = 0

    def insert(self, data):
        new_node = Node(data)

        parent = None
        node = self.root
        while node:
            parent = node
            if  new_node.data < node.data:
                node = node.left_child
            elif new_node.data > node.data:
                node = node.right_child
            else:
                break

        if parent:
            if new_node.data < parent.data:
                parent.left_child = new_node
            elif new_node.data > parent.data:
                parent.right_child = new_node
            else:
                return

            new_node.parent = parent
        else:
            self.root = new_node

        top = new_node
        while top != self.root:
            top = top.parent
            if top.balance:
                break

        self.updateBalance(new_node, top)
        self.rebalance(top)



avl = AVLTree()

for data in input().strip():
    avl.insert(data)

print(''.join(avl.inorder(avl.getRoot())))
print()
print(''.join(avl.preorder(avl.getRoot())))
print()
print(''.join(avl.postorder(avl.getRoot())))
