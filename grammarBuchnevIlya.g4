grammar grammarBuchnevIlya;
IDENTIFIER : [a-zA-Z]+[a-zA-Z0-9]*;             // match lower-case identifiers
NUMBERS:
    BINARY
    | OCTAL
    | DECIMAL
    | HEXADECIMAL
    ;


fragment BINARY: [0-1]+('B'|'b');

fragment OCTAL: [0-7]+('O'|'o');

fragment DECIMAL: [0-9]+('D'|'d')?;

fragment HEXADECIMAL: [0-9]+([0-9]|'A'|'B'|'C'|'D'|'E'|'F'|'a'|'b'|'c'|'d'|'e'|'f')*('H'|'h');

BOOL_CONST: 'true'|'false';

type:
    int
    | float
    | bool
    ;

int: '%';
float: '!';
bool: '$';



program : '{' (description|operator';')+  '}' ;

description: ' ';

operator: ' ';

expression: operand ( operation_relationship operand)* ;

operand: summand (operation_summary summand)*;

summand: multiplier (operation_multiple multiplier)*;

multiplier:
    IDENTIFIER
    | NUMBERS
    | BOOL_CONST
    | operation_unary multiplier
    | '(' expression ')'
    ;

numbers: ;

operation_relationship: '<>'|'='|'<'|'<='|'>'|'>=';
operation_summary: '+'|'-'|'or';
operation_multiple: '*'|'/'|'and';
operation_unary: '~';

