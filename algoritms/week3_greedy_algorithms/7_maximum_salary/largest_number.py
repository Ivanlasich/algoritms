
maxi=0
def compare(a):
    s = str(a)
    div = maxi -len(s)
    return int(s + div*s[-1])

if __name__ == '__main__':
    n = int(input())
    Digits = list(map(int, input().split()))
    answer=[]
    while Digits!=[]:
        maxDigit=0
        for digit in Digits:
            if (int(str(digit)+str(maxDigit)) >= int(str(maxDigit)+str(digit))):
                maxDigit = digit
        answer.append(maxDigit)
        Digits.remove(maxDigit)
print(''.join([str(i) for i in answer]))