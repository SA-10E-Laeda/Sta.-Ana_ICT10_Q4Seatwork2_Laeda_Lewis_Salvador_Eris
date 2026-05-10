from pyscript import document
from pyscript import window

class Student:
    def __init__(self, name, age, section, subject, class_num):
        self.name = name
        self.age = age
        self.section = section
        self.subject = subject
        self.class_num = class_num
    
    def present(self):
        return f"<div class='card mb-3' style='background-color: #ece6c7;'><div class='card-body'>{self.name} (Age: {self.age}) - Section: {self.section}, Subject: {self.subject}, Class #: {self.class_num}</div></div>"
    

students = [
    Student("Julian Casablancas", "47", "10-E", "Music", 1),
    Student("Maryam Mirzakhani", "45", "10-R", "Mathematics", 2),
    Student("Vladimir Nabokov", "82", "10-E", "English", 3),
    Student("Cecilia Payne", "90", "10-R", "Science", 4),
    Student("E.M. Rose", "78", "10-E", "History", 5),
    Student("Venus Williams", "40", "10-R", "PE", 6)
]

def display_students():
    output = document.getElementById("output")
    output.innerHTML = ""

    for student in students:
        new_entry = document.createElement("div")
        new_entry.className = "border rounded p-2 mb-2"
        new_entry.innerHTML = student.present()
        output.appendChild(new_entry)

def class_exists(class_num):
    for student in students:
        if student.class_num == class_num:
            return True
    return False

def add_student(event=None):
    # Prevent page reload (safe even if event is None)
    if event:
        event.preventDefault()

    name = document.getElementById("name").value
    age = document.getElementById("age").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value
    class_num = document.getElementById("classNum").value

    if not name or not age or not section or not subject or not class_num:
        window.alert("Please fill in all fields!")
        return
    
    if class_exists(class_num):
        window.alert("This Class number already exists!")
        return


    students.append(Student(name, age, section, subject, class_num))
    

    display_students()

    output = document.getElementById("output")

    # Create a new div element instead of using innerHTML += (more stable)
    new_entry = document.createElement("div")
    new_entry.className = "border rounded p-2 mb-2"
    new_entry.innerHTML = f"""
        <strong>{name}</strong> (Age: {age})<br>
        Section: {section}<br>
        Subject: {subject}<br>
        Class #: {class_num}
    """

    display_students()

    output.appendChild(new_entry)

    # Clear inputs
    document.getElementById("name").value = ""
    document.getElementById("age").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""
    document.getElementById("classNum").value = ""

    display_students()