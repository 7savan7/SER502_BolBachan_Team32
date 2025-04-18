import ply.lex as lex

# List of token names includes:
# operators (arithmetic, relational, boolean, increment, logical),
# delimiters (parentheses, braces, semicolon), keywords (print, assign),
# and types (int, bool, string).

tokens = [
    'ID', 'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'GT', 'LT', 'EQ',
    'AND', 'OR',
    'INCR', 'DECR',
    'ASSIGN_OP', 'QMARK', 'COLON',
    'LPAREN', 'RPAREN', 'SEMI',
    'LBRACE', 'RBRACE',
    'PRINT', 'ASSIGN', 'TYPE', 'BOOL',
    'AGAR', 'TOH', 'NAHITOH', 'JABTAK', 'BAARBAAR'
]

# The dictionary maps the reserved Hindi words to their corresponding token names. 
reserved = {
    'rakho': 'ASSIGN',
    'bolBhai': 'PRINT',
    'agar': 'AGAR',
    'toh': 'TOH',
    'nahiToh': 'NAHITOH',
    'jabTak': 'JABTAK',
    'baarBaar': 'BAARBAAR',
    'int': 'TYPE',
    'bool': 'TYPE',
    'string': 'TYPE',
    'true': 'BOOL',
    'false': 'BOOL',
    'badaHai': 'GT',
    'chhotaHai': 'LT',
    'barabarHai': 'EQ',
    'jodo': 'PLUS',
    'ghatao': 'MINUS',
    'guna': 'TIMES',
    'bhaag': 'DIVIDE'
}

# Arithmetic operators , relational operators, boolean operators, increment/decrement operators
# and logical operators are defined using regex patterns. 
t_QMARK   = r'\?'
t_COLON   = r':'
t_AND     = r'&'
t_OR      = r'\|'
t_INCR    = r'\+\+'
t_DECR    = r'\-\-'
t_ASSIGN_OP = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMI    = r';'
t_LBRACE  = r'\{' 
t_RBRACE  = r'\}'

# STRING rule:
# Matches double-quoted strings, excluding newlines.
# The value is stored without the enclosing quotes.
def t_STRING(t):
    r'"[^"\n]*"'
    t.value = t.value[1:-1]  
    return t

# NUMBER rule: 
# Matches integers.
# The value is converted to an integer. 
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# ID rule:
# Matches identifiers.
# If the identifier is a reserved word, it is assigned the corresponding token type.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Whitespace and newline handler:
# Ignores whitespace characters (spaces, tabs, carriage returns).
t_ignore = ' \t\r'

# Increments the line number for each newline character.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handler:
# Prints an error message for illegal characters and skips them.
def t_error(t):
    print(f"Illegal character: '{t.value[0]}'")
    t.lexer.skip(1)

# Lexer builder
lexer = lex.lex()