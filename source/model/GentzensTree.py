from collections import deque
import Node
import StringConstants
class GentzensTree:
    def __init__(self, expression):
        LHS = []
        RHS = []
        RHS.append(expression)

        self.root_node = Node.Node(LHS, RHS)
        self.root_node.strip_left_and_right_handside()
        self.leaf_nodes = []

    def algorithm_for_gentzen_system_creating_tree(self):
        unserved_nodes = deque()
        unserved_nodes.append(self.root_node)

        while unserved_nodes:
            curr_node = unserved_nodes.popleft()

            new_nodes_for_curr = curr_node.get_new_nodes()
            assert len(new_nodes_for_curr) <= 2

            if len(new_nodes_for_curr) == 0 :
                self.leaf_nodes.append(curr_node)
            elif len(new_nodes_for_curr) == 1:
                curr_node.set_left_child(new_nodes_for_curr[0])
            elif len(new_nodes_for_curr) == 2:
                curr_node.set_left_child(new_nodes_for_curr[0])
                curr_node.set_right_child(new_nodes_for_curr[1])

            unserved_nodes.extend(new_nodes_for_curr)

    def print_tree(self):
        print("Level Order Traversal of the Gentzen's Proof Tree: ")
        q = deque()
        q.append(self.root_node)

        while q:
            curr = q.popleft()
            print(curr)
            print()

            if curr.get_left_child() is not None:
                q.append(curr.get_left_child())
            
            if curr.get_right_child() is not None:
                q.append(curr.get_right_child())

    def contradicting_node(self):
        for node in self.leaf_nodes:
            if node.is_contradiction():
                return node        
        return None
    
    def print_contradicting_node(self):
        print(f"Node with contradiction: {self.contradicting_node()}")

    def check_contradiction(self):
        return self.contradicting_node() is not None
    
    def check_satisfiability(self):
        return self.check_contradiction is not None
    
def main():
    list = []
    list.append("(")
    list.append("A")
    list.append(StringConstants.StringOperators.conjunction)
    list.append("(")
    list.append("A")
    list.append(StringConstants.StringOperators.implication)
    list.append("B")
    list.append(")")
    list.append(")")
    list.append(StringConstants.StringOperators.implication)
    list.append("B")

    g = GentzensTree(list)
    g.algorithm_for_gentzen_system_creating_tree()
    print(g.check_satisfiability)

    g.print_tree()

if __name__ == "__main__":
    main()

        