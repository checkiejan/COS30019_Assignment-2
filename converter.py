import re
def postfix_to_infix(postfix_expr):
    stack = []

    for symbol in postfix_expr:
        # If the symbol is a propositional variable, push it to the stack
        if symbol.isalpha():
            stack.append(symbol)
        # If the symbol is a unary operator (~), pop the last element from the stack, combine it with the operator
        # and push the result back to the stack
        elif symbol == "~":
            operand = stack.pop()
            new_expr = f"{symbol}({operand})"
            stack.append(new_expr)
        # If the symbol is a binary operator (&, |, =>), pop the last two elements from the stack,
        # combine them with the operator and push the result back to the stack
        elif symbol in ["&", "||", "=>"]:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expr = f"({operand1} {symbol} {operand2})"
            stack.append(new_expr)
        # If the symbol is a biconditional operator (<=>), replace it with a combination of & and | operators
        elif symbol == "<=>":
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expr = f"(({operand1} & {operand2}) | (~{operand1} & ~{operand2}))"
            stack.append(new_expr)

    # The last element in the stack is the infix expression
    return stack[-1]

def posfixEval(input): #Shunting Yard algorithm to transform into postfix 
    operator_stack = []  # Stack to store operators
    lst = [] #list to store the sentence
    precedence = {"~": 3, "&": 2, "||": 1, "=>": 0, "<=>": 0}

    for token in input:
        if token in ["~", "&", "||", "=>", "<=>"]:
            while operator_stack and operator_stack[-1] != "(" and precedence[token] <= precedence[operator_stack[-1]]:
                temp = operator_stack.pop()
                lst.append(temp)
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                temp = operator_stack.pop()
                lst.append(temp)
            operator_stack.pop()  # Remove "(" from stack
        else:
            lst.append(token)

    while operator_stack:
        temp = operator_stack.pop()
        lst.append(temp)
    return lst #assign the list to the sentence list

string ="a<=>a"
input = re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]|\w*(?<!<)=>|<=>|[(]|[)]", string)
lst = posfixEval(input)
postfix_expr = ["A", "B", "<=>"]
print(postfix_to_infix(lst))  # Output: ((A & B) | (~A & ~B))
from sympy.parsing.sympy_parser import parse_expr
exp = parse_expr(postfix_to_infix(lst))
print(exp)