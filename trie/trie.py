

class TrieNode():
    def __init__(self,letter:str,children):
        self.letter = letter

        # dictionary with letter to node matching
        # null is None matched to None
        self.children = children

def dfs_print(first_node:TrieNode, pref):
    """A dfs traversal which returns all inserted words"""
    words = []
    if not first_node:
        return 
    
    def print_words(first_node: TrieNode = None,word = pref):
        if not first_node:
            return
        
        word += first_node.letter

        if None in first_node.children:
                if word:
                    words.append(word)

        
        
        for _,v in first_node.children.items():
            print_words(v, word)
            
    
    print_words(first_node=first_node,word="")

    return "\n".join(words)

class Trie(object):
    """A trie class for strings"""
    def __init__(self, trie_head = None):
        if trie_head:
            self.head = trie_head
        else:
            self.head = TrieNode("",{})
    
    def prefix_search(self,target_prefix:str):
        """Traverse tree until entire prefix is found. Return last node or None"""

        # keep original word
        word = target_prefix[:]
        curr = self.head

        # traverse trie to determine if
        # it contains the target prefix
        for letter in list(word):
            if letter in curr.children:
                curr = curr.children[letter]
                word = word[1:]
            else:
                # some letter wasn't found
                break
        
        # return node with last prefix letter
        if not word:
            return curr
        else:
            return None
    
    def autocomplete(self,target_prefix):
        curr = self.prefix_search(target_prefix)

        if curr:
            return dfs_print(curr,target_prefix)
        else:
            return ""


    
    def exists(self,target_word:str):
        """Search if target word exists in trie """
        node = self.prefix_search(target_word)
        if node:
            return None in node.children
        
        return False
    
    def remove(self,target_word:str):
        """Remove target word from trie"""

        # preserve original word
        word = target_word[:]
        curr = self.head

        # keep nodes of target word to check for removal
        prev_nodes = []

        #search for word
        for letter in list(word):
            if letter in curr.children:
                prev_nodes.append(curr)
                curr = curr.children[letter]
                word = word[1:]
        
        # word or prefix found
        if  curr and not word:
            # make sure word is removed
            del curr.children[None]

            # delete nodes which don't lead
            # to other words
            for node in prev_nodes[::-1]:
                if not node.children:
                    del node




    

    
    def insert(self,target:str):

        # preserve original word
        counter = 0
        curr = self.head

        # search for target word,
        # traversing trie until the
        # insertion point is found
        for letter in list(target):
            if letter in curr.children:
                curr = curr.children[letter]
                counter += 1
            else:
                break


        # whole prefix in trie,
        # make sure word is inserted
        if len(target) == counter:
            ### by adding a value with key None,
            ### the path from the root to the last
            ### node is considered an inserted word
            ### lack of None key signifies that
            ### the word hasn't been inserted
            curr.children[None] = True
        
        # add rest of letters
        for letter in list(target[counter:]):
            next_node = TrieNode(letter,{})
            curr.children[letter] = next_node
            curr = next_node
        # make sure word is inserted 
        curr.children[None] = None
    
    

    def __repr__(self,first_node: TrieNode = None,word = "") -> str:
        """A dfs traversal which returns all inserted words"""
        if not first_node:
            first_node = self.head

        return dfs_print(first_node,word)
        
        

            


a = Trie()
a.insert("abc")
a.insert("cbe")



