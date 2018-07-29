class Student(object):
    """类"""
    name = 'Student'

    def __init__(self, name, score):
        # 这是属性
        # 访问限制
        self.__name = name
        self.score = score

    def _print_score(self):
        print('%s: %s' % (self.__name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()

if __name__ == '__main__':
    # 实例化对象
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart._print_score()
    lisa._print_score()
