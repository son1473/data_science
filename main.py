#거꾸로 읽어도 똑같은 단어를 팔린드롬(palindrome)이라고 한다.

def is_palindrome(word):
    for i in range(len(word)//2): #절반까지만 테스트 하겠다.
        if word[i] != word[(-i)-1]: #절반 기준 앞과 뒤를 순서대로 비교하면서, 틀린게 있으면 False, 없으면 True
            return False
    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
