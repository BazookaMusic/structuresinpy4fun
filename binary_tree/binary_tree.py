class Node():
    def __init__(self, l, r, contents):
        self.l = l
        self.r = r
        self.contents = contents
    
    @staticmethod
    def post_order(node):
        if not node:
            return
        yield from  Node.post_order(node.l)
        yield from  Node.post_order(node.r)
        yield node
    
    @staticmethod
    def in_order(node):
        if not node:
            return
        yield from  Node.in_order(node.l)
        yield node
        yield from  Node.in_order(node.r)

    @staticmethod
    def pre_order(node):
        if not node:
            return
        yield node
        yield from  Node.pre_order(node.l)
        yield from  Node.pre_order(node.r)
    
   

class BinaryTree():
    """A binary tree class with a reference to the root"""
    def __init__(self, root = None):
        self.root = root
    
    def in_order(self):
        """ traversal generator for in order traversal"""
        yield from Node.in_order(self.root)
    
    def post_order(self):
        """ traversal generator for post order"""
        yield from  Node.post_order(self.root)
    
    def pre_order(self):
        """ traversal generator for pre_order """
        yield from  Node.pre_order(self.root)
    

    def reverse(self):
        """ reverse binary tree in place,
        returns the binary tree for chaining"""
        def rev_helper(node):
            """helper function to reverse at a 
            certain node"""   
            if not node:
                return

            temp = node.r
            node.r = node.l
            node.l = temp

            rev_helper(node.r)
            rev_helper(node.l)

        rev_helper(self.root)

        return self
    
    @staticmethod
    def toBinaryTree(node):
        """ wrap a node in a BinaryTree class"""
        return BinaryTree(node)


        

# example code
if __name__ == "__main__":
    a = Node(None,None,1)
    b = Node(None,None,2)
    c = Node(b,a,3)


    a = Node(None,None,6)
    b = Node(a,None,5)
    e = Node(c,b,4)

    d = BinaryTree(e)
    for el in d.reverse().pre_order():
        print(el.contents)

    

    

    