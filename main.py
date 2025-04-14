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

# Predictive Parsing Table
# States |  a  |  +  |  -  |  *  |  /  |  (  |  )  |  $  |
#   E    | TE' |     |     |     |     | TE' |     |     |
#   E'   |     | T+E'| T-E'|     |     |     |  ɛ  |  ɛ  |
#   T    | FT' |     |     |     |     | FT' |     |     |
#   T'   |     |  ɛ  |  ɛ  | F*T | F/T |     |  ɛ  |  ɛ  |
#   F    |  a  |     |     |     |     | (E) |     |     |

# Input Examples: (remove whitespace)
# "(a+a)*a$"
# "a*(a/a)$"
# "a(a+a)$"

# Currently used below     
def tokenize(input_string: str) -> list:
    tokens = []
    current_number = ""
    for char in input_string:
        if char.isdigit() or char.isalpha():
            current_number += char
        elif current_number:
            tokens.append(current_number)
            current_number = ""
            if char in "+=*/()":
                tokens.append(char)
        elif char in "+-*/()":
            tokens.append(char)
    if current_number:
        tokens.append(current_number)
    return tokens

parser_table = {
    'E': {
        'a': ['T', 'E\''],
        '(': ['T', 'E\'']
    },
    'E\'': {
        '+': ['+', 'T', 'E\''],
        '-': ['-', 'T', 'E\''],
        ')': [], # epsilon
        '$': [], # epsilon
    },
    'T': {
        'a': ['F', 'T\''],
        '(': ['F', 'T\''],
    },
    'T\'': {
        '*': ['*', 'F', 'T\''],
        '/': ['/', 'F', 'T\''],
        '+': [], # epsilon
        '-': [], # epsilon
        ')': [], # epsilon
        '$': [], # epsilon
    },
    'F': {
        'a': ['a'],
        '(': ['(', 'E', ')'],
    }
}

def parser(tokens, parser_table, start_symbol):
    stack = ['$', start_symbol]
    index = 0

    print(tokens)

    while (stack):
        top = stack.pop()
        current_token = tokens[index]
        # TODO Complete rest of parser #


    # END TODO #
    if index == len(tokens):
        print("Parsing Complete: Input passed!\n")
        return True
    else:
        print("Parsing Complete: Input failed!\n")
        return False

if __name__ == "__main__":
    print("Running LR parser\n")

    string1 = "(a + a)*a$"
    print(f"Input string: \"{string1}\"")
    tokens1 = tokenize(string1)
    parser(tokens1, parser_table, 'E')

    string2 = "a*(a/a)$"
    print(f"Input string: \"{string2}\"")
    tokens2 = tokenize(string2)
    parser(tokens2, parser_table, 'E')

    string3 = "a (a + a) $"
    print(f"Input string: \"{string3}\"")
    tokens3 = tokenize(string3)
    parser(tokens3, parser_table, 'E')