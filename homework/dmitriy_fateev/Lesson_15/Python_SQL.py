import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO students (name, second_name) VALUES ('John', 'Brittle')")
db.commit()
student_id = cursor.lastrowid

cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('1984', %s)",
               (student_id,))
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES ('Дом в котором...', %s)",
               (student_id,))
db.commit()

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) values ('cool_guys', 'may 2026', 'oct 2026')")
group_id = cursor.lastrowid
db.commit()

cursor.execute("UPDATE students set group_id = %s where id = %s", (group_id, student_id))
db.commit()

subjects = ['speleology', 'mountaineering', 'natural science']
subject_ids = []

for subject in subjects:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", (subject,))
    subject_ids.append(cursor.lastrowid)
db.commit()

cursor.execute("""
    INSERT INTO lessons (title, subject_id) VALUES 
    ('speleology basics', %s), ('speleology practice', %s),
    ('mountaineering basics', %s), ('mountaineering practice', %s), 
    ('natural science basics', %s), ('natural science practice', %s)""", (
    subject_ids[0], subject_ids[0],
    subject_ids[1], subject_ids[1],
    subject_ids[2], subject_ids[2]))
db.commit()

cursor.execute("SELECT id FROM lessons WHERE subject_id IN (%s, %s, %s) ORDER BY id",
               (subject_ids[0], subject_ids[1], subject_ids[2]))
lesson_ids = [row[0] for row in cursor.fetchall()]

marks_data = [
    ('5', lesson_ids[0], student_id),
    ('5', lesson_ids[1], student_id),
    ('4', lesson_ids[2], student_id),
    ('5', lesson_ids[3], student_id),
    ('5', lesson_ids[4], student_id),
    ('5', lesson_ids[5], student_id)
]

cursor.executemany("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)", marks_data)
db.commit()

cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_id,))
marks = cursor.fetchall()
print(f"\n Оценки студента ID {student_id}:")
for mark in marks:
    print(f"  {mark}")

cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_id,))
books = cursor.fetchall()
print(f"\n Книги студента ID {student_id}:")
for book in books:
    print(f"  {book}")

query = '''
    SELECT 
        students.id as student_id, students.name, students.second_name,
        `groups`.title as group_title, `groups`.start_date, `groups`.end_date,
        books.title as book_title, marks.value as mark_value, lessons.title as lesson_title,
        subjects.title as subject_title
    FROM students
    JOIN books ON students.id = books.taken_by_student_id
    JOIN `groups` ON students.group_id = `groups`.id
    JOIN marks ON students.id = marks.student_id
    JOIN lessons ON marks.lesson_id = lessons.id
    JOIN subjects ON lessons.subject_id = subjects.id
    WHERE students.id = %s
'''

cursor.execute(query, (student_id,))
results = cursor.fetchall()

print(f"\nСтудент: {results[0]['name']} {results[0]['second_name']}")
print(f"Группа: {results[0]['group_title']} ({results[0]['start_date']} - {results[0]['end_date']})")

print("Книги:")
for row in results:
    book_title = row.get('book_title')
    print(f"{book_title}")

print("Оценки:")
for row in results:
    mark_value = row.get('lesson_title')
    print(f"{row['mark_value']} по предмету {row['subject_title']} (урок: {row['lesson_title']})")

db.close()
