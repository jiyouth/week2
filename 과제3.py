studentscore = [70,80,90,100,90,50,60]

for i in range(len(studentscore)):
    if studentscore[i] >= 80:
        print('학생 %d번은 합격입니다.' % (i+1))
    else: 
        print('학생 %d번은 불합격 입니다.' % (i+1))