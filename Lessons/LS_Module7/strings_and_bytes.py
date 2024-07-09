print('hello')
print(ord('h'))
a = 'hello'
chars = []
for i in a:
    chars.append(ord(i))
s = ''
for i in chars:
    s += chr(i)
print(s)

# for i in range(128):
#     print(chr(i))

# for i in range(1000, 2000):
#     print(chr(i))

print(hex(ord('h')))  # перевели символ в числовое представление, а затем в 16ричную систему
bb = b'\x68'  # класс байтов, меняем 0 на \ (тогда работает decode())
print(type(bb))
print(bb.decode())  # раскодировали, заменили


