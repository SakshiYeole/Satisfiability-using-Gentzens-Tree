import os
import sys

path = os.getcwd() + '\model'
sys.path.append(path)
from model import GentzensTree
from model import StringConstants

def read_input_from_file(path):
        try: 
            with open(path, 'r', encoding='utf-8') as file:
                input_list = file.readline().split()
                input = [s for s in input_list if s]
                if input:
                    return input
                else:
                    return []
        except FileNotFoundError:
            print(f"File {path} not found.")
            return None
        except Exception as e:
            print(f"an error occurred: {e}")
            return None

def print_available_operators():
    print("Available operators are: ")
    print(f"Conjunction: {StringConstants.StringOperators.conjunction}")
    print(f"Disjunction: {StringConstants.StringOperators.disjunction}")
    print(f"Implication: {StringConstants.StringOperators.implication}")
    print(f"Double-Implication: {StringConstants.StringOperators.double_implication}")
    print(f"Negation: {StringConstants.StringOperators.negation}")

    # print("NOTE: Kindly use the above operators only")

def main():
    print_available_operators()
    input_file_path = os.path.join(os.getcwd(), "..", "Input", "InputExpression.txt")
    input = read_input_from_file(input_file_path)

    print("Input Expression: \n")
    print(input)
    gentzen_tree = GentzensTree.GentzensTree(input)

    print("Applying Gentzens Proof Tree Rules: ")
    gentzen_tree.algorithm_for_gentzen_system_creating_tree()
    gentzen_tree.print_tree()

    print(f"COntradiction at leaf Node(IF ANY): {gentzen_tree.check_contradiction()}")
    if gentzen_tree.check_contradiction():
        gentzen_tree.print_contradicting_node()
        print()
        print("The input expression is SATISFIABLE")
    else:
        print("The input expression is NOT SATISFIABLE")
        print()
    
if __name__ == "__main__":
    main()
    