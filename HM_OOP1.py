class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calculate_avg_grade(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        result = round(sum_ / len_, 2)
        return result

    def __gt__(self, other_student):
        return self.calculate_avg_grade() > other_student.calculate_avg_grade()

    def avg_course_student(self, course):
        if course in self.grades:
            sum_course = sum(self.grades[course])
            len_course = len(self.grades[course])
            return sum_course / len_course
        else:
            return "Ошибка"

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.calculate_avg_grade()}\n'
                f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {",".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}

    def calculate_avg_grade(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        result = round(sum_ / len_, 2)
        return result

    def avg_course_lecturer(self, course):
        if course in self.grades:
            sum_course = sum(self.grades[course])
            len_course = len(self.grades[course])
            return sum_course / len_course
        else:
            return "Ошибка"

    def __gt__(self, other_lecturer):
        return self.calculate_avg_grade() > other_lecturer.calculate_avg_grade()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calculate_avg_grade()}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student1 = Student('Иван', 'Иванов', 'M')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']

student2 = Student('Елена', 'Смирнова', 'F')
student2.courses_in_progress += ['Python', 'Java']
student2.finished_courses = ['Введение в программирование']

reviewer1 = Reviewer('Петр', 'Петров')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Ирина', 'Попова')
reviewer2.courses_attached += ['Python']

lecturer1 = Lecturer('Борис', 'Борисов')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Александра', 'Александрова')
lecturer2.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 9)

student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer2, 'Python', 8)
student2.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer2, 'Python', 7)


print(student1)
print(student2)
print()
print(lecturer1)
print(lecturer2)
print()

print('Сравнение по средним оценкам:')
print(f'{student1.name} {student1.surname} < {student2.name} {student2.surname}', student1 < student2)
print(f'{lecturer1.name} {lecturer1.surname} < {lecturer2.name} {lecturer2.surname}', lecturer1 < lecturer2)
print()

lecturer_list = [lecturer1, lecturer2]
for lecturer in lecturer_list:
    print(f"Средняя оценка за лекции лектора {lecturer.name} {lecturer.surname} - {Lecturer.avg_course_lecturer(lecturer, 'Python')}")
print()

student_list = [student1, student2]
for student in student_list:
    print(f"Средняя оценка за лекции студента {student.name} {student.surname} - {Student.avg_course_student(student, 'Python')}")


