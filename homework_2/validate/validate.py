def validate_stack_sequences(pushed, popped):
    if len(pushed) != len(popped) or not pushed:
        return False

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
