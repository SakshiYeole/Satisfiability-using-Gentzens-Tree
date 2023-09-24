
class Brackets:
    round_opening = "("
    round_closing = ")"
    square_opening = "["
    sqaure_closing = "]"
    curly_opening = "{"
    curly_closing = "}"

    @staticmethod
    def is_opening_bracket(s):
        brackets_list = [Brackets.round_opening, Brackets.square_opening, Brackets.curly_opening]
        return s in brackets_list
    
    @staticmethod
    def corresponding_closing_bracket(bracket):
        if bracket == Brackets.round_opening:
            return Brackets.round_closing
        elif bracket == Brackets.curly_opening:
            return Brackets.curly_closing
        elif bracket == Brackets.square_opening:
            return Brackets.sqaure_closing
        return None