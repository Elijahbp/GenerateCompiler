import sys
from antlr4 import *

from output.com.antr.TestLexer import TestLexer
from output.com.antr.TestParser import TestParser

def create_generator(argv):
    input_stream = FileStream()
    lexer = TestLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TestParser(stream)
    tree = parser.startRule()
    walker = ParseTreeWalker()
    walker.walk()
    print('ok')


if __name__ == '__main__':
    create_generator(sys.argv)

