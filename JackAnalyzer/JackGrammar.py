
# The Jack language includes five types of terminal elements (tokens):
# KEYWORD, SYMBOL, IDENTIFIER,INT_CONST,STRING_CONS



# tokens CONSTANTS
KEYWORD = 1
SYMBOL = 2
IDENTIFIER = 3
INT_CONST = 4
STRING_CONS = 5
NO_TOKEN = -1
NO_PHRASE = -1

# KEYWORD tokens
K_CLASS = 'class'
K_CONSTRUCTOR = 'constructor'
K_FUNCTION = 'function'
K_METHOD = 'method'
K_FIELD = 'field'
K_STATIC = 'static'
K_VAR = 'var'
K_INT = 'int'
K_BOOLEAN = 'boolean'
K_CHAR = 'char'
K_VOID = 'void'
K_LET = 'let'
K_DO = 'do'
K_IF = 'if'
K_ELSE = 'else'
K_WHILE = 'while'
K_RETURN = 'return'
K_TRUE = 'true'
K_FALSE = 'false'
K_NULL = 'null'
K_THIS = 'this'
K_NONE = ''

keywords = [K_CLASS ,K_CONSTRUCTOR ,K_FUNCTION ,K_METHOD ,K_FIELD ,K_STATIC
,K_VAR ,K_INT ,K_BOOLEAN ,K_CHAR ,K_VOID ,K_LET ,K_DO ,K_IF ,K_ELSE ,K_WHILE
,K_RETURN , K_TRUE ,K_FALSE ,K_NULL ,K_THIS ,K_NONE ]

# SYMBOL tokens
symbols = ['{' , '}' , '(' , ')' , '[' , ']' , '. ' , ', ' , '; ' , '+' , '-' ,
          '*' , '/' , '&' , ',' , '<' , '>' , '=' , '~']


# tokens type
tokens_types = ['keyword', 'symbol', 'integerConstant', 'stringConstant',
                'identifier']

# regex for int and string
int_re = r'\d+'
str_re = r'"[^"\n]*"'

# identifier regex - A sequence of letters, digits, and underscore
#  ( '_' ) not starting with a digit
id_re = r'[^\d][\w\-]+'


# comment patterns regex
comment_pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)|" \
          r"(/\**.*?\*/|//[^\r\n]*$)"

