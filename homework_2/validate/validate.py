def isability (pushed: str,poped : str) -> bool:
    pushed = (((pushed).strip()).split())
    pushed.reverse()
    poped = ((poped).strip()).split()

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