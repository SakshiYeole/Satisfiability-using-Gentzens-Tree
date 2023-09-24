import copy
import os
import sys
# from typing import List

from model import StringConstants
from model import Brackets

class Node:
    def __init__(self, LHS, RHS) -> None:
        self.LHS = []
        for left in LHS:
            if left is None or not left:
                continue
            else:
                self.LHS.append(left)
        
        self.RHS = []
        for right in RHS:
            if right is None or not right:
                continue
            else:
                self.RHS.append(right)

        self.left_child = None
        self.right_child = None

    def set_left_child(self, left_child):
        self.left_child = left_child

    def set_right_child(self, right_child):
        self.right_child = right_child

    def get_left_child(self):
        return self.left_child
    
    def get_right_child(self):
        return self.right_child
    
    def strip_left_and_right_handside(self):
        self.strip_for_list_of_list(self.LHS)
        self.strip_for_list_of_list(self.RHS)

    def strip_for_list_of_list(self, list):
        for formula in list:
            initial_value_bracket = Brackets.Brackets.is_opening_bracket(formula[0])
            while initial_value_bracket:
                initial_symbol= formula[0]
                corresponding_closing_symbol = Brackets.Brackets.corresponding_closing_bracket(initial_symbol)
                cnt = 1

                need_to_remove = False
                for i in range(1, len(formula)):
                    curr_symbol = formula[i]
                    if curr_symbol == initial_symbol:
                        cnt += 1
                    elif curr_symbol == corresponding_closing_symbol:
                        cnt -= 1

                    if cnt == 0:
                        if  i== (len(formula) - 1):
                            need_to_remove = True
                        break
                if need_to_remove:
                    formula.remove(0)
                    formula.remove(len(formula)-1)
                else:
                    break

                initial_value_bracket = Brackets.Brackets.is_opening_bracket(formula[0])

    def break_a_formula_into_two_parts_given_index(self, formula, index):
        before_index = formula[:index]
        after_index = formula[index + 1:]
        result = [before_index, after_index]
        return result
    
    # returns the index at which splitting needs to be done
    def splitting_character_index(self, formula):
        stack = []
        result = -1
        for i, symbol in enumerate(symbol):
            # check if symbol is an operator
            if StringConstants.StringOperators.is_operator(symbol):
                while stack and (StringConstants.StringOperators.precedence_of_operators(symbol) <= StringConstants.StringOperators.precedence_of_operators(formula[stack[-1]])):
                    result = stack[-1]
                    stack.pop()
                stack.append(i)
            elif symbol =="(":
                stack.append(i)
            elif symbol == ")":
                while stack and formula[stack[-1]] != "(":
                    result = stack[-1]
                    stack.pop()
                stack.pop()

        if stack:
            result = stack[-1]
        stack.clear()

        return result

    def deep_copy_list_of_list(self, input_list):
        result = []
        for formula in input_list:
            result.append(list(formula))
        return result
    
    def break_node_for_left_side(self, left, index):
        broken_formula = self.break_a_formula_into_two_parts_given_index(left, index)
        symbol_on_which_splitting = left[index]

        if symbol_on_which_splitting == StringConstants.StringOperators.implication:
            # create two nodes, A->B => delta
            #       lambda, B => delta
            #       lambda  => A, delta

            new_lhs_first = self.deep_copy_list_of_list(self.LHS)
            new_lhs_first.remove(left)
            new_lhs_first.append(broken_formula[1])

            new_rhs_first = self.deep_copy_list_of_list(self.RHS)
            first_node = Node(new_lhs_first, new_rhs_first)

            new_lhs_second = self.deep_copy_list_of_list(self.LHS)
            new_lhs_second.remove(left)

            new_rhs_second = self.deep_copy_list_of_list(self.RHS)
            new_rhs_second.append(broken_formula[0])
            second_node = Node(new_lhs_second, new_rhs_second)

            node_list = [first_node, second_node]

            return node_list   
        
        elif symbol_on_which_splitting == StringConstants.StringOperators.conjunction:
            # create one other node, lambda, A and B => delta
            #                          lambda, A, B => delta

            new_lhs = self.deep_copy_list_of_list(self.LHS)
            new_lhs.remove(left)
            new_lhs.append(broken_formula[0])
            new_lhs.append(broken_formula[1])

            new_rhs = self.deep_copy_list_of_list(self.RHS)

            new_node = Node(new_lhs, new_rhs)
            node_list = [new_node]

            return node_list
        
        elif symbol_on_which_splitting == StringConstants.StringOperators.disjunction:
            # create two different nodes, lambda, A or B => delta
            #                           lambda, A => delta
            #                           lambda, B => delta

            new_lhs_first = self.deep_copy_list_of_list(self.LHS)
            new_lhs_first.remove(left)
            new_lhs_first.append(broken_formula[0])

            new_rhs_first = self.deep_copy_list_of_list(self.RHS)
            first_node = Node(new_lhs_first, new_rhs_first)

            new_lhs_second = self.deep_copy_list_of_list(self.LHS)
            new_lhs_second.remove(left)
            new_lhs_second.append(broken_formula[1])

            new_rhs_second = self.deep_copy_list_of_list(self.RHS)
            second_node = Node(new_lhs_second, new_rhs_second)

            node_list = [first_node, second_node]

            return node_list  
        
        elif symbol_on_which_splitting == StringConstants.StringOperators.negation:
            # create one other node, lambda, not A => delta
            #                       lambda => A, delta

            assert not broken_formula[0]
            new_lhs = self.deep_copy_list_of_list(self.LHS)
            new_lhs.remove(left)

            new_rhs = self.deep_copy_list_of_list(self.RHS)
            new_rhs.append(broken_formula[1])

            new_node = Node(new_lhs, new_rhs)
            node_list = [new_node]

            return node_list
        
        else:
            return None
        
    def break_node_for_right_side(self, right, index):
        broken_formula = self.break_a_formula_into_two_parts_given_index(right, index)
        symbol_on_which_splitting = right[index]

        if symbol_on_which_splitting == StringConstants.StringOperators.implication:
            # create one different node, lambda => A->B, delta
            #                           lambda, A => B, delta

            new_lhs = self.deep_copy_list_of_list(self.LHS)
            new_lhs.append(broken_formula[0])

            new_rhs = self.deep_copy_list_of_list(self.RHS)
            new_rhs.remove(right)
            new_rhs.append(broken_formula[1])

            new_node = Node(new_lhs, new_rhs)
            node_list = [new_node]

            return node_list
        
        elif symbol_on_which_splitting == StringConstants.StringOperators.conjunction:
            # create two different nodes, lamba => A and B, delta
            #                           lambda => A, delta
            #                           lambda => B, delta

            new_lhs_first = self.deep_copy_list_of_list(self.LHS)
            
            new_rhs_first = self.deep_copy_list_of_list(self.RHS)
            new_rhs_first.remove(right)
            new_rhs_first.append(broken_formula[0])

            first_node = Node(new_lhs_first, new_rhs_first)

            new_lhs_second = self.deep_copy_list_of_list(self.LHS)

            new_rhs_second = self.deep_copy_list_of_list(self.RHS)
            new_rhs_second.remove(right)
            new_rhs_second.append(broken_formula[1])

            second_node = Node(new_lhs_second, new_rhs_second)
            node_list = [first_node, second_node]

            return node_list
        
        elif symbol_on_which_splitting == StringConstants.StringOperators.disjunction:
            # create one different node, lambda => A or B, delta
            #                            lamba => A, B, delta

            new_lhs = self.deep_copy_list_of_list(self.LHS)

            new_rhs = self.deep_copy_list_of_list(self.RHS)
            new_rhs.remove(right)
            new_rhs.append(broken_formula[0])
            new_rhs.append(broken_formula[1])

            new_node = Node(new_lhs, new_rhs)
            node_list = [new_node]

            return node_list

        elif symbol_on_which_splitting == StringConstants.StringOperators.negation:
            # create a different node, lambda => not A, delta
            #                           lambda, A => delta

            assert not broken_formula[0]

            new_lhs = self.deep_copy_list_of_list(self.LHS)
            new_lhs.append(broken_formula[1])

            new_rhs = self.deep_copy_list_of_list(self.RHS)
            new_rhs.remove(right)

            new_node = Node(new_lhs, new_rhs)
            node_list = [new_node]

            return node_list
        
        else:
            return None
        
    def get_new_nodes(self):
        # loop on left
        for left in self.LHS:
            index_of_splitting = self.splitting_character_index(left)

            if index_of_splitting < 0:
                # no splitting
                continue

            result = self.break_node_for_left_side(left, index_of_splitting)

            assert result is not None

            for node in result:
                node.strip_left_and_right_handside()
            return result
        
        # loop on right
        for right in self.RHS:
            index_of_splitting = self.splitting_character_index(right)

            if index_of_splitting < 0:
                # no splitting
                continue

            result = self.break_node_for_left_side(right, index_of_splitting)

            assert result is not None

            for node in result:
                node.strip_left_and_right_handside()
            return result
        
        # returns empty list
        return []

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
    
    