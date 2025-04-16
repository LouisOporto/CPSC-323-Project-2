# Create a parser given the alphabet
# {i, +, -, *, /, ), (} and ending with $

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

# Predictive Parsing Table
# States |  a  |  +  |  -  |  *  |  /  |  (  |  )  |  $  |
#   E    | TE' |     |     |     |     | TE' |     |     |
#   E'   |     | T+E'| T-E'|     |     |     |  ɛ  |  ɛ  |
#   T    | FT' |     |     |     |     | FT' |     |     |
#   T'   |     |  ɛ  |  ɛ  | F*T | F/T |     |  ɛ  |  ɛ  |
#   F    |  a  |     |     |     |     | (E) |     |     |

# Retrieve all the valid language alphabet (removing whitespace)
def tokenize(input_string: str) -> list:
    tokens = []
    current_number = ""
    for char in input_string:
        if char.isdigit() or char.isalpha():
            current_number += char
        elif current_number:
            tokens.append(current_number)
            current_number = ""
            if char in "+=*/()$":
                tokens.append(char)
        elif char in "+-*/()$":
            tokens.append(char)
    if current_number:
        tokens.append(current_number)
    return tokens

parser_table = { # Parsing Table and their expanded ACTIONS
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

    while (stack):
        # Start with the starting symbol in the stack until we reach $ or otherwise fail.
        top = stack.pop()
        current_token = tokens[index]
        
        if top == current_token == '$':
            # Completed parser and is valid
            break
        
        elif top in parser_table: # Non-terminal
            production = parser_table[top].get(current_token)
            if production is None:
                print(f"Syntax error at token '{current_token}', expected something for non-terminal '{top}'")
                break
            for symbol in reversed(production):
                if symbol != '':
                    stack.append(symbol)
        
        elif top == current_token: # Terminal match
            index += 1
        
        else:
            print(f"Syntax error: expected '{top}', got '{current_token}'")
            break

    if index == len(tokens) - 1: # Valid String
        print("Parsing Complete: Input passed!\n")
        return True
    else: # Invalid String
        print("Parsing Complete: Input failed!\n")
        return False

if __name__ == "__main__":
    print("Running LR parser\n")

    # Example 1
    string1 = "(a + a)*a$"
    print(f"Input string: \"{string1}\"")
    tokens1 = tokenize(string1)
    parser(tokens1, parser_table, 'E')

    # Example 2
    string2 = "a*(a/a)$"
    print(f"Input string: \"{string2}\"")
    tokens2 = tokenize(string2)
    parser(tokens2, parser_table, 'E')

    # Example 3
    string3 = "a (a + a) $"
    print(f"Input string: \"{string3}\"")
    tokens3 = tokenize(string3)
    parser(tokens3, parser_table, 'E')