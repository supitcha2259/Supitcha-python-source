# ===========================
# 11. STRING FORMATTING
# ===========================

print("\n=== STRING FORMATTING ===")

# % formatting
name = "ashish"
age = 8
print("Using %% formatting:")
print("name=%s and age=%d" % (name, age))
print("name=%s and age=%d" % ("ankita", 6))

# .format() method
print("\nUsing .format() method:")
id_num = 10
name = 'shankar'
sal = 20000

# Different format styles
str1 = '{},{},{}'.format(id_num, name, sal) # '{},{},{}' เป็นฟอแมตของตัวแปร id_num, name, sal
#str1 = f'{id_num},{name},{sal}' เป็นวิธีเขียนอีกแบบ
print(str1)  # 10,shankar,20000 

str2 = '{} - {} - {}'.format(id_num, name, sal)
print(str2)  # 10 - shankar - 20000

str3 = 'id={}\nname={}\nsal={}'.format(id_num, name, sal)
print(str3)