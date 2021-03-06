class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:

    def __init__(self):
        self.Root = None
        self.BSTArray=[]

    def CreateFromArray(self, a ,len_a=0):
	# создаём массив дерева BSTArray из заданного  массива a
        # шаг 0 сортируем исходный массив по возрастанию
        if not a:
            return None
        if self.BSTArray==[]:
            a=self.Sort_initial_data(a)
            len_a=len(a)
        #шаг 1 определяем элементы дерева 
        middle=int((len(a))/2)
        node=BSTNode(a[middle],None)
        self.BSTArray.append(node)
        node.LeftChild=self.CreateFromArray(a[:middle])
        node.RightChild=self.CreateFromArray(a[middle+1:])
        if len(self.BSTArray)==len_a:
            index=0
            index_max=0
            q=0
            while index_max<len_a:
                index_max=index_max+2**(q)
                q+=1
            array_for_sort=[]
            children=[]
            parents=[]
            parents.append(self.BSTArray[index])
            array_for_sort.append(self.BSTArray[index])
            while index+1<index_max:
                for every_parent in parents:
                    if every_parent.NodeKey!=None:
                        if every_parent.LeftChild!=None:
                            array_for_sort.append(every_parent.LeftChild)
                            children.append(every_parent.LeftChild)
                        else:
                            every_parent.LeftChild=BSTNode(None,None)
                            array_for_sort.append(every_parent.LeftChild)
                            children.append(every_parent.LeftChild)
                        if every_parent.RightChild!=None:
                            array_for_sort.append(every_parent.RightChild)
                            children.append(every_parent.RightChild)
                        else:
                            every_parent.RightChild=BSTNode(None,None)
                            array_for_sort.append(every_parent.RightChild)
                            children.append(every_parent.RightChild)
                        index+=2
                parents.clear()
                for j in range(0,len(children)):
                    parents.append(children[j])
                children.clear()
            self.BSTArray=array_for_sort
        return node

			
    def GenerateTree(self):
	# создаём дерево с нуля из массива BSTArray
        if self.BSTArray==None:
            return False
        TreeNode=self.BSTArray[0]
        levels=0
        if TreeNode!=None:
            parents=[]
            children=[]
            output=[]
            TreeNode.Parent=None
            TreeNode.Level=levels+1
            output.append(TreeNode)
            parents.append(TreeNode)
            while parents!=[]:
                levels+=1
                for everynode in parents:
                        if everynode.LeftChild!=None:
                            everynode.LeftChild.Parent=everynode
                            everynode.LeftChild.Level=levels+1
                            output.append(everynode.LeftChild)
                            children.append(everynode.LeftChild)
                        else:
                            output.append(None)
                            children.append(None)
                        if everynode.RightChild!=None:
                            everynode.RightChild.Parent=everynode
                            everynode.RightChild.Level=levels+1
                            output.append(everynode.RightChild)
                            children.append(everynode.RightChild)
                        else:
                            output.append(None)
                            children.append(None)
                parents.clear()
                for everynode in children:
                    if everynode!=None:
                        parents.append(everynode)
                    else:
                        pass
                children.clear()
            q_ty=0
            for j in range(0,levels):
                q_ty=q_ty+2**j
            output=output[:q_ty]
            self.Root=self.BSTArray[0]
            return output

    def Sort_initial_data(self,a):
    #Сортировка исходного массива
        length=len(a)
        for i in range(0,length):
            for j in range(i,length):
                if a[i]>a[j]:
                    a[i],a[j]=a[j],a[i]
                else:
                    pass
        return a

    def IsBalanced(self, root_node):
        if root_node!=None:
            #Блок проверки больше, меньше значение NodeKey
            if root_node.LeftChild.NodeKey!=None:
                if root_node.NodeKey>root_node.LeftChild.NodeKey:
                    Left=True
                else:
                    Left=False
            elif root_node.LeftChild.NodeKey==None:
                Left=True
            else:
                pass
            if root_node.RightChild.NodeKey!=None:
                if root_node.RightChild.NodeKey>root_node.NodeKey:
                    Right=True
                else:
                    Right=False
            elif root_node.RightChild.NodeKey==None:
                Right=True
            if Right!=True and Left!=True:
                return False
            height_res=self.heightBalanced(root_node)
            return height_res
            
    
    def height(self,root_node):
        # Определяет глубину дерева
        if root_node is None:
            return 0
        if root_node is False:
            return 0
        return max(self.height(root_node.LeftChild),self.height(root_node.RightChild))+1 


    def heightBalanced(self, root_node):
        # Проверка на сбалансированность дерева по высоте
        if root_node==None:
            return True
        if root_node.LeftChild!=False: 
            left_Sub_Tree=self.height(root_node.LeftChild)
        else:
            return True
        if root_node.RightChild!=False:
            right_Sub_Tree=self.height(root_node.RightChild)
        else:
            return True
        if (abs(left_Sub_Tree-right_Sub_Tree)<=1) and self.heightBalanced(root_node.LeftChild) is True and self.heightBalanced(root_node.RightChild) is True: 
            return True
        else:
            return False
"""
a=[2,4,6,7,8,9,0,10,16,567]
BT=BalancedBST()
BT.CreateFromArray(a)
print(BT.BSTArray)
print(BT.GenerateTree())
print(BT.Root.NodeKey)
print(BT.IsBalanced(BT.Root))
for i in range(0,len(BT.BSTArray)):
    print(BT.BSTArray[i].NodeKey)
"""