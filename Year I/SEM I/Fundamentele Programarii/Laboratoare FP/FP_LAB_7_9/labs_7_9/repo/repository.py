from labs_7_9.domain.domain import Data, Student, Disciplina, Nota


class StudentRepository:
    def __init__(self):
        self.students = {}

    def adaugare_student(self, student):
        student_id = student.getStudentId()
        if student_id in self.students:
            raise ValueError("Studentul este deja introdus!")
        self.students[student_id] = student

    def update_student(self, student):
        student_id = student.getStudentId()
        if student_id not in self.students:
            raise ValueError("Studentul nu poate fi modificat!")
        self.students[student_id].setName(student.getName())

    def delete_student(self, student):
        student_id = student.getStudentId()
        if student_id not in self.students:
            raise ValueError("Studentul nu poate fi sters!")
        del self.students[student_id]

    def find_student(self, student):
        student_id = student.getStudentId()
        if student_id not in self.students:
            raise ValueError("Studentul nu poate fi gasit!")
        return self.students[student_id]

    def get_all_students(self):
        return list(self.students.values())

    def size(self):
        return len(self.students)


def test_student_repo_memory():

    stundet_repo = StudentRepository()
    assert stundet_repo.size() == 0
    student = Student(1, "Andrei")
    stundet_repo.adaugare_student(student)
    assert stundet_repo.size() == 1
    student_secund = Student(2, "Alex")
    stundet_repo.adaugare_student(student_secund)
    assert stundet_repo.size() == 2
    stundet_repo.delete_student(Student(1, "Andrei"))
    student_trei = Student(3, "Ion")
    stundet_repo.adaugare_student(student_trei)
    assert stundet_repo.size() == 2
    stundet_repo.update_student(Student(2, "Nelu"))
    assert stundet_repo.find_student(Student(2, "Nelu")) == stundet_repo.get_all_students()[0]
    assert len(stundet_repo.get_all_students()) == 2


test_student_repo_memory()


class DisciplinaRepository:
    def __init__(self):
        self.discipline = {}

    def adaugare_disciplina(self, disciplina):
        disciplina_id = disciplina.getDisciplinaId()
        if disciplina_id in self.discipline:
            raise ValueError("Disciplina este deja introdusa!")
        self.discipline[disciplina_id] = disciplina

    def update_disciplina(self, disciplina):
        disciplina_id = disciplina.getDisciplinaId()
        if disciplina_id not in self.discipline:
            raise ValueError("Disciplina nu poate fii modificata!")
        self.discipline[disciplina_id].setDisciplinaName(disciplina.getDisciplinaName())
        self.discipline[disciplina_id].setProfesor(disciplina.getProfesor())

    def delete_disciplina(self, disciplina):
        disciplina_id = disciplina.getDisciplinaId()
        if disciplina_id not in self.discipline:
            raise ValueError("Disciplina nu poate fii stearsa!")
        del self.discipline[disciplina_id]

    def find_disciplina(self, disciplina):
        disciplina_id = disciplina.getDisciplinaId()
        if disciplina_id not in self.discipline:
            raise ValueError("Disciplina nu poate fii gasita!")
        return self.discipline[disciplina_id]

    def get_all_discipline(self):
        return list(self.discipline.values())

    def size(self):
        return len(self.discipline)


def test_disciplina_repo_memory():
    disciplina_repo = DisciplinaRepository()
    disciplina = Disciplina("1", "Matematica", "Prof. Popescu")
    disciplina_repo.adaugare_disciplina(disciplina)
    assert disciplina_repo.size() == 1
    disciplina_secunda = Disciplina("2", "Romana", "Prof. Ionescu")
    disciplina_repo.adaugare_disciplina(disciplina_secunda)
    assert disciplina_repo.size() == 2
    disciplina_repo.update_disciplina(Disciplina("2", "FP", "Prof. Alin"))
    assert (disciplina_repo.find_disciplina(Disciplina("2", "FP", "Prof. Alin")) ==
            disciplina_repo.get_all_discipline()[1])
    assert len(disciplina_repo.get_all_discipline()) == 2
    disciplina_repo.delete_disciplina(Disciplina("2", "FP", "Prof. Alin"))
    assert disciplina_repo.size() == 1
    assert len(disciplina_repo.get_all_discipline()) == 1


test_disciplina_repo_memory()


class NotaRepository:
    def __init__(self):
        self.note = []

    def find_note(self, student_id, disciplina_id):
        for nota in self.note:
            if nota.student_id() == student_id and nota.disciplina_id() == disciplina_id:
                return nota
        return None

    def asignare_nota(self, nota):
        if self.find_note(nota.student_id(), nota.disciplina_id()) is not None:
            raise AttributeError("Nota exista deja pentru acest student!")
        return self.note.append(nota)

    def size(self):
        return len(self.note)

    def get_note_by_disciplina(self, disciplina):
        disciplina_id = disciplina.getDisciplinaId()
        for nota in self.note:
            if nota.disciplina_id() == disciplina_id:
                return nota

    def get_all_from_all(self):
        lista_note = []
        for nota in self.note:
            gr = Nota(int(nota.disciplina_id()), int(nota.student_id()), int(nota.getNotaValoare()))
            lista_note.append(gr)
        return lista_note


def test_nota_repo_memory():
    nota_repo = NotaRepository()
    nota = Nota(10, 1, 1)
    nota_repo.asignare_nota(nota)
    assert nota_repo.size() == 1
    nota_secunda = Nota(9, 2, 2)
    nota_repo.asignare_nota(nota_secunda)
    assert nota_repo.size() == 2
    nota_trei = Nota(8, 1, 2)
    nota_repo.asignare_nota(nota_trei)
    assert nota_repo.size() == 3
    assert nota_repo.get_note_by_disciplina(Disciplina(2, "Romana", "Prof. Ionescu")) == nota_secunda
    assert len(nota_repo.get_all_from_all()) == 3


test_nota_repo_memory()

