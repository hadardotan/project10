import os, re, glob
from xml.sax.saxutils import escape
from JackAnalyzer.JackGrammar import *


# handles the compiler's input:
# allows:
#     ignoring white space
#     advancing the input, one token at a time
#     getting the value and type of the current token

class JackTokenizer(object):

    def __init__(self, input_file, output_file):
        """
        Opens the input file/stream and gets ready
        to tokenize it.
        :param input_file
        """
        self.input_file = input_file #already open!!
        self.code = self.file_to_str()
        self.output_file = output_file
        self.tokens_to_process = self.tokenize_file(self.code)
        self.current_token_type = NO_TOKEN
        self.current_value = NO_PHRASE



    def file_to_str(self):
        """

        :return:
        """
        code = ""
        for line in self.input_file:
            code+=line
        return code

    def has_more_tokens(self):
        """
        checks if we have more tokens in the input
        :return: boolean
        """
        return self.tokens_to_process != []

    def get_next(self):
        """

        :return: value and type of next token
        """
        next_token = self.tokens_to_process[0]
        next_value, next_type = self.phrase_to_token(next_token)
        return next_value, next_type




    def advance(self):
        """
        Gets the next token from the input and
        makes it the current token. This method
        should only be called if hasMoreTokens()
        is true. Initially there is no current token.

        :return: xml line <token_type> token </token_type>
        """

        if self.has_more_tokens():
            current_token = self.tokens_to_process.pop(0)
            self.current_value, self.current_token_type =\
                self.phrase_to_token(current_token)
            print(self.current_value,   self.current_token_type)
        else:
            self.current_value, self.current_token_type = NO_TOKEN, NO_PHRASE


    def token_type(self):
        """
        :return: the type of the current token (KEYWORD, SYMBOL,
        IDENTIFIER,INT_CONST,STRING_CONST)
        """
        return self.current_token_type

    def phrase_value(self):
        """

        :return: phrase value
        """
        return self.current_value

    def start_tag(self, val):
        self.output_file.write('<'+val+'>')
        print(self.output_file)

    def end_tag(self, val):
        self.output_file.write('</'+val+'>')

    def generate_xml(self):
        """

        :return:
        """
        val = self.phrase_value()
        type = self.token_type()
        self.start_tag(tokens_types[type])
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
        self.end_tag(tokens_types[type])

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
        self.remove_comments()
        # find strings

        tokenized_lines = re.split(STRING_RE, self.code)
        print(tokenized_lines)
        #split symbols
        new_tokenized = []
        for part in tokenized_lines:
            if not re.match(RE_STRING_COMPILED,part.strip()):
                print(part)
                part = re.split(SYMBOLS_RE, part)
                new_tokenized+= part
            else:
                new_tokenized += [part]
        tokenized_lines = new_tokenized

        i=0
        while i < len(tokenized_lines):
            if QUOTATION_MARK in tokenized_lines[i]: #case token is a string
                tokenized_lines[i] = [tokenized_lines[i].strip()]
            else:
                tokenized_lines[i] = tokenized_lines[i].strip()
                tokenized_lines[i] = tokenized_lines[i].split(' ')
            i+=1

        tokenized_lines = [item for sublist in tokenized_lines for
                           item in sublist]
        tokenized_lines = [string for string in tokenized_lines
                           if len(string) > 0] #remove empty strings

        print(tokenized_lines)
        return tokenized_lines

    # def split_strings(self):
    #     """
    #
    #     :return:
    #     """
    #     num_of_strings, i = 0, 0
    #     search_string = self.code
    #     start = True
    #
    #     while start == True:
    #         start = search_string.find("\"")
    #         print(search_string)
    #         search_string = search_string[start + 1:]
    #         end = search_string.find("\"")
    #         search_string = search_string[end + 1:]
    #         num_of_strings += 1
    #         print(search_string)
    #     #split by quotation marks
    #     tokenized_lines = self.code.split('"')
    #     while i < num_of_strings:
    #         tokenized_lines[i] = tokenized_lines[i].split(' ')
    #         i += 1
    #     tokenized_lines[i] = ["\""+tokenized_lines[i]+"\""]
    #     tokenized_lines[i+1] = tokenized_lines[i+1].split(' ')
    #     tokenized_lines = [item for sublist in tokenized_lines for
    #                        item in sublist]
    #     return tokenized_lines

    def remove_comments (self):
        """

        :return:
        """
        remove = True
        while (remove):
            # newline_re = RE_NEWLINE_COMPILED.match(self.code)
            comment1_re = RE_COMMENT1_COMPILED.match(self.code)
            comment2_re = RE_COMMENT2_COMPILED.match(self.code)
            remove = False
            # if newline_re:
            #     self.update_code_by_match(RE_NEWLINE_COMPILED)
            #     remove = True
            if comment1_re:
                self.update_code_by_match(RE_COMMENT1_COMPILED)
                remove = True
            elif comment2_re:
                self.update_code_by_match(RE_COMMENT2_COMPILED)
                remove = True


    def update_code_by_match(self, match):
        """
        updates the code according to regex match
        :return:
        """
        current_code = self.code
        current_code = re.sub(match,"",current_code)
        self.code = " ".join(current_code.split())



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
        elif self.is_string(phrase):
            type = STRING_CONS
            val = val[1:-2] # remove "" from string
        elif self.is_identifier(phrase):
            type = IDENTIFIER
        elif self.is_symbol(phrase):
            type = SYMBOL
        elif self.is_int(phrase):
            type = INT_CONST
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
        return re.match(RE_ID_COMPILED, phrase)

    def is_int(self, phrase):
        """

        :param phrase:
        :return:
        """
        return re.match(RE_INT_COMPILED, phrase)

    def is_string(self, phrase):
        """

        :param phrase:
        :return:
        """
        return re.match(RE_STR_COMPILED, phrase)

