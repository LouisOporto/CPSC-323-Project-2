# Create a parser given the alphabet
# {i, +, -, *, /, ), (} and ending with $
# Given a CFG and parsing table
# CFG
# E -> E + T
# E -> E - T
# E -> T
# T -> T * F
# T -> T / F
# T -> F
# F -> (E)
# F -> a

# First and Follow Table
# ELEMENT | FIRST | FOLLOW
#   E     |(, a   | $, )
#   Q     |+, -, ɛ| $, )
#   T     |(, a   | +, -, ), $
#   R     |/, *, ɛ| +, -, ), $
#   F     |(, a   | $

if __name__ == "__main__":
    print("Running LR parser\n")