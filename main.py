# Create a parser given the alphabet
# {i, +, -, *, /, ), (} and ending with $

# Given a CFG and parsing table
# CFG (original)
# E -> E + T
# E -> E - T
# E -> T
# T -> T * F
# T -> T / F
# T -> F
# F -> (E)
# F -> a

# Left-recursion rules elimination
# E -> TE'
# E' -> T + E'
# E' -> T - E'
# E' -> ɛ

# T -> FT'
# T' -> F * T'
# T' -> F / T'
# T' -> ɛ

# F -> (E)
# F -> a

# First and Follow Table
# ELEMENT  |  FIRST  | FOLLOW
#    E     | (, a    | $, )
#    E'    | +, -, ɛ | $, ) 
#    T     | (, a    | +, -, ), $
#    T'    | /, *, ɛ | +, -, ), $
#    F     | (, a    | $

# Input Examples: (remove whitespace)
# "(a+a)*a$"
# "a*(a/a)$"
# "a(a+a)$"

# Invalid method need to change this but an idea
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0 
    
    def _get_next_token(self):
        if self.current_token_index < len(self.tokens)
            return self.tokens[self.current_token_index]
        return None
    
    def _consume_token(self):
        self.current_token_index += 1

    def parse(self):
        return self.parse_expression()
    
    def parse_expression(self):
        left_term = self.parse_term()
        while self._get_next_token in "+-":
            op = self._get_next_token()
            self._consume_token()
            right_term = self.prase_term()
            left_term = self.self.evaluate(left_term, op, right_term)
        return left_term
    
    def parse_term(self):
        token = self._get_next_token()
        self._consume_token()
        return int(token)
    
    def evaluate(self, left, op, right):
        if op == "+":
            return left + right
        if op == "-":
            return left - right
        if op == "*":
            return left * right
        if op == "/":
            return left * right
        
def tokenize(input_string: str) -> list:
    tokens = []
    current_number = ""
    for char in input_string:
        if char.isdigit() or char.isalpha():
            current_number += char
        elif current_number:
            tokens.append(("NUMBER", current_number))
            current_number = ""
            if char in "+=*/()":
                tokens.append((char, char))
        elif char in "+-*/()":
            tokens.append((char, char))
    if current_number:
        tokens.append(("NUMBER", current_number))
    return tokens

def parser(input_string):
    print(input_string)


if __name__ == "__main__":
    print("Running LR parser\n")

    string1 = "(a + a)*a$"
    string2 = "a*(a/a)$"
    string3 = "a (a + a) $"
    print(f"Input string: \"{string1}\"")
    tokens1 = tokenize(string1)
    parser(tokens1)

    print(f"Input string: \"{string2}\"")
    tokens2 = tokenize(string2)
    parser(tokens2)

    print(f"Input string: \"{string3}\"")
    tokens3 = tokenize(string3)
    parser(tokens3)