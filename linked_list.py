# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:49:05 2019

@author: Sudharshan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:44:07 2019

@author: Sudharshan
"""

"""
Represents the node of a linked-list.

Contains a single value along with a reference to the next node.
"""
class ListNode:
    """
    Constructs a ListNode.
    
    Accepts a data value and a reference to the next node as inputs.
    
    Parameters:
        data: Value to be stored in the node.
        next_node (ListNode): Reference to the next node.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
    
    def __unicode__(self):
        return "[" + str(self.data) + "]"
    
    def __str__(self):
        return self.__unicode__()
    
    def __repr__(self):
        return self.__unicode__()

# Helper functions to process linked-lists.

def search_list(L, key):
    """
    Searches a sequence of list-nodes for the presence of the given key.
    
    Parameters:
        L (ListNode): The ListNode where the linear search commences.
        key: The value to search for.
        
    Returns:
        bool: True if 'key' is found, False otherwise.
    """
    while L != None and L.data != key:
        L = L.next
    return L

  
def insert_after(node, new_node):
    """
    Inserts a new given ListNode 'new_node' after the current given
    ListNode 'node'.
    
    Parameters:
        node (ListNode): The node after which a new node is to be inserted.
        new_node (ListNode): The node to be inserted.
    """
    assert node, "The node preceding the inserted node cannot be empty."
    assert new_node, "The node to be inserted cannot be empty."
    new_node.next = node.next
    node.next = new_node
    
def delete_after(node):
    """
    Deletes the ListNode following 'node'.
    
    Parameters:
        node (ListNode): ListNode whose successor is to be deleted.
    """
    assert node, "Node cannot be empty."
    if node.next:
        node.next = node.next.next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0
        
    def get_head(self):
        return self.head
    
    def get_tail(self):
        return self.tail
    
    def is_empty(self):
        return self.num_nodes == 0
    
    def size(self):
        return self.num_nodes
    
    def add(self, item):
        node = ListNode(item)
        if not self.head:
            self.head, self.tail = node, node
        else:
            self.tail.next = node
            self.tail = self.tail.next
            
        # Increment list size.
        self.num_nodes += 1
    
    def search(self, item):
        return search_list(self.head, item)
    
    def delete(self, item):
        if not self.head:
            raise ValueError("Cannot delete from empty list.")
        if self.head.data == item:
            if self.head is self.tail:
                self.tail = None
                
            self.head = self.head.next
            # Decrement list size.
            self.num_nodes -= 1
            return True
        ptr = self.head
        while ptr.next and ptr.next.data != item:
            ptr = ptr.next
        
        if ptr.next:
            if self.tail is ptr.next:
                self.tail = ptr
            delete_after(ptr)
            self.num_nodes -= 1
            return True
        return False
    
    def __str__(self):
        return str(self.head) if self.head else "Empty List"
    
    def __unicode__(self):
        return self.__str__()
    
    def __repr__(self):
        return self.__str__()
    
    def stringify(self):
        ptr, res = self.head, []
        while ptr:
            res.append(ptr.data)
            ptr = ptr.next
        return str(res)
            
            
    
    