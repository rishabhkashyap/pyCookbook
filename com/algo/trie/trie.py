from com.algo.trie.node import Node


class Trie:
    def __init__(self):
        self.root = Node('')

    def add_word(self, word):

        if (word is not None and isinstance(word, str)):
            current_node = self.root
            for char in word:
                node = current_node.get_neighbour(char)
                if (node is not None):
                    current_node = node
                else:
                    new_node = Node(char)
                    current_node.add(new_node)
                    current_node = new_node
            current_node.is_word = True



    def search_word(self, word):
        if (word is not None and isinstance(word, str)):
            current_node = self.root
            word_available = False
            for char in word:
                node = current_node.get_neighbour(char)
                if (node is not None  and node.label==char):
                    current_node = node

                else:
                    current_node=node
                    break

            if(current_node is not None and current_node.is_word):
                word_available=True


        return word_available


if __name__=='__main__':
     trie=Trie()
     trie.add_word('geek')
     trie.add_word('geekforgeeks')
     trie.add_word('geeky')
     trie.add_word('geektrust')
     trie.add_word('apple')

     found=trie.search_word('geektrust')
     print('geektrust found = {}'.format(found))