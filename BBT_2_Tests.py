import unittest, random, Balanced_Binary_Tree_2_1

def Create_Random_data(size=5):
    #Создание массива с данными 
    data_massive=[]
    for _ in range(0,size):
        data_massive.append(random.randint(100,200))
    return data_massive

Tree=Balanced_Binary_Tree_2_1.BalancedBST()
Tree.CreateFromArray(Create_Random_data())

class BBB_2_Tests(unittest.TestCase):

    def test_data_type(self):
        #Проверка типа данных BSTArray
        for j in range(0,len(Tree.BSTArray)):
            isinstance(Tree.BSTArray[j],int)
    
    def test_q_ty(self):
        #Проверка кол-ва элементов (для теста сбалансированности дерева)
        tree_data=Tree.GenerateTree()
        height_tree=Tree.height(Tree.Root)
        q_ty=0
        for level in range(0,height_tree):
            q_ty=q_ty+2**level
        self.assertEqual(len(tree_data),q_ty)

    def test_is_Balanced(self):
        # Тест на Сбалансированность
        # Подаем на вход другой тип данных 
        self.assertEqual(Tree.IsBalanced(random.randint(100,200)),False)
        # Подаем на вход элемент не содержащийся в дереве
        number_for_test=random.randint(500,1000)
        number_for_test_BSTNode=Balanced_Binary_Tree_2_1.BSTNode(number_for_test,None)
        self.assertEqual(Tree.IsBalanced(number_for_test_BSTNode),False)
        #Создаем дерево из 1 елемента и тестируем его
        massive_one=Create_Random_data(1)
        BT_one=Balanced_Binary_Tree_2_1.BalancedBST()
        BT_one.CreateFromArray(massive_one)
        BT_one.GenerateTree()
        self.assertEqual(BT_one.IsBalanced(BT_one.Root),True)
        #Создаем дерево на основе пустого массива
        massive_zero=Create_Random_data(0)
        BT_zero=Balanced_Binary_Tree_2_1.BalancedBST()
        BT_zero.CreateFromArray(massive_zero)
        BT_zero.GenerateTree()
        self.assertEqual(BT_zero.IsBalanced(BT_zero.Root),False)







if __name__ == '__main__':
    try:
        unittest.main()
    except: 
        SystemExit
    input()