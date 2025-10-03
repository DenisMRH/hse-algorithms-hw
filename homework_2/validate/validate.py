def validate_stack_sequences(pushed, popped):
    if len(pushed) != len(popped) or not pushed:
        return False

<<<<<<< HEAD
    if len(pushed) != len(poped):
        return False

    stack = [None]

    for i in range (0, len(poped)) :
        if stack[len(stack)-1] != poped[i]:

            while stack[len(stack)-1] != poped[i]  and len(pushed)>0:
                stack.append(pushed.pop())

                if stack[len(stack)-1] == poped[i]:
                    stack.pop()
                    break
        else:
            stack.pop()

    return True if stack == [None] else  False

if __name__ == "__main__":
    pushed = input("pushed: ")
    poped = input("poped: ")
    print(isability(pushed, poped))
=======
    stack = []
    j = 0

    for x in pushed:
        stack.append(x)
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1

    return not stack
    
def parse_line(s):
    return [int(x) for x in s.strip().split()]


if __name__ == "__main__":
    pushed = parse_line(input("pushed: "))
    popped = parse_line(input("popped: "))
    print(validate_stack_sequences(pushed, popped))
>>>>>>> hw2
