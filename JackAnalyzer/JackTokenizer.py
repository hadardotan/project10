import os
from xml.sax.saxutils import escape
#
# handles the compiler's input:
# allows:
#     ignoring white space
#     advancing the input, one token at a time
#     getting the value and type of the current token


class JackTokenizer(object):

    def __init__(self, input_file):
        """
        Opens the input file/stream and gets ready
        to tokenize it.
        :param input_file
        """
        file = open(input_file,'r')
        self.token_type = -1
        self.current_value = 0;


    def has_more_tokens(self):
        """
        checks if we have more tokens in the input
        :return: boolean
        """

    def advance(self):
        """
        Gets the next token from the input and
        makes it the current token. This method
        should only be called if hasMoreTokens()
        is true. Initially there is no current token.

        :return:
        """

    def token_type(self):
        """
        :return: the type of the current token (KEYWORD, SYMBOL,
        IDENTIFIER,INT_CONST,STRING_CONST)

        """

    def keyword(self):
        """
        :return:the keyword which is the current token:
        """

    def symbol(self):
        """
         Should be called only when tokenType() is SYMBOL.
        :return: the character which is the current token
        """

    def identifier(self):
        """
        Should be called only when tokenType() is IDENTIFIER
        :return: the identifier which is the current token
        """

    def int_val(self):
        """
        Should be called only when tokenType() is INT_CONST

        :return: the integer value of the current
        token.
        """

    def string_val(self):
        """
        Should be called only when tokenType() is STRING_CONST.
        :return:  the string value of the current token, without the double
         quotes
        """

