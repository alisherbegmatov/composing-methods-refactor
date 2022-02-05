# By Kamran Bigdely Nov. 2020
# Replace temp variable with a aquery

# TODO: Use the 'extract method' refactoring technique to improve this code.
# TODO: If required, use the 'replace temp variable with the query' technique to make it easier to extract methods.

class Employer:
    def __init__(self, name):
        self.name = name

    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')


class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")


class School:
    def __init__(self, students) -> None:
        self.students = students
        self.min_gpa = 2.5  # minimum acceptable GPA
        self.passed_students = []
        # Find the students in the school who have successfully graduated.
        self.get_graduated_Student()

    def process_graduation(self):
        self.print_graduated_Student()
        self.send_congrat_email()
        self.connect_top_employers()

    def get_graduated_Student(self):
        for s in self.students:
            if s.get_gpa() > self.min_gpa:
                self.passed_students.append(s)

    def print_graduated_Student(self):
        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for s in self.passed_students:
            print(s.name)
        print('****************************')

    def send_congrat_email(self):
        # Send congrat emails to them.
        for s in self.passed_students:
            s.send_congrat_email()

    def get_top_10_students(self):
        # Find the top 10% of them and send their contact to the top employers
        self.passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(self.passed_students))
        top_10_percent = self.passed_students[index:]

    def connect_top_employers(self):
        top_10_percent = self.get_top_10_students()
        top_employers = [Employer('Microsoft'), Employer(
            'Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)


students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2, 'kami'), Student(3, 'sarah')]
school = School(students)
school.process_graduation()
