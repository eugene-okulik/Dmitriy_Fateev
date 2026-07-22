first_program_output = "результат операции: 42"
second_program_output = "результат операции: 514"
third_program_output = "результат работы программы: 9"

def result(text):
    index = text.index(':')
    number = int(text[index + 1:]) + 10
    return number

numbers = (result(first_program_output),
           result(second_program_output),
           result(third_program_output))

print(*numbers)
