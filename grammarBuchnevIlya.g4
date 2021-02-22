grammar grammarBuchnevIlya;

//<идентификатор>::= <буква> {<буква> | <цифра>}
OPEN_PROGRAM: '{';
CLOSE_PROGRAM: '}';
END_LINE: ';';

BOOL: 'true'|'false';
//<тип>::= % | ! | $
TYPE:
    '%'//integer
    | '!'//float
    | '$'//bool
    ;

WS : [ \t\r\n]+ -> skip ;
SPACE : ' ';

OPERATION_RELATIONSHIP: '<>'|'='|'<'|'<='|'>'|'>=';
OPERATION_SUMMARY: '+'|'-'|'or';
OPERATION_MULTIPLE: '*'|'/'|'and';
OPERATION_UNARY:'~';

IDENTIFIER : [a-zA-Z]([a-zA-Z]|NUMBER_STRING)*;

//<число>::= <целое> | <действительное>
numbers: INTEGER | real;

//<числовая_строка>::= {/ <цифра> /}
NUMBER_STRING: [0-9]+;

//<целое>::= <двоичное> | <восьмеричное> | <десятичное> | <шестнадцатеричное>
INTEGER:
    BINARY
    | OCTAL
    | DECIMAL
    | HEXADECIMAL
    ;

//<действительное>::= <числовая_строка> <порядок> | [<числовая_строка>] . <числовая_строка> [порядок]
real: (NUMBER_STRING order) | (NUMBER_STRING)? '.' NUMBER_STRING (order)?;

//<двоичное>::= {/ 0 | 1 /} (B | b)
BINARY: [0-1]+('B'|'b');

//<восьмеричное>::= {/ 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 /} (O | o)
OCTAL: [0-7]+('O'|'o');

//<десятичное>::= {/ <цифра> /} [D | d]
DECIMAL: NUMBER_STRING('D'|'d')?;

//<шестнадцатеричное>::= <цифра> {<цифра> | A | B | C | D | E | F | a | b |  c | d | e | f} (H | h)
HEXADECIMAL: NUMBER_STRING([0-9][a-fA-F])*('H'|'h');



//<порядок>::= ( E | e )[+ | -] <числовая_строка>
order: ('E'|'e') ('+'|'-')?;
//<логическая_константа>::= true | false


//<выражение>::= <операнд>{<операции_группы_отношения> <операнд>}
expression: operand ( OPERATION_RELATIONSHIP operand)* ;

//<операнд>::= <слагаемое> {<операции_группы_сложения> <слагаемое>}
operand: summand (OPERATION_SUMMARY summand)*;

//<слагаемое>::= <множитель> {<операции_группы_умножения> <множитель>}
summand: multiplier (OPERATION_MULTIPLE multiplier)*;

//<множитель>::= <идентификатор> | <число> | <логическая_константа> | <унарная_операция> <множитель> | (<выражение>)
multiplier:
    BOOL
    |IDENTIFIER
    | numbers
    | OPERATION_UNARY multiplier
    | '(' expression ')'
    ;



//<программа>::= «{» {/ (<описание> | <оператор>) ; /} «}»
program : OPEN_PROGRAM (description|operator END_LINE)+  CLOSE_PROGRAM;

//<описание>::= {<идентификатор> {, <идентификатор> } : <тип> ;}
description: (IDENTIFIER (',' IDENTIFIER )* ':' TYPE ';')+;




//<оператор>::= <составной> | <присваивания> | <условный> | <фиксированного_цикла> | <условного_цикла> | <ввода> | <вывода>
operator: composite| assignments|conditional|fixed_cycle|conditional_loop|input_m|output_m;

//<составной>::= «{» <оператор> { ; <оператор> } «}»
composite: '{' operator (';' operator)* '}';

//<присваивания> ::= [ let ] <идентификатор> = <выражение>
assignments: ('let')? IDENTIFIER '=' expression;

//<условный>::= if <выражение> then <оператор> [else <оператор>] end_else
conditional: 'if' expression 'then' operator ('else' operator)* 'end_else';

//<фиксированного_цикла>::= for «(» [<выражение>] ; [<выражение>] ; [<выражение>] «)» <оператор>
fixed_cycle: 'for' '(' (expression)? ';' (expression)? ';'(expression)? ')' operator;

//<условного_цикла>::= do while <выражение> <оператор> loop
conditional_loop: 'do' 'while' expression operator 'loop';

//<ввода>::= input «(»<идентификатор> {пробел <идентификатор>}«)»
input_m: 'input' '(' IDENTIFIER (' ' IDENTIFIER)* ')' ;

//<вывода>::= output «(»<выражение> { пробел <выражение> }«)»
output_m: 'output' '(' expression (' ' expression)* ')';

//<многострочные_комментарии>::=/* */
multistr_comment: '/*' .*? '*/';

