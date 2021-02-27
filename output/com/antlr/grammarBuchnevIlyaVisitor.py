# Generated from /Users/elijah/PycharmProjects/GenerateCompiler/grammarBuchnevIlya.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .grammarBuchnevIlyaParser import grammarBuchnevIlyaParser
else:
    from grammarBuchnevIlyaParser import grammarBuchnevIlyaParser

# This class defines a complete generic visitor for a parse tree produced by grammarBuchnevIlyaParser.

class grammarBuchnevIlyaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by grammarBuchnevIlyaParser#numbers.
    def visitNumbers(self, ctx:grammarBuchnevIlyaParser.NumbersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#real.
    def visitReal(self, ctx:grammarBuchnevIlyaParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#order.
    def visitOrder(self, ctx:grammarBuchnevIlyaParser.OrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#expression.
    def visitExpression(self, ctx:grammarBuchnevIlyaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#operand.
    def visitOperand(self, ctx:grammarBuchnevIlyaParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#summand.
    def visitSummand(self, ctx:grammarBuchnevIlyaParser.SummandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#multiplier.
    def visitMultiplier(self, ctx:grammarBuchnevIlyaParser.MultiplierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#program.
    def visitProgram(self, ctx:grammarBuchnevIlyaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#description.
    def visitDescription(self, ctx:grammarBuchnevIlyaParser.DescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#operator.
    def visitOperator(self, ctx:grammarBuchnevIlyaParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#composite.
    def visitComposite(self, ctx:grammarBuchnevIlyaParser.CompositeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#assignments.
    def visitAssignments(self, ctx:grammarBuchnevIlyaParser.AssignmentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#conditional.
    def visitConditional(self, ctx:grammarBuchnevIlyaParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#fixed_cycle.
    def visitFixed_cycle(self, ctx:grammarBuchnevIlyaParser.Fixed_cycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#conditional_loop.
    def visitConditional_loop(self, ctx:grammarBuchnevIlyaParser.Conditional_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#input_m.
    def visitInput_m(self, ctx:grammarBuchnevIlyaParser.Input_mContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#output_m.
    def visitOutput_m(self, ctx:grammarBuchnevIlyaParser.Output_mContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by grammarBuchnevIlyaParser#multistr_comment.
    def visitMultistr_comment(self, ctx:grammarBuchnevIlyaParser.Multistr_commentContext):
        return self.visitChildren(ctx)



del grammarBuchnevIlyaParser