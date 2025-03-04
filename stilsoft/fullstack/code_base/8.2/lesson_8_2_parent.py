class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)

    def run(self):
        print(f'Я не могу бежать, извини')    

class Runner(Person):
    def run(self):
        print(f'Привет, я - {self.firstname} и я бегу')
    pass

class Dancer(Person):
    pass

runner = Runner('Михаил', 'Краснодеревщик')
runner.print_name()
runner.run()

runner = Dancer('Михаил', 'Краснодеревщик')
runner.print_name()
runner.run()


class Article():
    def __init__(self, content):
        self.content = content

class ArticleExtended(Article):
    def count_symbols(self):
        return len(self.content)
    
    def count_words(self):
        words = self.content.split()
        return len(words)

article = ArticleExtended("""Ваш баланс состовляет rur -567.072.565,13. 
                  Номер заблокирован.
                  Вас ожидает 26 лет рабства. """)

print(article.count_symbols())
print(article.count_words())