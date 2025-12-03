# Generated from Algoritmia.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AlgoritmiaParser import AlgoritmiaParser
else:
    from AlgoritmiaParser import AlgoritmiaParser

# This class defines a complete listener for a parse tree produced by AlgoritmiaParser.
class AlgoritmiaListener(ParseTreeListener):

    # Enter a parse tree produced by AlgoritmiaParser#root.
    def enterRoot(self, ctx:AlgoritmiaParser.RootContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#root.
    def exitRoot(self, ctx:AlgoritmiaParser.RootContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#procedure.
    def enterProcedure(self, ctx:AlgoritmiaParser.ProcedureContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#procedure.
    def exitProcedure(self, ctx:AlgoritmiaParser.ProcedureContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#params.
    def enterParams(self, ctx:AlgoritmiaParser.ParamsContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#params.
    def exitParams(self, ctx:AlgoritmiaParser.ParamsContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#block.
    def enterBlock(self, ctx:AlgoritmiaParser.BlockContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#block.
    def exitBlock(self, ctx:AlgoritmiaParser.BlockContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#statement.
    def enterStatement(self, ctx:AlgoritmiaParser.StatementContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#statement.
    def exitStatement(self, ctx:AlgoritmiaParser.StatementContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#assignment.
    def enterAssignment(self, ctx:AlgoritmiaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#assignment.
    def exitAssignment(self, ctx:AlgoritmiaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#read.
    def enterRead(self, ctx:AlgoritmiaParser.ReadContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#read.
    def exitRead(self, ctx:AlgoritmiaParser.ReadContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#write.
    def enterWrite(self, ctx:AlgoritmiaParser.WriteContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#write.
    def exitWrite(self, ctx:AlgoritmiaParser.WriteContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#writeParam.
    def enterWriteParam(self, ctx:AlgoritmiaParser.WriteParamContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#writeParam.
    def exitWriteParam(self, ctx:AlgoritmiaParser.WriteParamContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#play.
    def enterPlay(self, ctx:AlgoritmiaParser.PlayContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#play.
    def exitPlay(self, ctx:AlgoritmiaParser.PlayContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#conditional.
    def enterConditional(self, ctx:AlgoritmiaParser.ConditionalContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#conditional.
    def exitConditional(self, ctx:AlgoritmiaParser.ConditionalContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#iteration.
    def enterIteration(self, ctx:AlgoritmiaParser.IterationContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#iteration.
    def exitIteration(self, ctx:AlgoritmiaParser.IterationContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#procCall.
    def enterProcCall(self, ctx:AlgoritmiaParser.ProcCallContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#procCall.
    def exitProcCall(self, ctx:AlgoritmiaParser.ProcCallContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#listAppend.
    def enterListAppend(self, ctx:AlgoritmiaParser.ListAppendContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#listAppend.
    def exitListAppend(self, ctx:AlgoritmiaParser.ListAppendContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#listCut.
    def enterListCut(self, ctx:AlgoritmiaParser.ListCutContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#listCut.
    def exitListCut(self, ctx:AlgoritmiaParser.ListCutContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#ListSize.
    def enterListSize(self, ctx:AlgoritmiaParser.ListSizeContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#ListSize.
    def exitListSize(self, ctx:AlgoritmiaParser.ListSizeContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#Parenthesis.
    def enterParenthesis(self, ctx:AlgoritmiaParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#Parenthesis.
    def exitParenthesis(self, ctx:AlgoritmiaParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#ListLiteral.
    def enterListLiteral(self, ctx:AlgoritmiaParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#ListLiteral.
    def exitListLiteral(self, ctx:AlgoritmiaParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#MulDivMod.
    def enterMulDivMod(self, ctx:AlgoritmiaParser.MulDivModContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#MulDivMod.
    def exitMulDivMod(self, ctx:AlgoritmiaParser.MulDivModContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#Variable.
    def enterVariable(self, ctx:AlgoritmiaParser.VariableContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#Variable.
    def exitVariable(self, ctx:AlgoritmiaParser.VariableContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#Number.
    def enterNumber(self, ctx:AlgoritmiaParser.NumberContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#Number.
    def exitNumber(self, ctx:AlgoritmiaParser.NumberContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#AddSub.
    def enterAddSub(self, ctx:AlgoritmiaParser.AddSubContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#AddSub.
    def exitAddSub(self, ctx:AlgoritmiaParser.AddSubContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#ListAccess.
    def enterListAccess(self, ctx:AlgoritmiaParser.ListAccessContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#ListAccess.
    def exitListAccess(self, ctx:AlgoritmiaParser.ListAccessContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#Note.
    def enterNote(self, ctx:AlgoritmiaParser.NoteContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#Note.
    def exitNote(self, ctx:AlgoritmiaParser.NoteContext):
        pass


    # Enter a parse tree produced by AlgoritmiaParser#Relational.
    def enterRelational(self, ctx:AlgoritmiaParser.RelationalContext):
        pass

    # Exit a parse tree produced by AlgoritmiaParser#Relational.
    def exitRelational(self, ctx:AlgoritmiaParser.RelationalContext):
        pass



del AlgoritmiaParser