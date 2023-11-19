# PLC-test2
creating a new programming language as well as the lexical and syntax compiler for it

## language rules
lexical rules (regular expression):
keyword, loop: \[ l \]
keyword, switch statement: \[ s \]
keyword, else: \[ e \]
keyword, start: START
keyword, end: END
keyword, store byte1: \[ b1 \]
keyword, store byte2: \[ b2 \]
keyword, store byte4: \[ b4 \]
keyword, store byte8: \[ b8 \]
keyword, true: T
keyword, and: & &
keyword, or: | |
special symbol, left_paran: \(
special symbol, right_paran: \)
special symbol, end of statement: ;
special symbol, begin of code block: \{
special symbol, end of code block: \}
special symbol, add: \+
special symbol, minor: \-
special symbol, multiply: \*
special symbol, devide: \/
special symbol, modul: \%
special symbol, assign: =
special symbol, not equal: !=
special symbol, equal: =
special symbol, less than: <
special symbol, less or equal: < =
special symbol, greater than: >
special symbol, greater or equal: >=
int_lit: [0-9]+
identifier: ([a-zA-Z]|_){6,8}

syntax rules:
s--> 'START' <stmt> 
<stmt> --> <switch>|<loop>|<block>|<var_op>
<block> --> '{' <stmt> ';' '}'
<switch> --> '[s]' <boolexpr> <block> ['[e]'<block>]
<loop> --> '[l]' <boolexpr> <block>
<var_op> --> 'id' (<declare>|<assign>)
<declar> --> '[b1]'|'[b2]'|'[b4]'|'[b8]'
<assign> --> '=' <expr>
<expr> --> <term> {('*'|'/'|'%') <term>}
<term> --> <factor> {('+'|'-') <factor>}
<factor> --> 'id'|'int_lit'|'(' <expr> ')'

<boolexpr> --> <bor>{'AND' <bor>}
<bor> --> <beq> {'OR' <beq>}
<beq> --> <brel> {('!='|'==') <brel>}
<bel> --> <bexpr> {('<='|'>='|'<'|'<') <bexpr>}
<bexpr> --> <bterm> {('*'|'/'|'%') <bterm>}
<bterm> --> <bfactor> {('+'|'-') <bfactor>}
<bfactor>--> 'id'|'int_lit'|'bool_lit'

every rule set in this language conforms to the standard of an LL Grammar and there's no lefthand recursion. 
