CREATE TABLE Classes (id serial PRIMARY KEY, name varchar(50) NOT NULL UNIQUE);

CREATE TABLE Students (id serial PRIMARY KEY, name varchar(50) NOT NULL, age int CHECK (age >=6 AND age <=18),
						class_id int NOT NULL REFERENCES Classes (id) ON DELETE CASCADE);
					
CREATE TABLE Subjects (id serial PRIMARY KEY, name varchar(50) NOT NULL UNIQUE);

CREATE TABLE Teachers (id serial PRIMARY KEY, name varchar(50) NOT NULL, 
					   subject_id int NOT NULL REFERENCES Subjects (id) ON DELETE CASCADE);

CREATE TABLE Grades (id serial PRIMARY KEY, student_id int NOT NULL REFERENCES Students(id) ON DELETE CASCADE,
					subject_id int NOT NULL REFERENCES Subjects (id) ON DELETE CASCADE,
					 grade int NOT NULL CHECK (grade>=1 AND grade<=10), letter varchar(1) NOT NULL CHECK (letter ~ '^[a-z]'));
					 
CREATE TABLE Marks (id serial PRIMARY KEY, student_id int NOT NULL REFERENCES Students(id) ON DELETE CASCADE,
					subject_id int NOT NULL REFERENCES Subjects(id) ON DELETE CASCADE, mark int NOT NULL);
				


INSERT INTO Classes (name) VALUES ('Mathematics class'), ('English class'), ('Physical Education class'),
('Computer Science class'), ('Foreign Languages class');

INSERT INTO Students (name, age, class_id)
VALUES ('Alice', 9, 4), ('David', 12, 1), ('Emma', 7, 3), ('Grace', 11, 2), ('James', 8, 3), ('Lily', 15, 1), ('Matthew', 10, 4),
('Olivia', 14, 5), ('Sophia', 13, 2), ('William', 18, 1);

INSERT INTO Subjects (name) 
VALUES ('Mathematics'), ('Science'), ('History'), ('English'), ('Physical Education'), ('Art'), ('Music'), 
('Geography'), ('Computer Science'), ('Foreign Languages');

INSERT INTO Teachers (name, subject_id)
VALUES ('Alice Johnson', 3), ('David Smith', 6), ('Alice Johnson', 8), ('James Brown', 2), ('Lily Parker', 7),
('Matthew Cooper', 10), ('David Smith', 5), ('Alice Johnson', 1), ('David Smith', 4), ('Lily Parker', 9);

INSERT INTO Grades (student_id, subject_id, grade, letter)
VALUES (3, 6, 8, 'a'), (7, 2, 5, 'b'), (1, 9, 3, 'c'), (5, 4, 1, 'a'), (2, 8, 7, 'c'), (9, 3, 9, 'b'), (8, 7, 9, 'b'),
(6, 5, 6, 'a'), (4, 1, 10, 'a'), (10, 10, 10, 'a');

INSERT INTO Marks (student_id, subject_id, mark)
VALUES (3, 7, 2), (1, 9, 8), (5, 4, 7), (2, 8, 3), (6, 5, 8),
 (9, 3, 6), (8, 7, 10), (4, 1, 5), (10, 6, 3), (7, 2, 9),
 (4, 8, 1), (1, 3, 5), (6, 9, 2), (3, 7, 6), (8, 4, 10),
 (5, 10, 4), (2, 6, 7), (7, 1, 10), (9, 5, 1), (10, 2, 4);
 


CREATE INDEX idx_students_name ON Students(name);
CREATE INDEX idx_teachers_name ON Teachers(name);
CREATE INDEX idx_subjects_name ON Subjects(name);
CREATE INDEX idx_grades_students_id ON Grades(student_id);
CREATE INDEX idx_grades_subjects_id ON Grades(subject_id);
CREATE INDEX idx_classes_name ON Classes(name);


SELECT name, age
FROM Students AS s
JOIN Grades AS g ON  s.id = g.student_id
WHERE g.grade=10 AND g.letter = 'a';

SELECT t.name AS teacher, s.name AS subject
FROM Teachers AS t
JOIN Subjects AS s ON t.subject_id = s.id 
WHERE s.name IN ('Mathematics','Physical Education');

SELECT s.name AS student, AVG(m.mark) AS Average_mark
FROM Students AS s
JOIN Marks AS m ON s.id = m.student_id 
GROUP BY s.name
ORDER BY AVG(m.mark);

SELECT stu.name, m.mark 
FROM Marks AS m
JOIN Students AS stu ON m.student_id = stu.id
JOIN Subjects AS sub ON m.subject_id  = sub.id
WHERE sub.name = 'English' AND m.mark = (SELECT max(m.mark) FROM Marks AS m, Subjects WHERE Subjects.name = 'English')
GROUP BY stu.name, m.mark;

SELECT t.name AS teacher, COUNT(DISTINCT t.subject_id) AS num_subjects
FROM Teachers AS t
JOIN Subjects AS s ON t.subject_id = s.id
GROUP BY t.name
HAVING COUNT(DISTINCT t.subject_id) > 1;

SELECT s.name AS student, s.class_id AS CLASS
FROM Students AS s
WHERE s.class_id = (SELECT s.class_id FROM Students AS s WHERE s.name = 'David') AND s.name != 'David';

SELECT c.name AS class, COUNT(s.name)
FROM Students AS s
JOIN Classes AS c ON s.class_id = c.id
GROUP BY c.name;  

SELECT s.name
FROM Marks AS m
LEFT JOIN Subjects AS s ON m.subject_id = s.id
GROUP BY s.name
HAVING COUNT(m.subject_id)=0;

