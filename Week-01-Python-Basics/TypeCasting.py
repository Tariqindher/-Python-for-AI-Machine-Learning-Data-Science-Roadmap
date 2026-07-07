# Original values
string_num = "25"
int_num = 10
float_num = 19.99
text = ""
word = "Python"

# String to Integer
num = int(string_num)
print("String to Integer:", num, type(num))

# Integer to Float
decimal = float(int_num)
print("Integer to Float:", decimal, type(decimal))

# Float to Integer
whole = int(float_num)
print("Float to Integer:", whole, type(whole))

# Integer to String
text_num = str(int_num)
print("Integer to String:", text_num, type(text_num))

# Boolean Conversion
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print('bool(""):', bool(text))
print('bool("Python"):', bool(word))
