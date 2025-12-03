# Generated from Algoritmia.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AlgoritmiaParser import AlgoritmiaParser
else:
    from AlgoritmiaParser import AlgoritmiaParser

# This class defines a complete generic visitor for a parse tree produced by AlgoritmiaParser.

class AlgoritmiaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgoritmiaParser#root.
    def visitRoot(self, ctx:AlgoritmiaParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#procedure.
    def visitProcedure(self, ctx:AlgoritmiaParser.ProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#params.
    def visitParams(self, ctx:AlgoritmiaParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#block.
    def visitBlock(self, ctx:AlgoritmiaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#statement.
    def visitStatement(self, ctx:AlgoritmiaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#assignment.
    def visitAssignment(self, ctx:AlgoritmiaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#read.
    def visitRead(self, ctx:AlgoritmiaParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#write.
    def visitWrite(self, ctx:AlgoritmiaParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#writeParam.
    def visitWriteParam(self, ctx:AlgoritmiaParser.WriteParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#play.
    def visitPlay(self, ctx:AlgoritmiaParser.PlayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#conditional.
    def visitConditional(self, ctx:AlgoritmiaParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#iteration.
    def visitIteration(self, ctx:AlgoritmiaParser.IterationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#procCall.
    def visitProcCall(self, ctx:AlgoritmiaParser.ProcCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#listAppend.
    def visitListAppend(self, ctx:AlgoritmiaParser.ListAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#listCut.
    def visitListCut(self, ctx:AlgoritmiaParser.ListCutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#ListSize.
    def visitListSize(self, ctx:AlgoritmiaParser.ListSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Parenthesis.
    def visitParenthesis(self, ctx:AlgoritmiaParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#ListLiteral.
    def visitListLiteral(self, ctx:AlgoritmiaParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#MulDivMod.
    def visitMulDivMod(self, ctx:AlgoritmiaParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Variable.
    def visitVariable(self, ctx:AlgoritmiaParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Number.
    def visitNumber(self, ctx:AlgoritmiaParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#AddSub.
    def visitAddSub(self, ctx:AlgoritmiaParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#ListAccess.
    def visitListAccess(self, ctx:AlgoritmiaParser.ListAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Note.
    def visitNote(self, ctx:AlgoritmiaParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#Relational.
    def visitRelational(self, ctx:AlgoritmiaParser.RelationalContext):
        return self.visitChildren(ctx)



del AlgoritmiaParser