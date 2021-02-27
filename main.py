import sys
from antlr4 import *

from com.antlr.grammarBuchnevIlyaLexer import grammarBuchnevIlyaLexer
from com.antlr.grammarBuchnevIlyaParser import grammarBuchnevIlyaParser

def create_generator(argv):
    input_stream = FileStream('test.txt')
    lexer = grammarBuchnevIlyaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammarBuchnevIlyaParser(stream)
    tree = parser.program()
    print('ok')


if __name__ == '__main__':
    create_generator(sys.argv)

