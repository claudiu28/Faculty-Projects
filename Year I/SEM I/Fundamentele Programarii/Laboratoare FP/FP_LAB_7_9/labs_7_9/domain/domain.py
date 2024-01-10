class Student:
    def __init__(self, studentid, name):
        self.__name = name
        self.__studentId = studentid

    def getName(self):
        return self.__name

    def getStudentId(self):
        return self.__studentId

    def setName(self, name):
        self.__name = name

    def __le__(self, other):
        return self.__name <= other.getStudentId()

    def __repr__(self):
        return f"Student id: {self.__studentId}, student name: {self.__name};"


class Disciplina:
    def __init__(self, disciplinaid, name, profesor):
        self.__disciplinaId = disciplinaid
        self.__Disciplinaname = name
        self.__profesor = profesor

    def getDisciplinaId(self):
        return self.__disciplinaId

    def getDisciplinaName(self):
        return self.__Disciplinaname

    def getProfesor(self):
        return self.__profesor

    def setProfesor(self, profesor):
        self.__profesor = profesor

    def setDisciplinaName(self, name):
        self.__Disciplinaname = name

    def __repr__(self):
        return f"disciplinaId: {self.__disciplinaId}, Disciplinaname: {self.__Disciplinaname}, Profesor: {self.__profesor}"


class Nota:
    def __init__(self, valoare_nota, student_id, disciplina_id):
        self.__valoare_nota = valoare_nota
        self.__student_id = student_id
        self.__disciplina_id = disciplina_id

    def getNotaValoare(self):
        return self.__valoare_nota

    def student_id(self):
        return self.__student_id

    def disciplina_id(self):
        return self.__disciplina_id

    def __lt__(self, other):
        return self.__valoare_nota <= other.getNotaValoare()

    def __eq__(self, other):
        return self.__student_id == other.student_id() and self.__disciplina_id == other.disciplina_id()


class Data:
    def __init__(self, disciplina_id, student, nota):
        self.__disciplina_id = disciplina_id
        self.__student = student
        self.__nota = nota
        self.__name = None

    def get_student(self):
        return self.__student.getStudentId()

    def get_disciplina_id(self):
        return self.__disciplina_id

    def get_nota(self):
        return self.__nota

    def get_student_name(self):
        return self.__student.getName()

    def set_name_student(self, name):
        self.__name.setName(name)

    def __lt__(self, other):
        return self.__nota <= other.get_nota()

    def __repr__(self):
        return f"Disciplina id: {self.__disciplina_id}, student: {self.__student}, nota: {self.__nota}"


def test_student():
    student = Student(1, "Andrei")
    assert student.getStudentId() == 1
    assert student.getName() == "Andrei"

    student.setName("Alex")
    assert student.getName() == "Alex"


def test_disciplina():
    disciplina = Disciplina(2, "Matematica", "Prof. Popescu")
    assert disciplina.getDisciplinaId() == 2
    assert disciplina.getDisciplinaName() == "Matematica"
    assert disciplina.getProfesor() == "Prof. Popescu"

    disciplina.setProfesor("Prof. Popescu")
    assert disciplina.getProfesor() == "Prof. Popescu"


def test_nota():
    nota = Nota(10, 1, 2)
    assert nota.getNotaValoare() == 10
    assert nota.student_id() == 1
    assert nota.disciplina_id() == 2


def test_data():
    student = Student(1, "Alex")
    disciplina = Disciplina(2, "Matematica", "Prof. Popescu")
    nota = Nota(10, 1, 2)

    data = Data(2, student, nota)
    assert data.get_student() == 1
    assert data.get_disciplina_id() == 2
    assert data.get_nota() == nota
    assert data.get_student_name() == "Alex"


test_student()
test_disciplina()
test_nota()
test_data()
