from labs_7_9.domain.domain import Student, Disciplina, Nota


class StudentValidation:
    @staticmethod
    def eroare_student(student):
        errors = []
        if int(student.getStudentId()) < 0:
            errors.append("ID-ul studentului nu poate fi negativ!")
        if student.getName() == "":
            errors.append("Numele studentului nu poate fi vid!")
        if len(student.getName()) > 50:
            errors.append("Numele studentului nu poate avea mai mult de 50 de caractere!")
        if len(errors) > 0:
            raise ValueError(errors)


class DisciplinaValidation:
    @staticmethod
    def eroare_disciplina(disciplina):
        errors = []
        if int(disciplina.getDisciplinaId()) < 0:
            errors.append("ID-ul disciplinei nu poate fi negativ!")
        if not disciplina.getDisciplinaName():
            errors.append("Numele disciplinei nu poate fi vid!")
        if len(disciplina.getDisciplinaName()) > 50:
            errors.append("Numele disciplinei nu poate avea mai mult de 50 de caractere!")
        if not disciplina.getProfesor():
            errors.append("Numele profesorului nu poate fi vid!")
        if len(errors) > 0:
            raise ValueError(errors)


class NoteValidation:
    @staticmethod
    def eroare_nota(nota):
        errors = []
        if int(nota.getNotaValoare()) < 0 or int(nota.getNotaValoare()) > 10:
            errors.append("Nota trebuie sa fie intre 0 si 10!")
        if len(errors) > 0:
            raise ValueError(errors)


def test_student_validation():
    student = Student(-1, "")
    try:
        StudentValidation.eroare_student(student)
        assert False
    except ValueError:
        assert True


def test_disciplina_validation():
    disciplina = Disciplina(-1, "", "")
    try:
        DisciplinaValidation.eroare_disciplina(disciplina)
        assert False
    except ValueError:
        assert True


def test_nota_validation():
    nota = Nota(-1, -1, -1)
    try:
        NoteValidation.eroare_nota(nota)
        assert False
    except ValueError:
        assert True


test_student_validation()
test_disciplina_validation()
test_nota_validation()
