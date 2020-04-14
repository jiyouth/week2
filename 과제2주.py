class Student:
    def __init__(self,id,grade_list):
        self.id = id
        self.grade_list = grade_list

class AvgCalculator:
    def __init__(self):
        self.dict = {}

    def calc_avg_grade(self,stu):
        self.dict[stu.id] = (stu.grade_list[0]+stu.grade_list[1]+stu.grade_list[2])/3

    def __str__(self):
        sdict = sorted(self.dict.items())
        for id,avg in sdict: 
            print ("Student ID: {}, Average Grade: {}".format(id,avg))

stu1 = Student(id="2015104221", grade_list=[30, 60, 60])
stu2 = Student(id="2019311060", grade_list=[80, 70, 90])
stu3 = Student(id="2015105323", grade_list=[20, 30, 40])
calculator = AvgCalculator()

calculator.calc_avg_grade(stu1)
calculator.calc_avg_grade(stu2)
calculator.calc_avg_grade(stu3)

calculator.strprint()