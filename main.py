import sys
from antlr4 import *

from com.antlr.grammarBuchnevIlyaLexer import grammarBuchnevIlyaLexer
from com.antlr.grammarBuchnevIlyaParser import grammarBuchnevIlyaParser
from com.antlr.grammarBuchnevIlyaListener import grammarBuchnevIlyaListener

class MyKeyInput(grammarBuchnevIlyaListener):
    def enterProgram(self, ctx:grammarBuchnevIlyaParser.ProgramContext):
        print('Lolkekchebureck')


def create_generator(argv):
    input_stream = FileStream('test.txt')
    lexer = grammarBuchnevIlyaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammarBuchnevIlyaParser(stream)
    tree = parser.program()
    program =MyKeyInput()
    walker = ParseTreeWalker()
    walker.walk(program,tree)
    print('ok')


if __name__ == '__main__':
    create_generator(sys.argv)

