import re
from sentence import *
string ="(a <=> (c => ~d))"
print(re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|\w*(?<!<)=>|<=>|[(]|[)]", string))
# sentence = Sentence(string)
# print(sentence.lst)
# sentence.setValue({"a": True})
operators = {"&": And, "=>": Imply ,"<=>": Bicondition,"~": Not,"||": Or}
lst = re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|\w*(?<!<)=>|<=>|[(]|[)]", string)
# visited = []
# i = 0
# while i < len(lst):
#     if lst[i] in operators:
#         if i+1 <len(lst) and lst[i+1] == "(":
#             temp1 = lst[i]
#             lst.pop(i)
#             y = i+1
#             while lst[y] != ")":
#                 y+=1

#             visited.append(y+1)
#             lst.insert(y+1,temp1)
#         elif i not in visited and i + 1<len(lst):
#             temp1 = lst[i]
#             lst.pop(i)
#             y = i+1
#             print(temp1)
#             while lst[y] not in operators:
#                 y+=1
#                 print(y)
#             visited.append(y+1)
#             lst.insert(y+1,temp1)
#             print(lst)
        
#     i += 1


# temp1 = lst[i]
# lst[i] = lst[i+1]       
# lst[i+1] = temp1
# print(sentence.result())
t1 = {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': True, 'd': True, 'a': True}
ls =[
    {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': True, 'h': True, 'd': True, 'a': True},
    {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': True, 'd': True, 'a': True},
    {'p2': True, 'p3': True, 'p1': True, 'c': True, 'e': True, 'b': True, 'f': True, 'g': False, 'h': False, 'd': True, 'a': True}
]
lst = [
    {'a': True, 'b': True, 'p3': True, 'p2': True, 'c': True, 'p1': True},
    {'a': True, 'b': False, 'p3': True, 'p2': True, 'c': True, 'p1': True}
]
#print(t1 in lst)


def evaluate_sentence(sentence, variables):
    sentence = re.findall("[a-zA-Z0-9]+|[&]|[~]|[|]+|\w*(?<!<)=>|<=>|[(]|[)]", sentence)
    output_queue = []  # Output queue for the Reverse Polish Notation (RPN)
    operator_stack = []  # Stack to store operators

    precedence = {"~": 3, "&": 2, "||": 1, "=>": 0, "<=>": 0}

    for token in sentence:
        if token in ["~", "&", "||", "=>", "<=>"]:
            while operator_stack and operator_stack[-1] != "(" and precedence[token] <= precedence[operator_stack[-1]]:
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop())
            operator_stack.pop()  # Remove "(" from stack
        else:
            output_queue.append(resolve_variable(token, variables))

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return evaluate_rpn(output_queue)


def evaluate_rpn(expression):
    print(expression)
    stack = []
    for token in expression:
        if token in ["~", "&", "||", "=>", "<=>"]:
            right_operand = stack.pop()
            if token != "~":
                left_operand = stack.pop()

            if token == "~":
                result = not right_operand
            elif token == "&":
                result = left_operand and right_operand
            elif token == "||":
                result = left_operand or right_operand
            elif token == "=>":
                result = (not left_operand) or right_operand
            elif token == "<=>":
                result = left_operand == right_operand

            stack.append(result)
        else:
            stack.append(token)

    return stack[0]


def resolve_variable(token, variables):
    if token in variables:
        return variables[token]
    else:
        raise ValueError("Undefined variable: " + token)


# Example usage
variables = {"a": True, "c": False, "d":True,"b":True}

# sentence1 = "A & B"
# result1 = evaluate_sentence(sentence1, variables)
# print(sentence1, "=", result1)

# sentence2 = "A || B"
# result2 = evaluate_sentence(sentence2, variables)
# print(sentence2, "=", result2)

# sentence3 = "A => B"
# result3 = evaluate_sentence(sentence3, variables)
# print(sentence3, "=", result3)

sentence4 = "a & b =>p3"
sentence = Sentence(sentence4)
#print(sentence.lst)
sentence.setValue({'a': True, 'b': False, 'p3': True, 'p2': True, 'c': True, 'p1': True})
print(sentence.result())


