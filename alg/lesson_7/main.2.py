def Is(s):
    dict = {'{':'}','[':']','(':')'}
    a = s[::-1]
    for i in range(len(s)//2):
        if dict[s[i]] == a[i]:
            continue
        else:
            return 'no'
    return 'yes'

def Is2(s):
    dict = {'{': '}', '[': ']', '(': ')'}
    t = 0
    i = len(s) - 1
    while t <= len(s) // 2:
        if s[i] != dict[s[t]]:
            return 'no'
        t += 1
        i -= 1
    return 'yes'

if __name__ == '__main__':
    s = '{[]}'
    print(Is(s))
    list = ['{[]}']
    list.pop()