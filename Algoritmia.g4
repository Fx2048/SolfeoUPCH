grammar Algoritmia;

// Regla principal
root : procedure+ EOF ;

// Procedimientos
procedure : ID params? block ;
params : ID+ ;
block : '|:' statement* ':|' ;

// Instrucciones
statement
    : assignment
    | read
    | write
    | play
    | conditional
    | iteration
    | procCall
    | listAppend
    | listCut
    ;

// Asignación
assignment : ID '<-' expr ;

// Lectura
read : '<?>' ID ;

// Escritura
write : '<w>' writeParam+ ;
writeParam : expr | STRING ;

// Reproducción
play : '(:)' expr ;

// Condicional
conditional : 'if' expr block ('else' block)? ;

// Iteración
iteration : 'while' expr block ;

// Llamada a procedimiento
procCall : ID expr* ;

// Añadir a lista
listAppend : ID '<<' expr ;

// Cortar de lista
listCut : '8<' ID '[' expr ']' ;

// Expresiones
expr
    : expr op=('*'|'/'|'%') expr       # MulDivMod
    | expr op=('+'|'-') expr           # AddSub
    | expr op=('='|'/='|'<'|'>'|'<='|'>=') expr  # Relational
    | '(' expr ')'                      # Parenthesis
    | ID '[' expr ']'                  # ListAccess
    | '#' ID                           # ListSize
    | '{' expr* '}'                    # ListLiteral
    | ID                               # Variable
    | NUM                              # Number
    | NOTE                             # Note
    ;

// Tokens
ID : [A-Z][a-zA-Z0-9_]* | [a-z][a-zA-Z0-9_]* ;

NOTE : [A-G][0-8]? ;

NUM : [0-9]+ ;

STRING : '"' (~["\r\n])* '"' ;

COMMENT : '###' .*? '###' -> skip ;

WS : [ \t\r\n]+ -> skip ;