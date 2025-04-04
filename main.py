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
# E -> TQ
# Q -> +TQ
# Q -> -TQ
# Q -> ɛ
# T -> FR
# R -> *FR
# R -> /FR
# R -> ɛ
# F -> (E)
# F -> a

# First and Follow Table
# ELEMENT | FIRST | FOLLOW
#   E     |(, a   | $, )
#   Q     |+, -, ɛ| $, )
#   T     |(, a   | +, -, ), $
#   R     |/, *, ɛ| +, -, ), $
#   F     |(, a   | $

# Input Examples: (remove whitespace)
# "(a+a)*a$"
# "a*(a/a)$"
# "a(a+a)$"

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