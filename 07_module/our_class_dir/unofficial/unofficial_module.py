import random
from our_class_dir.official.official_module import student_count

def study():
    print(f'{student_count}명의 학생들이 열심히 공부를 한다!')

def go_lunch(menus):
    return random.choice(menus)