import mysql.connector as mysql
import os, dotenv, csv


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
datafile_path = os.path.join(homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")
dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor()


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8', newline='') as csv_file:
        file_data = csv.reader(csv_file)
        for row in file_data:
            yield row


reading_file = read_file(datafile_path)
columns = next(reading_file)

query = """
SELECT * FROM students 
JOIN `groups` ON students.group_id = `groups`.id 
JOIN books ON students.id = books.taken_by_student_id 
JOIN marks ON students.id = marks.student_id 
JOIN lessons ON marks.lesson_id = lessons.id 
JOIN subjects ON lessons.subject_id = subjects.id 
WHERE students.name = %s 
  AND students.second_name = %s 
  AND `groups`.title = %s 
  AND books.title = %s 
  AND subjects.title = %s 
  AND lessons.title = %s 
  AND marks.value = %s
"""

for line in reading_file:
    print(line)
    cursor.execute(query, line)
    result = cursor.fetchall()
    if not result:
        print("Не найдено")

db.close()
