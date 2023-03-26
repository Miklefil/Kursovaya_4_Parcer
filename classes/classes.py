

class Vacancy:
    __slots__ = ('name', 'url', 'description', 'salary', 'date_published')
    self.name = data['name']
    self.url = data['url']
    self.description = data['description']
    self.salary = data.get('salary')
    self.date_published = data['date_published']

    def __gt__(self, other):
        return self.date_published > other.date_published

    def __lt__(self, other):
        return self.date_published < other.date_published

    def __str__(self):
        return f'Вакансия - {self.name}, заработная плата - {self.get_salary()}'

    def get_salary(self) -> str:
        """Возвращает зарплату в отформативанном виде"""
        if self.salary is not None:
            if self.salary.get('from') not in [0, None] and self.salary.get('to') not in [0, None]:
                return f"от {self.salary.get('from')} до {self.salary.get('to')} руб/мес"