## Applied-Maths-sem_2
# [Лабораторная 1. Линейной программирование и симплекс-метод.](Applied-Maths-sem_2/lab1)

**Цель:** Реализовать симплекс метод с методом искусственного базиса для решения задач ЛП в канонической форме. Ответить на вопросы про двойственность задачи ЛП, метод искусственного базиса, выпуклость ОДР и графический метод решения задач ЛП.

Конструктор моего класса: 

```python
class SimplexMethod:
    def __init__(self, a: list, b: list, c: list, opt="max"):
        self.eps = 1e-6
        self.a = a
        self.b = b
        self.c = c
        self.opt = opt
        self.table = []
        self.variables = []
        if self.opt == 'min':
            for i in range(len(c)):
                c[i] = -c[i]


```
[Полная реализация](Applied-Maths-sem_2/lab1/lab1_SimplexMethod.py)
