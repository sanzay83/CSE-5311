class BinarySearchTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = BinarySearchTreeNode(key)
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        parent = None
        while current is not None:
            parent = current
            if key < current.val:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent
        if key < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node
    
    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.val:
                return current
            elif key < current.val:
                current = current.left
            else:
                current = current.right
        return None
    
    def delete(self, key):
        node = self.search(key)
        if node is None:
            return
        
        if node.left is None:
            self._transplant(node, node.right)
        elif node.right is None:
            self._transplant(node, node.left)
        else:
            successor = self._minimum(node.right)
            if successor.parent != node:
                self._transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self._transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent
    
    def _minimum(self, node):
        while node.left is not None:
            node = node.left
        return node


class RedBlackTreeNode:
    def __init__(self, key, color='red'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
    
class RedBlackTree:
    RED = True
    BLACK = False

    def __init__(self):
        self.NIL_LEAF = RedBlackTreeNode(key=None, color='black')
        self.root = self.NIL_LEAF
    
    def insert(self, key):
        new_node = RedBlackTreeNode(key)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF
        new_node.parent = None        
        current = self.root
        parent = None
        while current != self.NIL_LEAF:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        
        self.fix_insert(new_node)
    
    def fix_insert(self, node):
        while node != self.root and node.parent.color == self.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == self.RED:
                    node.parent.color = self.BLACK
                    uncle.color = self.BLACK
                    node.parent.parent.color = self.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = self.BLACK
                    node.parent.parent.color = self.RED
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == self.RED:
                    node.parent.color = self.BLACK
                    uncle.color = self.BLACK
                    node.parent.parent.color = self.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = self.BLACK
                    node.parent.parent.color = self.RED
                    self.left_rotate(node.parent.parent)
            self.root.color = self.BLACK
    
    def delete(self, key):
        node_to_delete = self.search(key)
        if node_to_delete == self.NIL_LEAF:
            return
        
        original_color = node_to_delete.color
        if node_to_delete.left == self.NIL_LEAF:
            temp_node = node_to_delete.right
            self._transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL_LEAF:
            temp_node = node_to_delete.left
            self._transplant(node_to_delete, node_to_delete.left)
        else:
            successor = self._minimum(node_to_delete.right)
            original_color = successor.color
            temp_node = successor.right
            if successor.parent == node_to_delete:
                temp_node.parent = successor
            else:
                self._transplant(successor, successor.right)
                successor.right = node_to_delete.right
                successor.right.parent = successor
            self._transplant(node_to_delete, successor)
            successor.left = node_to_delete.left
            successor.left.parent = successor
            successor.color = node_to_delete.color
        
        if original_color == self.BLACK:
            self.fix_delete(temp_node)
  
    def fix_delete(self, node):
        while node != self.root and node.color == self.BLACK:
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == self.RED:
                    sibling.color = self.BLACK
                    node.parent.color = self.RED
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                
                if sibling.left.color == self.BLACK and sibling.right.color == self.BLACK:
                    sibling.color = self.RED
                    node = node.parent
                else:
                    if sibling.right.color == self.BLACK:
                        sibling.left.color = self.BLACK
                        sibling.color = self.RED
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    
                    sibling.color = node.parent.color
                    node.parent.color = self.BLACK
                    sibling.right.color = self.BLACK
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == self.RED:
                    sibling.color = self.BLACK
                    node.parent.color = self.RED
                    self.right_rotate(node.parent)
                    sibling = node.parent.left
                
                if sibling.right.color == self.BLACK and sibling.left.color == self.BLACK:
                    sibling.color = self.RED
                    node = node.parent
                else:
                    if sibling.left.color == self.BLACK:
                        sibling.right.color = self.BLACK
                        sibling.color = self.RED
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    
                    sibling.color = node.parent.color
                    node.parent.color = self.BLACK
                    sibling.left.color = self.BLACK
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = self.BLACK

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL_LEAF:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL_LEAF:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def _minimum(self, node):
        while node.left != self.NIL_LEAF:
            node = node.left
        return node
    
    def search(self, key):
        current = self.root
        while current != self.NIL_LEAF:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return self.NIL_LEAF
    

class AVLTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = AVLTreeNode(key)
        if self.root is None:
            self.root = new_node
            return
        self.root = self._insert(self.root, new_node)
    
    def _insert(self, node, new_node):
        if node is None:
            return new_node
        
        if new_node.key < node.key:
            node.left = self._insert(node.left, new_node)
            node.left.parent = node
        else:
            node.right = self._insert(node.right, new_node)
            node.right.parent = node
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and new_node.key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and new_node.key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and new_node.key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and new_node.key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node
    
    def delete(self, key):
        if self.root is None:
            return
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._get_minimum(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        
        if node is None:
            return node
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2

        if T2 is not None:
            T2.parent = z
        y.parent = z.parent
        z.parent = y
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        if T3 is not None:
            T3.parent = z
        y.parent = z.parent
        z.parent = y
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _get_minimum(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node
    
    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    print(bst.search(7).val)
    bst.delete(5)

    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(30)
    rbt.insert(15)
    rbt.delete(20)
    print(rbt.search(20).key)

    avl = AVLTree()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(25)
    print(avl.search(25).key)
    avl.delete(20)
        