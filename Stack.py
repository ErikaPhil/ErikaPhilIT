# Description: Converts Infix Notation to Postfix Notation
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]

infixString = str(input("Enter an infix notation: "))
def InfixToPostfix(infixString):

    prec = {"*": 5, "/": 4, "+": 3, "-": 2, "(": 1}
    operand = "0123456789"
    op = "+-*/"
    stack = Stack()
    postFix = []
    cList = infixString.split()

    for c in cList:

        if c in operand:
            postFix.append(c)

        elif c in operand and c in op:
            
        elif c == "(":
            stack.push(c)

        elif c == ")":
            while True:
                next = stack.pop()
                if next is None or next == '(':
                    break
                elif not next.isidentifier():
                    postFix.append(next)

        else:
            if not stack.isEmpty():
                next = stack.peek()
                while not stack.isEmpty() and prec[next] >= prec[c] and c.isidentifier():
                    postFix.append(stack.pop())
            stack.push(c)

    while not stack.isEmpty():
        postFix.append(stack.pop())

    return " ".join(postFix)

print("Postfix Notation: {}".format(InfixToPostfix(infixString)))


postfixString = (InfixToPostfix(infixString))
def postfixStringEval(postfixString):

    operand = "0123456789"
    operandStack = Stack()
    cList = postfixString.split()
    
    for c in cList:

        if c in operand:
            operandStack.push(int(c))

        else:
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()

            result = dotheMath(c, int(operand1), int(operand2))
            operandStack.push(result)

    return operandStack.pop()

def dotheMath(operator,op1, op2):

    if operator == "*":
        return op2 * op1

    elif operator == "/":
        return op2 / op1

    elif operator == "+":
        return op2 + op1

    else:
        return op2 - op1
print("The result is {}".format(postfixStringEval(postfixString)))
