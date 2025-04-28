import random

teacher_name = '이주원'
student_count = 30

def study():
    print(f'{student_count}명의 학생들이 열심히 공부를 한다!')

def lecture():
    print(f'{teacher_name} 선생님이 수업중이다~~~')

def go_lunch(menus):
    return random.choice(menus)
