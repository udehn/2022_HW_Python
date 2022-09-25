
def check_parentheses_balance(str):
    LeftParentheses = ['(', '[', '{']
    RightParentheses = [')', ']', '}']
    temp = list()
    for c in str:
        if c not in LeftParentheses and c not in RightParentheses:
            continue
        elif c in LeftParentheses:
            temp.append(c)
        elif len(temp) and LeftParentheses.index(temp[-1]) == RightParentheses.index(c):
            temp.pop()
        else:
            return False
    return True


if __name__ == '__main__':

    # Input
    # str = input("Input:")

    # sample 1
    str = "(hello)"

    # sample 2
    # str = "(22+3)*(21/[34+1)]"

    if check_parentheses_balance(str):
        print('True')
    else:
        print('False')
