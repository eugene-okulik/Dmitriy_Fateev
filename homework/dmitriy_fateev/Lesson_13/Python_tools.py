import os
from datetime import datetime, timedelta


DAYS_OF_WEEK = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
datafile_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")


def read_file():
    with open(datafile_path, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            yield f'{line.split()[1]} {line.split()[2]}'


LINE = read_file()


def parse_date(line):
    return datetime.strptime(line, "%Y-%m-%d %H:%M:%S.%f")


def task_1(date):
    print(f"1. На неделю позже: {date + timedelta(weeks=1)}")


def task_2(date):
    print(f"2. День недели: {DAYS_OF_WEEK[date.weekday()]}")


def task_3(date):
    print(f"3. Было дней назад: {(datetime.now() - date).days}")


STEPS = [task_1, task_2, task_3]

for step_number, step in enumerate(STEPS):
    try:
        this_line = next(LINE)
        step(parse_date(this_line))

    except ValueError as e:
        print(f"Ошибка в строке {step_number + 1}: {e}")
