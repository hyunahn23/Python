# 1. import 구문 사용
# our_class.py 모듈을 가져와서
# import our_class as oc

# # 선생님 이름과 학생 수를 출력하고
# print(our_class.teacher_name, our_class.student_count)

# # study() 함수와 lecture() 함수를 호출하고
# our_class.study()
# our_class.lecture()

# # 먹고 싶은 메뉴명이 5개 담긴 menus 리스트를 만들어서
# menus = ['짜장면', '제육볶음', '김밥', '샐러드', '샌드위치']

# # go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!
# print(our_class.go_lunch(menus))

###########################################

# 2. from-import 구문 사용
# our_class.py 모듈을 가져와서
# from our_class import teacher_name, student_count, study, lecture, go_lunch

# # 선생님 이름과 학생 수를 출력하고
# print(teacher_name, student_count)

# # study() 함수와 lecture() 함수를 호출하고
# study()
# lecture()

# # 먹고 싶은 메뉴명이 5개 담긴 menus 리스트를 만들어서
# menus = ['짜장면', '제육볶음', '김밥', '샐러드', '샌드위치']

# # go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!
# print(go_lunch(menus))

###########################################

# 3. 패키지 내의 모듈 import
import our_class_dir.official.official_module
from our_class_dir.unofficial.unofficial_module import study, go_lunch

# 선생님 이름과 학생 수를 출력하고
print(our_class_dir.official.official_module.teacher_name)
print(our_class_dir.official.official_module.student_count)

# study() 함수와 lecture() 함수를 호출하고
study()
our_class_dir.official.official_module.lecture()

# 먹고 싶은 메뉴명이 5개 담긴 menus 리스트를 만들어서
menus = ['짜장면', '제육볶음', '김밥', '샐러드', '샌드위치']

# go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해 보자!
print(go_lunch(menus))