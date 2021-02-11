class Node:
    def __init__(self, x, next, random=None):

        self.val=int(x)
        self.next=None
        self.random=None

class Solution:

    def __init__(self):
        self.visited={}

    def copyRandom(self, head):

        #1st case if head is not availble then return None
        if head==None:
            return None
        
        #2nd case if the head is already in the visited hash then return it
        if head in self.visited:
            return self.visited[head]

        #create a Node or deep copy
        node=Node(head.val, None, None)

        #Add head key to the visited dictionary
        self.visited[head]=node

        #recursively populate next and random pointers

        node.left=self.copyRandom(head.next)
        node.random=self.copyRandom(head.random)

        return node
                
