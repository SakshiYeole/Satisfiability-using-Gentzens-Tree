import copy
import os
import sys


from model import StringConstants 

class Node:
    def __init__(self, LHS, RHS) -> None:
        self.LHS = copy.deepcopy(LHS)
        self.RHS = copy.deepcopy(RHS)
        self.left_Child = None
        self.right_child = None

    def set_left_child(self, left_child):
        self.left_Child = left_child

    def set_right_child(self, right_child):
        self.right_child = right_child

    def get_new_nodes(self):
        pass

    def is_leaf_node(self):
        for left in self.LHS:
            if len(left) > 1:
                return False
            
        for right in self.RHS:
            if len(right) > 1:
                return False
        
        return True

    def is_contradiction(self):
        if self.is_leaf_node():
            for left in self.LHS:
                if left in self.RHS:
                    return True
        return False
    
    def __str__(self):
        return f"{self.LHS} -> {self.RHS}"
    
    # Testing

def main():
    left_list1 = []
    left_list1.append("Alice")
    left_list2 = []
    # left_list2.append("skdf")
    left_list2.append("Bob")
    right_list1 = []
    right_list2 = []
    right_list2.append("alice")
    right_list1.append("Bob")

    right = []
    left = []

    right.append(right_list1)
    right.append(right_list2)
    left.append(left_list1)
    left.append(left_list2)

    node = Node(left, right)
    print(node)
    print(node.is_leaf_node())
    print(node.is_contradiction())



if __name__ == "__main__":
    main()
    
    