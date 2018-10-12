class FaResult:
    CHIDAO = 'CHIDAO'
    KUANGKE = 'KUANGKE'
    DAJIA = 'DAJIA'


class Teacher:

    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.lesson_list = []
        self.teach_count = 0

    def teach(self):
        lesson = self.find_current_lesson()
        lesson.add_teach_count()

    def fa(self):
        pass

    def find_current_lesson(self):
        if len(self.lesson_list) > 0:
            return self.lesson_list[-1]
        else:
            return None

    def add_lesson(self, lesson):
        self.lesson_list.append(lesson)

    def what_lessons(self):
        print(self.lesson_list)

    def add_teach_count(self):
        self.teach_count += 1


class Student:

    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.beifa_count = 0

    def fuwocheng(self, count):
        if count > 10:
            print('jujue fuwocheng')
        else:
            print('zuo fuwocheng %d' % count)
        self.beifa_count += 1


class Lesson:

    def __init__(self, lesson_id, lesson_name):
        self.lesson_id = lesson_id
        self.lesson_name = lesson_name

    def __repr__(self):
        return self.lesson_name

    def __str__(self):
        return self.lesson_id


lesson1 = Lesson('python180401', 'python basic')
lesson2 = Lesson('python180402', 'python django')
lesson3 = Lesson('python180403', 'python scrapy')

teacher_xiao = Teacher(1, 'xiao')

teacher_xiao.add_lesson(lesson1)
teacher_xiao.add_lesson(lesson2)
teacher_xiao.add_lesson(lesson3)

teacher_xiao.what_lessons()

maxiangyang = Student(1, 'maxiangyang')