class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def maxSubsetXOR(self, arr, N):
        root = TrieNode()
        max_xor = float('-inf')
        
        # Function to insert a number into the Trie
        def insert(num):
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        # Function to find the maximum XOR for a given number
        def find_max_xor(num):
            node = root
            xor_num = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                # Try to maximize the XOR by choosing the opposite bit
                opposite_bit = 1 - bit
                if opposite_bit in node.children:
                    xor_num |= (1 << i)
                    node = node.children[opposite_bit]
                else:
                    node = node.children[bit]
            return xor_num
        
        # Insert the first number into the Trie
        insert(arr[0])
        max_xor = arr[0]
        
        for i in range(1, N):
            # Find the maximum XOR for the current number and update max_xor
            max_xor = max(max_xor, find_max_xor(arr[i]))
            # Insert the current number into the Trie
            insert(arr[i])
        
        # Convert the result to an integer to remove leading zeros
        return int(max_xor)

