grammar grammarBuchnevIlya;



//<логическая_константа>::= true | false
BOOL: 'true'|'false';
//<тип>::= % | ! | $
TYPE:
    '%'//integer
    | '!'//float/real
    | '$'//bool
    ;

WS : [\t\r\n]+ -> skip ;
SPACE : ' ';
COMMA : ',' ;
COLON : ':';
SEMICOLON : ';';

BLOCK_OPEN : '(';
BLOCK_CLOSE : ')';


OPERATION_RELATIONSHIP: '='|'<>'|'<'|'<='|'>'|'>=';
OPERATION_SUMMARY: '+'|'-'|'or';
OPERATION_MULTIPLE: '*'|'/'|'and';
OPERATION_UNARY:'~';

//<числовая_строка>::= {/ <цифра> /}
fragment NUMBER_STRING: [0-9]+;

//<идентификатор>::= <буква> {<буква> | <цифра>}
IDENTIFIER : [a-zA-Z]([a-zA-Z]|NUMBER_STRING)*;

//<число>::= <целое> | <действительное>
NUMBERS: INTEGER| REAL;


//<целое>::= <двоичное> | <восьмеричное> | <десятичное> | <шестнадцатеричное>
INTEGER:
    BINARY
    | OCTAL
    | DECIMAL
    | HEXADECIMAL
    ;



//<двоичное>::= {/ 0 | 1 /} (B | b)
BINARY: [0-1]+('B'|'b');

//<восьмеричное>::= {/ 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 /} (O | o)
OCTAL: [0-7]+('O'|'o');

//<десятичное>::= {/ <цифра> /} [D | d]
DECIMAL: NUMBER_STRING ('D'|'d')?;

//<шестнадцатеричное>::= <цифра> {<цифра> | A | B | C | D | E | F | a | b |  c | d | e | f} (H | h)
HEXADECIMAL: NUMBER_STRING ([0-9]|[a-fA-F])*('H'|'h');

//<действительное>::= <числовая_строка> <порядок> | [<числовая_строка>] . <числовая_строка> [порядок]
REAL: ((NUMBER_STRING ORDER) | ((NUMBER_STRING)? '.' NUMBER_STRING (ORDER)?));

//<порядок>::= ( E | e )[+ | -] <числовая_строка>
fragment ORDER: ('E'|'e') ('+'|'-')? NUMBER_STRING;


//<программа>::= «{» {/ (<описание> | <оператор>) ; /} «}»
program : '{' (description|operator ';')+  '}';

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
fixed_cycle: 'for' BLOCK_OPEN (expression)? ';' (expression)? ';'(expression)? BLOCK_CLOSE operator;

//<условного_цикла>::= do while <выражение> <оператор> loop
conditional_loop: 'do' 'while' expression operator 'loop';



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
    | NUMBERS
    | OPERATION_UNARY multiplier
    | '(' expression ')'
    ;

//<ввода>::= input «(»<идентификатор> {пробел <идентификатор>}«)»
input_m: 'input' BLOCK_OPEN IDENTIFIER (' ' IDENTIFIER)* BLOCK_CLOSE ;

//<вывода>::= output «(»<выражение> { пробел <выражение> }«)»
output_m: 'output' BLOCK_OPEN expression ( SPACE expression)* BLOCK_CLOSE;

//<многострочные_комментарии>::=/* */
multistr_comment: '/*' .*? '*/';