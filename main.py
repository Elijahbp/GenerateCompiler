import sys
from antlr4 import *

from MyListner import MyGrammarListner
from com.antlr.grammarBuchnevIlyaLexer import grammarBuchnevIlyaLexer
from com.antlr.grammarBuchnevIlyaParser import grammarBuchnevIlyaParser
from com.antlr.grammarBuchnevIlyaListener import grammarBuchnevIlyaListener

def create_generator(argv):
    lexer = grammarBuchnevIlyaLexer(FileStream('test.txt'))
    stream = CommonTokenStream(lexer)
    parser = grammarBuchnevIlyaParser(stream)
    tree = parser.program()
    program = MyGrammarListner()
    walker = ParseTreeWalker()
    walker.walk(program,tree)

if __name__ == '__main__':
    create_generator(sys.argv)