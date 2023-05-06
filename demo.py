# 测试
# print("Hello World")



# 创建对象
class Student:
    def __init__(self, stu_no, stu_name, age):
        self.stu_no = stu_no
        self.stu_name = stu_name
        self.age = age
    
    def study(self):
        print(self.stu_name + '正在学习')

    def sleep(self):
        print(self.stu_name + '正在睡觉')
        

        

stu1 = Student('0001', 'Aaron', '21')
stu1.study()
stu1.sleep()


        

