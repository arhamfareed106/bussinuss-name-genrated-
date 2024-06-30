class Student:
    def __init__(self, roll_number, name,class_name ):
        self.roll_number = roll_number
        self.name= name
        self.class_name= class_name
        self.marks={}
    def add_marks(self,subject, marks):
        if subject in self.marks:
            print(f"{subject} already has marks of {subject}")
        else:
            self.marks[subject]= marks        
    def calculate_avarge_marks(self):   
            if not self.marks:
             print("no marks")
            total_marks = sum(self.marks.values())
            avarage_marks = total_marks/len(self.marks)
            return avarage_marks 
    def display_studen_info(self):
        print(f"student information")
        print(f"roll number: {self.roll_number }")
        print(f"name: {self.name}")
        print(f"class: {self.class_name}")
        print(f"marks: {self.marks}")       
        print(f"avarge marks are:{self.calculate_avarge_marks()}")

student1 = Student(1, "musa", 10)
student2 = Student(2, "ali", 9)    
student1.add_marks("math", 45)
student1.add_marks("english", 55)

student2.add_marks("math", 87)
student2.add_marks("english", 76)

student2.display_studen_info()
student1.display_studen_info()