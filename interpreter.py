#token types, eof marks that there is no input left for analysis
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'


class Token(object):
    #double __ means function cannot be imported from any module
    def __init__(self, type, value):
        #type: INTEGER, PLUS, EOF
        self.type = type
        #value: 1, 2,...,9, '+', None
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type = self.type,
            #repr() returns the assigned value between "", even if it's string
            value = repr(self.value)
            )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):

    def __init__(self, text):
        #client string input
        self.text = text
        #index into self.text
        self.pos = 0
        #current token instance
        self.current_token = None

    def error(self):
        #a general exception, not recommended
        raise Exception('Error parsing input')

    def get_next_token(self):
        #l€xical analyzer, breaks a sentence into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        #get a char at self.pos and decide what to create
        current_char = text[self.pos]

        #if char is a num, convert to int, create token , increment self.pos
        #and return token
        if current_char.isdigit():
            token  = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        else:
            self.error()

    def eat(self, token_type):
        #compare the token with its passed type and if mathc eat token
        #and assign next token to self.current_token, or raise exception
        if self.current_token.type == token.type:
            self.current_token = self.get_next_token()

        else:
            self.error()

    def expr(self):
        #expr -> INTEGER PLUS INTEGER
        #set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        #expecting current token to be single number
        left = self.current_token
        self.eat(INTEGER)

        #if the token is a '+'
        op = self.current_token
        self.eat(PLUS)

        #if token is an int again
        right = self.current_token
        self.eat(INTEGER)

        #now token is set to EOF
        #we can return the result
        result = left.value + right.value
        return result

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()