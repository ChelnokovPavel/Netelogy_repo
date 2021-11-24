from students_and_mentor import Student, Mentor


def avg_grades(grades):
    """Расчет средней оценки"""
    lst = []
    for grade in grades.values():
        lst += grade
    return round(sum(lst)/len(lst), 1)


class Lecturer(Mentor):
    """Лекторы"""
    def __init__(self, *args):
        super().__init__(*args)
        self.grades = {}

    def rate_hw(self, *args, **kwargs):
        print('Лекторы не должны ставить оценки!')

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {avg_grades(self.grades)}'

    def __lt__(self, other):
        if self.grades and other.grades:
            if avg_grades(self.grades) < avg_grades(other.grades):
                return True
            else:
                return False
        else:
            return False


class Reviewer(Mentor):
    """Оценищики"""
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class NewStudent(Student):
    """Студенты"""
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress = ''
        for course in self.courses_in_progress:
            courses_in_progress = f'{courses_in_progress}{course}, '
        finished_courses = ''
        for course in self.finished_courses:
            finished_courses = f'{finished_courses}{course}, '
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {avg_grades(self.grades)}\n' \
               f'Курсы в процессе изучения: {courses_in_progress[:-2]}\n' \
               f'Завершенные курсы: {finished_courses[:-2]}'

    def __lt__(self, other):
        if self.grades and other.grades:
            if avg_grades(self.grades) < avg_grades(other.grades):
                return True
            else:
                return False
        else:
            return False


# Лекторы
Odel = Lecturer('Одел', 'Мужикшляпу')
Odel.courses_attached.append('Python')
Shlyapa = Lecturer('Аона', 'Емукакраз')
Shlyapa.courses_attached.append('Data Science')

# Оценищики
Zahodit = Reviewer('Заходит', 'Вбар')
Zahodit.courses_attached.append('Git')
Unlimited = Reviewer('Бесконечное', 'Числоматематиков')
Unlimited.courses_attached.append('Python')

# Студенты
Lupa = NewStudent('Лупа', 'Запупу', 'Муж')
Lupa.courses_in_progress = ['Python', 'Git', 'Бухгалтерский учет']
Lupa.add_courses('Хитрость')
Pupa = NewStudent('Пупа', 'Неполучилзарплату', 'Муж')
Pupa.courses_in_progress = ['Python', 'Data Science', 'Экономика']


# Задание 2

Unlimited.rate_hw(Lupa, 'Python', 10)
Unlimited.rate_hw(Lupa, 'Python', 7)
Unlimited.rate_hw(Lupa, 'Git', 10)
Zahodit.rate_hw(Lupa, 'Git', 2)

# Возвращает сообщение, рейзить ошибку не стал
Odel.rate_hw(Lupa, 'Python', 10)

# Студент ставит лектору оценку
Pupa.rate_lecture(Shlyapa, 'Data Science', 5)
Pupa.rate_lecture(Shlyapa, 'Data Science', 10)
Pupa.rate_lecture(Shlyapa, 'Data Science', 128)


# Задание 3
print(Shlyapa, '\n')
print(Unlimited, '\n')
print(Lupa)


# Задание 4
Unlimited.rate_hw(Pupa, 'Python', 666)
ppl = [Lupa, Pupa]


def comparison(peoples, course):
    avg = []
    for people in peoples:
        if course in people.grades:
            avg += people.grades[course]
    return f'Средняя оценка по курсу {course}: {round(sum(avg)/len(avg), 1)}'


print(comparison(ppl, 'Python'))






