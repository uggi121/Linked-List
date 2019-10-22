# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:44:07 2019

@author: Sudharshan
"""


class ListNode:
    """
    Represents the node of a linked-list.
    
    Contains a single value along with a reference to the next node.
    """
    
    def __init__(self, data, next_node=None):
        """
        Constructs a list node.
        
        Accepts a data value and a reference to the next node as inputs.
        
        Parameters:
            data: Value to be stored in the node.
            next_node (ListNode): Reference to the next node.
        """
        
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
        L (ListNode): The list node where the linear search commences.
        key: The value to search for.
        
    Returns:
        bool: True if 'key' is found, False otherwise.
    """
    
    while L != None and L.data != key:
        L = L.next
    return L

  
def insert_after(node, new_node):
    """
    Inserts a new given list node 'new_node' after the current given
    list node 'node'.
    
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
    """
    Represents a linked list.
    
    Consists of head and tail list nodes, which are the first and last nodes
    respectively.
    """
    
    def __init__(self):
        """Constructs an empty linked list."""
        
        self.head = None
        self.tail = None
        self.num_nodes = 0
        
    def get_head(self):
        """Returns the head (first node) of the linked list."""
        
        return self.head
    
    def get_tail(self):
        """Returns the tail (last node) of the linked list."""
        
        return self.tail
    
    def is_empty(self):
        """
        Checks if the list is empty.
        
        Returns True if the list is empty.
        
        Returns:
            bool: True if the list is empty.
        """
        
        return self.num_nodes == 0
    
    def size(self):
        """Returns the size of the linked-list."""
        
        return self.num_nodes
    
    def add(self, item):
        """
        Adds an item to the linked list.
        
        Parameters:
            item: The item to be added.
        """
        
        node = ListNode(item)
        if not self.head:
            self.head, self.tail = node, node
        else:
            self.tail.next = node
            self.tail = self.tail.next
            
        # Increment list size.
        self.num_nodes += 1
    
    def search(self, item):
        """
        Searches for an item in the linked list.
        
        Returns True if the item is found.
        
        Parameters:
            item: Item to be searched for.
            
        Returns:
            bool: True if the item is found.
        """
        
        return search_list(self.head, item)
    
    def delete(self, item):
        """
        Deletes the first occurrence of the given item.
        
        Parameters:
            item: The item to delete.
        
        Returns:
            bool: True if the deletion is successful.
        
        Raises:
            ValueError: If the list is empty.
        """
            
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
        """
        Returns a string representation of the linked list.
        
        Returns:
            str: String representation of the list.
        """
        
        ptr, res = self.head, []
        while ptr:
            res.append(ptr.data)
            ptr = ptr.next
        return str(res)
            
            
    
    