def preorder(root):
    arr=[]
    if root:
        arr.append(root.data)
        arr+=preorder(root.left)
        arr+=preorder(root.right)
    return arr
   
    # code here

def postOrder(root):
    # code here
    arr=[]
    if root:
        arr+=postOrder(root.left)
        arr+=postOrder(root.right)
        arr.append(root.data)
    return arr
class Solution:
    def InOrder(self,root):
        # code here
        arr=[]
        if root:
            arr+=self.InOrder(root.left)
            arr.append(root.data)
            arr+=self.InOrder(root.right)
        return arr
