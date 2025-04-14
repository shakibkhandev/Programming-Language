# Python Inheritance Crash Course
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent/Base class: The class being inherited from
# Child/Derived class: The class that inherits from another class

# Parent Class Definition
class Person:
    def __init__(self, fname, lname, age):
        """
        Initialize Person class with basic attributes
        Args:
            fname (str): First name of the person
            lname (str): Last name of the person
            age (int): Age of the person
        """
        self.firstname = fname
        self.lastname = lname
        self.age = age
    
    def get_full_name(self):
        """Return the full name of the person"""
        return f"{self.firstname} {self.lastname}"
    
    def introduce(self):
        """Method to introduce the person"""
        return f"Hi, I'm {self.get_full_name()} and I'm {self.age} years old."

# Child Class Definition
class Student(Person):
    def __init__(self, fname, lname, age, student_id, major):
        """
        Initialize Student class with Person attributes plus student-specific ones
        Args:
            fname (str): First name of the student
            lname (str): Last name of the student
            age (int): Age of the student
            student_id (str): Student's ID number
            major (str): Student's major field of study
        """
        # Call parent class's __init__ using super()
        super().__init__(fname, lname, age)
        # Add Student-specific attributes
        self.student_id = student_id
        self.major = major
        self.courses = []  # List to store enrolled courses
    
    def enroll_course(self, course):
        """
        Enroll student in a course
        Args:
            course (str): Name of the course
        """
        self.courses.append(course)
        print(f"{self.get_full_name()} has enrolled in {course}")
    
    # Override parent's introduce method
    def introduce(self):
        """Override the parent's introduce method with student-specific introduction"""
        return f"Hi, I'm {self.get_full_name()}, a {self.major} major with ID: {self.student_id}"

# Child Class of Student (Multi-level inheritance)
class GraduateStudent(Student):
    def __init__(self, fname, lname, age, student_id, major, research_topic):
        """
        Initialize GraduateStudent with Student attributes plus grad-specific ones
        Args:
            fname (str): First name of the graduate student
            lname (str): Last name of the graduate student
            age (int): Age of the graduate student
            student_id (str): Student's ID number
            major (str): Student's major field of study
            research_topic (str): Graduate research topic
        """
        super().__init__(fname, lname, age, student_id, major)
        self.research_topic = research_topic
        self.is_teaching = False
    
    def assign_teaching(self, is_teaching=True):
        """Assign or remove teaching duties"""
        self.is_teaching = is_teaching
        status = "assigned to" if is_teaching else "removed from"
        print(f"{self.get_full_name()} has been {status} teaching duties")

# Example Usage
if __name__ == "__main__":
    # Create a basic person
    person = Person("John", "Doe", 30)
    print("\nPerson Example:")
    print(person.introduce())
    
    # Create a student
    student = Student("Alice", "Smith", 20, "ST123", "Computer Science")
    print("\nStudent Example:")
    print(student.introduce())
    student.enroll_course("Python Programming")
    student.enroll_course("Data Structures")
    print(f"Enrolled courses: {', '.join(student.courses)}")
    
    # Create a graduate student
    grad_student = GraduateStudent("Bob", "Johnson", 25, "GS456", "AI", "Machine Learning")
    print("\nGraduate Student Example:")
    print(grad_student.introduce())
    grad_student.enroll_course("Advanced AI")
    grad_student.assign_teaching(True)
    print(f"Research Topic: {grad_student.research_topic}")
