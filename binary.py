#Define a tree
#Define an insert function  
#Building up a tree
#printing all nodes in order
#printing all nodes in Postorder
#printing all nodes in Preorder
#Breadth First search(bfs)-Algorithm using queues
#Depth first search(dfs) - Algoithm using stacks
#DFS Python code
#Searching for a key in tree
#Exercise - Tree top view

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self,data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def inOrderPrint(r):
    if r is None:
        return
    else:
        inOrderPrint(r.left)
        print(r.data, end=' ')
        inOrderPrint(r.right)

def preOrderPrint(r):
    if r is None:
        return
    else:
        print(r.data, end=' ')
        preOrderPrint(r.left)
        preOrderPrint(r.right)
        
if __name__ == '__main__':                 
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')
    
#print all nodes inorder
preOrderPrint(root)
    
