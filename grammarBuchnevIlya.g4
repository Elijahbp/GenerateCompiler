grammar grammarBuchnevIlya;
//<идентификатор>::= <буква> {<буква> | <цифра>}
IDENTIFIER : [a-zA-Z]+[a-zA-Z0-9]*;

//<число>::= <целое> | <действительное>
numbers: INTEGER | real;

//<числовая_строка>::= {/ <цифра> /}
number_string: [0-9]+;

//<целое>::= <двоичное> | <восьмеричное> | <десятичное> | <шестнадцатеричное>
INTEGER:
    BINARY
    | OCTAL
    | DECIMAL
    | HEXADECIMAL
    ;

//<двоичное>::= {/ 0 | 1 /} (B | b)
fragment BINARY: [0-1]+('B'|'b');

//<восьмеричное>::= {/ 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 /} (O | o)
fragment OCTAL: [0-7]+('O'|'o');

//<десятичное>::= {/ <цифра> /} [D | d]
fragment DECIMAL: number_string('D'|'d')?;

//<шестнадцатеричное>::= <цифра> {<цифра> | A | B | C | D | E | F | a | b |  c | d | e | f} (H | h)
fragment HEXADECIMAL: number_string([0-9]|'A'|'B'|'C'|'D'|'E'|'F'|'a'|'b'|'c'|'d'|'e'|'f')*('H'|'h');

//<действительное>::= <числовая_строка> <порядок> | [<числовая_строка>] . <числовая_строка> [порядок]
real: (number_string order) | (number_string)? '.' number_string (order)?;

//<порядок>::= ( E | e )[+ | -] <числовая_строка>
order: ('E'|'e') ('+'|'-')?;
//<логическая_константа>::= true | false
BOOL_CONST: 'true'|'false';

//<выражение>::= <операнд>{<операции_группы_отношения> <операнд>}
expression: operand ( operation_relationship operand)* ;

//<операнд>::= <слагаемое> {<операции_группы_сложения> <слагаемое>}
operand: summand (operation_summary summand)*;

//<слагаемое>::= <множитель> {<операции_группы_умножения> <множитель>}
summand: multiplier (operation_multiple multiplier)*;

//<множитель>::= <идентификатор> | <число> | <логическая_константа> | <унарная_операция> <множитель> | (<выражение>)
multiplier:
    IDENTIFIER
    | NUMBERS
    | BOOL_CONST
    | operation_unary multiplier
    | '(' expression ')'
    ;

operation_relationship: '<>'|'='|'<'|'<='|'>'|'>=';
operation_summary: '+'|'-'|'or';
operation_multiple: '*'|'/'|'and';
operation_unary: '~';


//<программа>::= «{» {/ (<описание> | <оператор>) ; /} «}»
program : '{' (description|operator';')+  '}' ;

//<описание>::= {<идентификатор> {, <идентификатор> } : <тип> ;}
description: (IDENTIFIER (',' IDENTIFIER )* ':' type ';')*;

//<тип>::= % | ! | $
type:
    int
    | float
    | bool
    ;

int: '%';
float: '!';
bool: '$';

//<оператор>::= <составной> | <присваивания> | <условный> | <фиксированного_цикла> | <условного_цикла> | <ввода> | <вывода>
operator: composite| assignments|conditional|fixed_cycle|conditional_loop|input|output;

//<составной>::= «{» <оператор> { ; <оператор> } «}»
composite: '{' operator (';' operator)* '}';

//<присваивания> ::= [ let ] <идентификатор> = <выражение>
assignments: ('let')? IDENTIFIER '=' expression;

//<условный>::= if <выражение> then <оператор> [else <оператор>] end_else
conditional: 'id' expression 'then' operator ('else' operator)* 'end_else';

//<фиксированного_цикла>::= for «(» [<выражение>] ; [<выражение>] ; [<выражение>] «)» <оператор>
fixed_cycle: 'for' '(' (expression)? ';' (expression)? ';'(expression)? ')' operator;

//<условного_цикла>::= do while <выражение> <оператор> loop
conditional_loop: 'do' 'while' expression operator 'loop';

//<ввода>::= input «(»<идентификатор> {пробел <идентификатор>}«)»
input: 'input' '(' IDENTIFIER (' ' IDENTIFIER)* ')' ;

//<вывода>::= output «(»<выражение> { пробел <выражение> }«)»
output: 'output' '(' expression (' ' expression)* ')';

//<многострочные_комментарии>::=/* */
multistr_comment: '/*' '*/';
