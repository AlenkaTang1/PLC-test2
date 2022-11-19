# PLC-test2

rules:
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
