
from Human import Human
#create objct from human class
obj1=Human(1,'aya ali','fayoum') #calling __init (self)
obj2=Human(2,'mark ','fayoum')
# obj3=Human()
obj1.count=100#remove adddress of count set by value
print(Human.count)#2
print(obj1.count)#100
print(obj2.count)#2
print(Human.getcount())
Human.measuretemp(37)
Human.measuretemp(38)
# obj1.id=10
# obj1.name='aya ali'
# obj1.add='fayoum'
# # print(obj1.id,obj1.name,obj1.add)
# obj1.drink()
# #instance var
# obj1.age=10

# obj1.eat()

# obj2.drink()
# print(type(obj1),obj1)
# print(type(obj2),obj2)

# import psycopg2
# #prepare db connection info
# host='localhost'
# user='iti'
# password='123'
# dbname='fayoumdemo'
# connection=psycopg2.connect( database=dbname,
#             user=user,
#             password=password,
#             host=host
#             )
# # print(type(connection),connection)
# cur=connection.cursor()
# cur.execute("insert into traineedata values(4,'mai',3);")
# traineeid=cur.fetchone()
# #insert,update,delete
# connection.commit()
# # recoreds=cur.fetchall()
# # # recoreds object of [(1,'aya',1),(),()]
# # print(recoreds)
# # for recored in recoreds:
# #     print('ID:',recored[0],"Name:",recored[1],"Track:",recored[2],sep='\n',end='\n============')

