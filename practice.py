#def swapPos(list, pos1, pos2):
 #   def swapPos(list, pos1, pos2):
 #       list[pos1], list[pos2] = list[pos2], list[pos1]
 #       return list


#swapPos([1,2,3,4],2,4)

#ef factorial(num):
#   if num < 2:
#       return num
#   else:
#       num = num * factorial(num-1)
#       return num

#def fib(n):
#    a=0
#    b=1
#    for i in range(n):
#        c=a+b
#        a=b
#        b = c
#    print(a)
#fib(7)


#def fib(n):
#    if n == 0:
#        return 0
#    if n == 1:
#        return 1
#    return fib(n-1) + fib(n-2)

#def digsum(num):
#    tot = 0
#    for i in range(0,len(str(num))):
#        tot += int(str(num)[i])
#    print(tot)
#digsum(2356)


##def sumDigits(num):
#    if num == 0:
#        return 0
#    return int(num % 10) + sumDigits(num//10)


###BINARY TREES


#class Node:
#    def __init__(self, val):
#        self.left = None
#        self.right = None
#        self.val = val


#n1 = Node(1)
#n2 = Node(2)
#n3 = Node(3)
#n4 = Node(4)
#n5 = Node(5)
#n6 = Node(6)
#n1.left = n2
#n1.right = n3
#n2.left = n4
#n2.right = n5
#n3.left = n6

##Left, Root Right
#def printInorder(root):
#    if root:
#        printInorder(root.left)
#        print(root.val)
#        printInorder(root.right)
#def printPostorder(root):
#    if root:
#        printInorder(root.left)
#        printInorder(root.right)
#        print(root.val)
#def printPreorder(root):
#    if root:
#        print(root.val)
#        printInorder(root.left)
#        printInorder(root.right)


####STACK PRACTICE

#Input = "()" = VALID
#Input = "(()" = INVALID
#Input = "(Hi))" = INVALID
#
# stack.pop()
# stack.push()
def validParen(str):
    #stack = []
    #stack.pop()
    #stack.append()
    #print(('INVALID', 'VALID')[str.count('(') == str.count(')')])
    stack = []
    for c in str:
        if c == '(':
            stack.push(1)
        elif c == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True

    stack = []
    print(stack.pop())










