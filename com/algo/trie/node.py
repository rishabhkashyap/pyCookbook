
class Node:

    def __init__(self,label):
        self.label=label
        self.is_word=False
        self.children=dict()



    def add(self,node):
        if(isinstance(node,Node)):
            self.children[node.label]=node


    def get_neighbour(self,label):
        neighbour=None
        if(isinstance(label,str)):
            neighbour=self.children.get(label)
        return neighbour

    def set_is_word(self,is_word):
        if(isinstance(is_word,bool)):
            self.is_word-is_word














