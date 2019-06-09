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
        for everydigit in range(0,len(a)):
            if a[everydigit]==None:
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
            self.BSTArray.clear()
            for every_node in array_for_sort:
                self.BSTArray.append(every_node.NodeKey)
        return node

			
    def GenerateTree(self):
	# создаём дерево с нуля из массива BSTArray
        if len(self.BSTArray)==0:
            return False
        levels=1
        j=0
        tree_array=[]
        for i in range(0,len(self.BSTArray)):
            node=BSTNode(self.BSTArray[i],None)
            tree_array.append(node)
        while j<len(self.BSTArray):
            if j==0:
                tree_array[j].Parent=None
                if len(self.BSTArray)>2*j+1:
                    tree_array[j].LeftChild=tree_array[2*j+1]
                else:
                    tree_array[j].LeftChild=None
                if len(self.BSTArray)>2*j+2:
                    tree_array[j].RightChild=tree_array[2*j+2]
                else:
                    tree_array[j].RightChild=None
            elif 2*j+1<len(self.BSTArray) and j!=0:
                tree_array[2*j+1].Parent=tree_array[j]
                tree_array[j].LeftChild=tree_array[2*j+1]
                tree_array[2*j+1].Parent=tree_array[j]
                if 2*j+2<len(self.BSTArray):
                    tree_array[2*j+2].Parent=tree_array[j]
                    tree_array[j].RightChild=tree_array[2*j+2]
                    tree_array[2*j+2].Parent=tree_array[j]
                else:
                    tree_array[j].RightChild=None
            else: 
                tree_array[j].LeftChild=None
            j+=1
        level_q_ty=1
        l=0
        while l<len(tree_array):
            if l==0:
                start=0
                finish=0
                tree_array[l].Level=levels
                l+=1
            else:
                start=finish+1
                level_q_ty=2*level_q_ty
                finish=start+level_q_ty-1
                if finish>len(tree_array):
                    finish=len(tree_array)
                levels+=1
                for number in range(start,finish+1):
                    tree_array[number].Level=levels
                    l+=1
                   #print(tree_array[number].NodeKey,levels)
        self.Root=tree_array[0]
        return tree_array


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
        if isinstance(root_node,BSTNode)==True:
            pass
        else:
            return False
        in_tree=False
        for every_node_Key in range(0,len(self.BSTArray)):
            if self.BSTArray[every_node_Key]==root_node.NodeKey:
                in_tree=True
                break
            else:
                in_tree=False
        if in_tree==False:
            return False
        if root_node!=None:
            if root_node.LeftChild==None and root_node.RightChild==None:
                return True
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
            else:
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
a=[50,25,75,20,37,62,84,19,21,31,43,55,70,80,92]
b=[2,4,56]
BT=BalancedBST()
BT.CreateFromArray(a)
print(BT.BSTArray)
BT.GenerateTree()
print(BT.IsBalanced(BT.Root))
"""
