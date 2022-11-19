'''
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
'''
import re


class RDA:
  def __init__(self, tokens) :
    self.tokens = tokens
    self.current = 0
    self.currentToken = tokens[self.current]


  def start(self):
    if self.currentToken == 'S':
      self.getNextToken()
      self.stmt()
    else:
      self.error()

  def getNextToken(self):
    if self.current < len(self.tokens):
      self.current += 1
    self.currentToken = self.tokens[self.current]


  def stmt(self):
    match self.currentToken:
      case '[s]':
        self.switch()
      case '[l]':
        self.loop()
      case 'id':
        self.var_op()
      case '{':
        self.block()
      case _:
        self.error()


  def block(self):
    if self.currentToken == '{':
      self.getNextToken()
      while self.currentToken == '[s]' or self.currentToken == '[l]' or self.currentToken == 'id' or self.currentToken == '{':
        self.stmt()
        if self.currentToken == ';':
          self.getNextToken()
          self.stmt()
        else:
          self.error()
      if self.currentToken == '}':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()
    

  def loop(self):
    if self.currentToken == '[l]':
      self.getNextToken()
      if self.currentToken == '(':
        self.getNextToken()
        self.boolexpr()
        if self.currentToken == ')':
          self.getNextToken()
          self.block()
        else:
          self.error()
      elif self.currentToken == 'int_lit':
        self.getNextToken()
        self.block()
      else:
        self.error()
      pass
    else:
      self.error()

  '''
  <switch> --> '[s]' '(' <boolexpr> ')' <block>
  '''
  def switch(self):
    if self.currentToken == '[s]':
      self.getNextToken()
      if self.currentToken == '(':
        self.getNextToken()
        self.boolexpr()
        if self.currentToken == ')':
          self.getNextToken()
          self.block()
          if self.currentToken == '[e]':
            self.getNextToken()
            self.block()
        else:
          self.error()
      else:
        self.error()
    else:
      self.error()
  '''
  <boolexpr> --> <bor>{'AND' <bor>}
  <bor> --> <beq> {'OR' <beq>}
  <beq> --> <brel> {('!='|'==') <brel>}
  <bel> --> <bexpr> {('<='|'>='|'<'|'<') <bexpr>}
  <bexpr> --> <bterm> {('*'|'/'|'%') <bterm>}
  <bterm> --> <bnot> {('+'|'-') <bnot>}
  <bnot> --> '[!]'<bfacor>
  <bfactor>--> 'id'|'int_lit'|'bool_lit'
  ''' 
  def boolexpr(self):
    self.bor()
    while self.currentToken == '&&':
      self.getNextToken()
      self.bor()
  def bor(self):
    self.beq()
    while self.currentToken == '||':
      self.getNextToken()
      self.beq()
  def beq(self):
    self.brel()
    while self.currentToken == '!=' or self.currentToken == '==':
      self.getNextToken()
      self.brel()
  def brel(self):
    self.bexpr()
    while self.currentToken == '<=' or self.currentToken == '>=' or self.currentToken == '>' or self.currentToken == '<':
      self.getNextToken()
      self.bexpr()
  def bexpr(self):
    self.bterm()
    while self.currentToken == '*' or self.currentToken == '/' or self.currentToken == '%':
      self.getNextToken()
      self.bterm()
  def bterm(self):
    self.bfactor()
    while self.currentToken == '+' or self.currentToken == '-' :
      self.getNextToken()
      self.bfactor()
  def bfactor(self):
    if self.currentToken == 'id' or self.currentToken == 'int_lit':
      self.getNextToken()
    elif self.currentToken == '(':
      self.getNextToken()
      self.bexpr()
      if self.currentToken == ')':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()
    
  '''
  <var_op> --> 'id' (<declare>|<assign>)
  <declar> --> '[b1]'|'[b2]'|'[b4]'|'[b8]'
  <assign> --> '=' <expr>
  <expr> --> <term> {('*'|'/'|'%') <term>}
  <term> --> <factor> {('+'|'-') <factor>}
  <factor> --> 'id'|'int_lit'|'(' <expr> ')'
  '''
  def var_op(self):
    if self.currentToken == 'id':
      self.getNextToken()
      if self.currentToken == '[b1]'or self.currentToken =='[b2]'or self.currentToken =='[b4]'or self.currentToken =='[b8]':
        self.getNextToken()
      elif self.currentToken == '=':
        self.getNextToken()
        self.expr()
      else:
        self.error()
  
  def expr(self):
    self.term()
    while self.currentToken == '*' or self.currentToken == '/'or self.currentToken == '%':
      self.getNextToken()
      self.term()
  def term(self):
    self.factor()
    while self.currentToken == '+' or self.currentToken == '-' :
      self.getNextToken()
      self.factor()

  def error(self):
    print("syntax error")
    StopIteration

  def factor(self):
    '''
    <factor> --> 'id' | 'int_lit' | '('<expr>')'
    '''
    if self.currentToken == 'id' or self.currentToken == 'int_lit':
      self.getNextToken()
    elif self.currentToken == '(':
      self.getNextToken()
      self.expr()
      if self.currentToken == ')':
        self.getNextToken()
      else:
        self.error()
    else:
      self.error()
        



