"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # what is already given to us... the original list.... 
        # work backwards....
        # iterate through the original list through head...
        if not head: return None
        ptr = head
        hashmap = {}


        #put into hashmap...
        while ptr:
            node = Node(x = ptr.val)
            hashmap[ptr] = node
            ptr = ptr.next
        
        ptr = head
        while ptr:
            new_node = hashmap[ptr]
            new_node.next = hashmap[ptr.next] if ptr.next else None
            new_node.random = hashmap[ptr.random] if ptr.random else None
            new_node = new_node.next 
            ptr = ptr.next
        return hashmap[head]


        
