def isability (pushed: str,poped : str) -> bool:
    pushed = (((pushed).strip()).split())
    pushed.reverse()
    poped = ((poped).strip()).split()

    # if len(pushed) != len(poped):
    #     return False

    temp = [None]
    for i in range (0, len(poped)) :
        if temp[len(temp)-1] != poped[i]:
            while temp[len(temp)-1] != poped[i]  and len(pushed)>0:
                temp.append(pushed.pop())
                if temp[len(temp)-1] == poped[i]:
                    print(temp[len(temp)-1])
                    temp.pop()
                    break
        else:
            print(temp[len(temp)-1])
            temp.pop()

    print(pushed,poped, temp)
    return True if temp == [None] else  False


pushed = input("pushed: ")
poped = input("poped: ")
print(isability(pushed, poped))