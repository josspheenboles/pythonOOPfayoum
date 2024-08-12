import  re
emailpattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
str1='asd@gmail.com dskfsdljfkjdklfj asd2@rmail.com'
print(re.match(emailpattern,str1))#str must start with email
print(re.fullmatch(emailpattern,str1))#str all email
print(re.findall(emailpattern,str1))#str must start with email
# username=input('enter username')
# if(len(username)>8):
#     emailpattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#     email = input('enter email')
#     if(re.fullmatch(emailpattern,email) is not None):
#             password = input('enter password')
#             print(username,email,password)
#     else:
#       print('invalid email format')
# else:
#     print('username must more than 8 letters')
# import  math

# print(math.pi)
# import os
#
# print(os.getlogin())
# print(os.name)
# print(os.getpid())
# os.chdir('..')
# os.chdir('Day2')
# os.system('mkdir test')
#
# os.system('cp traineedb traineedbbackup12-8')