import re

def isVariable(str):
  return re.search("[a-z]|[A-Z]|_{6,8}", str)

#lexical analyzer:
class LEX:
  def __init__(self, str):
    self.str = str
  def error(self):
    print("lexical error")
    exit()
  def checkLex(self):
    lexs = []
    for lex in self.str:
      if lex == "START":
        lexs.append('S')
      elif lex == "[l]":
        lexs.append('[l]')
      elif lex == "[s]":
        lexs.append('[s]')
      elif lex == "[b1]":
        lexs.append('[b1]')
      elif lex == "[b2]":
        lexs.append('[b2]')
      elif lex == "[b4]":
        lexs.append('[b4]')
      elif lex == "[b8]":
        lexs.append('[b8]')
      elif lex == "[e]":
        lexs.append('[e]')
      elif lex == "+":
        lexs.append('+')
      elif lex == "-":
        lexs.append('-')
      elif lex == "*":
        lexs.append('*')
      elif lex == "/":
        lexs.append('/')
      elif lex == "%":
        lexs.append('%')
      elif lex == ">":
        lexs.append('>')
      elif lex == ">=":
        lexs.append('>=')
      elif lex == "<":
        lexs.append('<')
      elif lex == "<=":
        lexs.append('<=')
      elif lex == "==":
        lexs.append('==')
      elif lex == "!=":
        lexs.append('!=')
      elif lex == "{":
        lexs.append('{')
      elif lex == "}":
        lexs.append('}')
      elif lex == "=":
        lexs.append('=')
      elif lex == ";":
        lexs.append(';')
      elif lex == "END":
        lexs.append('E')
      elif lex == "(":
        lexs.append('(')
      elif lex == ")":
        lexs.append(')')
      elif lex == "&&":
        lexs.append('&&')
      elif lex == "||":
        lexs.append('||')
      elif lex == "T":
        lexs.append('T')
      elif lex.isnumeric():
        lexs.append('int_lit')
      elif isVariable(lex):
        lexs.append('id')
      else:
        self.error()
    return lexs
      





#first test file, no error
file = open("/Users/tangalenka/PLC/test1.txt", "rt")
data = file.read()
lexs1 = data.split()
tokenString1 = LEX(lexs1)
t1 = tokenString1.checkLex()
print(t1)
test_1 = RDA(t1)
test_1.start()
#second test file, no error
file = open("/Users/tangalenka/PLC/test2.txt", "rt")
data = file.read()
lexs2 = data.split()
tokenString2 = LEX(lexs2)
t2 = tokenString2.checkLex()
print(t2)
test_2 = RDA(t2)
test_2.start()
#test file, syntax error
file = open("/Users/tangalenka/PLC/test4.txt", "rt")
data = file.read()
lexs4 = data.split()
tokenString4 = LEX(lexs4)
t4 = tokenString4.checkLex()
print(t4)
test_4 = RDA(t4)
test_4.start()
#test file, lexical error
file = open("/Users/tangalenka/PLC/test3.txt", "rt")
data = file.read()
lexs3 = data.split()
tokenString3 = LEX(lexs3)
t3 = tokenString3.checkLex()

