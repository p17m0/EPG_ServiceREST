def is_valid(st):
    """
    Проверка на валидность.
    """
    if st.count('(') != st.count(')'):
        return False
    if '=' in st:
        return False
    return True

def calculate(s):
    if is_valid(s):
        def calc(it):
            def update(op, v, stack):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(int(stack.pop() / v))
            num, stack, sign = 0, [], "+"
            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num, stack)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, j = calc(it + 1)
                    it = j - 1
                elif s[it] == ")":
                    update(sign, num, stack)
                    return sum(stack), it + 1
                it += 1
            update(sign, num, stack)
            return sum(stack)

        return calc(0)
    return -1
