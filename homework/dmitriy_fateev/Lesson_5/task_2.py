first_program_output = "результат операции: 42"
second_program_output = "результат операции: 514"
third_program_output = "результат работы программы: 9"

first_index = first_program_output.index(':')
first_number = int(first_program_output[first_index + 1:]) + 10

second_index = second_program_output.index(':')
second_number = int(second_program_output[second_index + 1:]) + 10

third_index = third_program_output.index(':')
third_number = int(third_program_output[third_index + 1:]) + 10

print(first_number, second_number, third_number)