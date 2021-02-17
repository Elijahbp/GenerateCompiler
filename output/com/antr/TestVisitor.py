# Generated from /Users/elijah/PycharmProjects/GenerateCompiler/Test.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TestParser import TestParser
else:
    from TestParser import TestParser

# This class defines a complete generic visitor for a parse tree produced by TestParser.

class TestVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TestParser#r.
    def visitR(self, ctx:TestParser.RContext):
        return self.visitChildren(ctx)



del TestParser