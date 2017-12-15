import os, re
from xml.sax.saxutils import escape
from JackAnalyzer.JackGrammar import *


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
        self.input_file = open(input_file,'r')
        self.file_lines = input_file.read() # reads entire contents of the file
        self.tokens_to_process = self.tokenize_file(self.file_lines)
        self.current_token_type = NO_TOKEN
        self.current_value = NO_PHRASE
        self.output_file = self.output_file # TODO : Change!!!!

    def has_more_tokens(self):
        """
        checks if we have more tokens in the input
        :return: boolean
        """
        return self.tokens_to_process != []

    def advance(self):
        """
        Gets the next token from the input and
        makes it the current token. This method
        should only be called if hasMoreTokens()
        is true. Initially there is no current token.

        :return: xml line <token_type> token </token_type>
        """
        if self.has_more_tokens():
            self.current_value, self.current_token_type =\
                self.tokens_to_process.pop(0)
        else:
            self.current_value, self.current_token_type = NO_TOKEN, NO_PHRASE
        self.generate_xml()

    def token_type(self):
        """
        :return: the type of the current token (KEYWORD, SYMBOL,
        IDENTIFIER,INT_CONST,STRING_CONST)
        """
        return self.token_type

    def phrase_value(self):
        """

        :return: phrase value
        """
        return self.current_value

    def start_tag(self, type):
        self.output_file.write('<'+tokens_types[type]+'>')

    def end_tag(self, type):
        self.output_file.write('</'+tokens_types[type]+'>')

    def generate_xml(self):
        """

        :return:
        """
        val = self.phrase_value()
        type = self.token_type()
        self.start_tag(type)
        if type == KEYWORD:
            self.output_file.write(self.keyword())
        elif type == SYMBOL:
            self.output_file.write(self.symbol())
        elif type == IDENTIFIER:
            self.output_file.write(self.identifier())
        elif type == INT_CONST:
            self.output_file.write(self.int_val())
        elif type == STRING_CONS:
            self.output_file.write(self.string_val())
        elif type == NO_TOKEN:
            self.output_file.write("error! no token recognized")
        self.end_tag(type)

    def keyword(self):
        """
        :return:the keyword which is the current token:
        """
        return self.current_value


    def symbol(self):
        """
         Should be called only when tokenType() is SYMBOL.
        :return: the character which is the current token
        """
        return escape(self.current_value)

    def identifier(self):
        """
        Should be called only when tokenType() is IDENTIFIER
        :return: the identifier which is the current token
        """
        return self.current_value

    def int_val(self):
        """
        Should be called only when tokenType() is INT_CONST

        :return: the integer value of the current
        token.
        """
        return self.current_value

    def string_val(self):
        """
        Should be called only when tokenType() is STRING_CONST.
        :return:  the string value of the current token, without the double
         quotes
        """
        return self.current_value

    def tokenize_file(self,file):
        """
        group the characters of a line into tokens as defined by Jack language
        syntax
        :param file:
        :return: tokenized_lines
        """
        lines = self.remove_comments(file).split(" ")
        tokenized_lines = []
        for phrase in lines:
            tokenized_lines += self.phrase_to_token(phrase)
        return tokenized_lines

    def remove_comments(self,file):
        """
        removes comment from file and replace it with one white space
        creates 2 groups of regex:
        first group captures quoted strings (double or single)
        second group captures comments (//single-line or /* multi-line */ or
        /** multi-line */)
        :return:
        """

        regex = re.compile(comment_pattern, re.MULTILINE | re.DOTALL)

        def _replacer(match):
            # if the 2nd group (capturing comments) is not None,
            # it means we have captured a non-quoted (real) comment string.
            if match.group(2) is not None:
                return " "  # so we will return space and remove the comment
            else:  # otherwise, we will return the 1st group
                return match.group(1)
        return regex.sub(_replacer, file)

    def phrase_to_token(self, phrase):
        """

        :param phrase
        sets token type according to phrase.
        if phrase is an string removes ""

        """
        val = phrase
        type = NO_TOKEN
        if self.is_keyword(phrase):
            type = KEYWORD
        elif self.is_identifier(phrase):
            type = IDENTIFIER
        elif self.is_symbol(phrase):
            type = SYMBOL
        elif self.is_int(phrase):
            type = INT_CONST
        elif self.is_string(phrase):
            type = STRING_CONS
            val = val[1:-2] # remove "" from string
        else:
            type = NO_TOKEN
        return val, type

    def is_keyword(self, phrase):
        """
        :return: boolean
        """
        return phrase in keywords

    def is_symbol(self, phrase):
        """

        :param phrase:
        :return: boolean
        """
        return phrase in symbols

    def is_identifier(self, phrase):
        """

        :param phrase:
        :return:
        """
        return re.match(id_re, phrase)

    def is_int(self, phrase):
        """

        :param phrase:
        :return:
        """
        return re.match(int_re, phrase)

    def is_string(self, phrase):
        """

        :param phrase:
        :return:
        """
        return re.match(str_re, phrase)
