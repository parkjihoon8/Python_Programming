#문자열
#"", ''

a ="python"
print(a, type(a))
b = 'python'

# I'll be back
print("I'll be back")
print('I\'ll be back')


multiline = """
life is short
you need python"""

print(multiline)

#docstring
def func():
    """
    이 함수는 테스트용입니다
    """
    pass
print(func.__doc__)

#문자열 연결
print("Hello" + "python")

#문자열 반복
print("Hello" * 10)
print("-" * 100)
print("Hello" + 10)