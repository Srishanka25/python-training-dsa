class BST:
    def __init__(self,key):
        self.key = key
        self.l_child=None
        self.r_child=None
    def insert_node(self,data):
        if self.key is None:
            print("empty")
            return
        if self.key == data:
            print("data elements is already present")
            return
        if self.key > data:
            if self.l_child:
                self.l_child.insert_node(data)
            else:
                self.l_child=BST(data)
        else:
            if  self.r_child:
                self.r_child.insert_node(data)
            else:
                self.r_child=BST(data)
    def pre_order(self):
        print(self.key,end=" ")
        if self.l_child:
            self.l_child.pre_order()
        if self.r_child:
            self.r_child.pre_order()
    def In_order(self):
        if self.l_child:
            self.l_child.In_order()
        print(self.key,end=" ")
        if self.r_child:
            self.r_child.In_order()
    def post_order(self):
        if self.l_child:
            self.l_child.post_order()
        if self.r_child:
            self.r_child.post_order()
        print(self.key,end=" ")
    def delete(self,data):
        if self.key is None:
            print("cannot delete from an empty tree")
        else:
            if data < self.key:
                if self.l_child:
                    self.l_child=self.l_child.delete(data)
                else:
                    print("the given node (data)is not present")
            elif data > self.key:
                if self.r_child:
                    self.r_child=self.r_child.delete(data)
                else:
                    print("the given node (data)is not present")
            else:
                if self.l_child in None:
                    temp=self.r_child
                    self=None
                    return temp
                if self.r_child in None:
                    temp=self.r_child
                    self=None
                    return temp
                n = self.r_child
                while n.l_child:
                    n=n.l_child
                self.key=n.key
                self.r_child=self.r_child.delete(n.l_child)
                
                
                
root=BST(45)
root.insert_node(30)
root.delete(7)

print(root)
root.insert_node(50)
lst=[1,2,4,5,7,4,8,3,4,5]
root1=BST(5)
for i in lst:
    root1.insert_node(i)
root1.pre_order()
root1.In_order()
root1.post_order()
print()
root1.delete(7)







                
                
                
            
            
            
        