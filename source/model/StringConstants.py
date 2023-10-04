
class StringOperators:    
    disjunction = '\u22C1'
    conjunction = '\u22C0'
    implication = '\u2192'
    double_implication = '\u2194'
    negation  = '\u223c'
    arrow = '\u21D2'

    @staticmethod
    def is_operator(str_value):
        operators = [StringOperators.implication, StringOperators.double_implication, StringOperators.disjunction, StringOperators.conjunction, StringOperators.negation]
        return str_value in operators
    
    @staticmethod
    def reverse_precedence_of_operators(operator):
        precedence = { 
            StringOperators.negation: 1,
            StringOperators.disjunction: 2,
            StringOperators.conjunction: 3,
            StringOperators.implication: 4,
            StringOperators.double_implication: 5 
        }
        return precedence.get(operator, -1)

# print(StringOperators.disjunction)
# print(StringOperators.conjunction)
# print(StringOperators.implication)
# print(StringOperators.double_implication)
# print(StringOperators.negation)