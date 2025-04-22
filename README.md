## Setup
To run the parser:
1. Clone or download this repository.
`https://github.com/LouisOporto/CPSC-323-Project-2.git`

3. Make sure you have Python 3 installed.
4. Navigate to the project directory.
5. Run the program using:
```bash
python main.py
```
## Code Explanation 

### Overview
The objective of this project is to implement a predictive parser (LL(1)) using a context-free 
grammar (CFG) and an associated parsing table. The parser reads an input string composed of the 
alphabet { i, +, -, *, /, ), ( } and ending with $. It checks whether the string conforms to 
the grammar using a stack-based parsing method. Unlike traditional compiler generators like 
Yacc or Bison, this parser is manually implemented in Python, providing a clear understanding of 
parsing techniques and grammar handling.

#### Tokenization
Serves as a lexical preprocessor to convert a raw input string into a list of valid tokens. 
It isolates multi-character identifiers like 'aa', handles arithmetic operators and parentheses, and strips out unnecessary whitespace.
```python
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
```
#### Parsing Table 
The CFG is encoded using a parsing table implemented as a dictionary. 
Each non-terminal key (e.g., 'E', 'T', etc.) and the value is another dictionary that maps input tokens to production rules. 
For the non-terminal E, if the next input token is 'a' or '(', the rule E → TE' is applied. 
E' handles operators after an expression. If + or - appears, it extends the expression. 
If the input is ) or $, it goes to epsilon (i.e., empty), meaning no more expansion is needed. 
T → FT': A term consists of a factor followed by more potential terms. This production applies when the token is 'a' or '('. T' handles multiplication/division that might follow a factor. 
If it sees +, -, etc., it goes epsilon, meaning the term ends. Lastly, F → a or F → (E): A factor is either a variable (a) or a parenthesized expression.
```python
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
```
#### Predictive Parser 
Defines the parser function, which takes a list of tokens, the parser table, and a starting symbol, in this case E. The stack is initialized. '$' marks the 
bottom, and the start symbol is placed on top to begin parsing. 'index' is used to track our position in the tokens list. While the stack is not empty, begin 
parsing. If both stack and input are at the end symbol $, parsing is complete and successful. If the top of the stack is a non-terminal, look up the production rule based on the current input token.
A syntax error is thrown if there is no matching rule. Production rule symbols are pushed onto the stack reversed to expand left to right. If the top of the stack matches the current token, move forward to the next token.
A syntax error is thrown if there's a mismatch between expected terminal and input token. If all tokens were consumed and $ was reached, the input is valid. Otherwise, it failed.


```python
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
```
### Data Structures Used
- Dictionary - Stores the grammar rules in a way the parser can easily access using the non-terminal and the current input token.
```python
parser_table = {
    'E': {'a': ['T', "E'"], '(': ['T', "E'"]},
    ...
}
```
- List - Simulate the call stack of the recursive parsing process
```python
stack = ['$', 'E']
```
## Dependencies and Version Used
Python 3

## Contributors
Louis Oporto  
Tommy Wijaya  
Chanel McGee

## License 
The MIT License (MIT)

