from labs_7_9.domain.domain import Nota, Student, Disciplina, Data
from labs_7_9.repo.repository import StudentRepository, DisciplinaRepository, NotaRepository


class FileStudentRepository(StudentRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__file_name, "r") as file:
                for line in file:
                    attrs = line.strip().split(";")
                    if len(attrs) == 2:
                        student_id = int(attrs[0])
                        name = attrs[1]
                        student = Student(student_id, name)
                        StudentRepository.adaugare_student(self, student)
        except (FileNotFoundError, IOError) as e:
            print(f"Error loading from file: {e}")

    def __store_to_file(self):
        try:
            with open(self.__file_name, "w") as file:
                for student in self.get_all_students():
                    file.write(f"{student.getStudentId()};{student.getName()}\n")
        except (FileNotFoundError, IOError) as e:
            print(f"Error writing to file: {e}")

    def adaugare_student(self, student):
        super().adaugare_student(student)
        self.__store_to_file()

    def delete_student(self, student):
        std = super().delete_student(student)
        self.__store_to_file()
        return std

    def update_student(self, student):
        super().update_student(student)
        self.__store_to_file()

    def clean_up(self):
        self.students = {}
        self.__store_to_file()


class FileDisciplinaRepository(DisciplinaRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_from_file_discipline()

    def __load_from_file_discipline(self):
        try:
            with open(self.__file_name, "r") as file:
                for line in file:
                    attrs = line.strip().split(";")
                    if len(attrs) == 3:
                        disciplina_id = int(attrs[0])
                        name = attrs[1]
                        profesor = attrs[2]
                        disc = Disciplina(disciplina_id, name, profesor)
                        DisciplinaRepository.adaugare_disciplina(self, disc)
        except (FileNotFoundError, IOError) as e:
            print(f"Error loading from file: {e}")

    def __store_to_file_discipline(self):
        try:
            with open(self.__file_name, "w") as file:
                for disciplina in self.get_all_discipline():
                    file.write(f"{disciplina.getDisciplinaId()}" + "\n" +
                               f"{disciplina.getDisciplinaName()}" + "\n" +
                               f"{disciplina.getProfesor()}\n")
        except (FileNotFoundError, IOError) as e:
            print(f"Error writing to file: {e}")

    def adaugare_disciplina(self, disciplina):
        super().adaugare_disciplina(disciplina)
        self.__store_to_file_discipline()

    def update_disciplina(self, disciplina):
        super().update_disciplina(disciplina)
        self.__store_to_file_discipline()

    def delete_disciplina(self, disciplina_id):
        dsc = super().delete_disciplina(disciplina_id)
        self.__store_to_file_discipline()
        return dsc


class FileNotaRepository(NotaRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_from_file_note()

    def __load_from_file_note(self):
        try:
            with open(self.__file_name, "r") as file:
                for line in file:
                    attrs = line.strip().split(";")
                    if len(attrs) == 3:
                        valoare_nota = int(attrs[0])
                        student_id = int(attrs[1])
                        disciplina_id = int(attrs[2])
                        nota = Nota(valoare_nota, student_id, disciplina_id)
                        self.note.append(nota)
        except (FileNotFoundError, IOError) as e:
            print(f"Error loading from file: {e}")

    def __store_to_file_note(self):
        try:
            with open(self.__file_name, "w") as file:
                for nota in self.note:
                    file.write(f"{nota.getNotaValoare()};{nota.student_id()};{nota.disciplina_id()}\n")
        except (FileNotFoundError, IOError) as e:
            print(f"Error writing to file: {e}")

    def asignare_nota(self, nota):
        super().asignare_nota(nota)
        self.__store_to_file_note()

    def get_note_by_disciplina(self, disciplina):
        try:
            with open(self.__file_name, "r") as file:
                lista_note = []
                disciplina_id = disciplina.getDisciplinaId()
                for line in file:
                    attrs = line.strip().split(";")
                    if len(attrs) == 3:
                        valoare_nota = int(attrs[0])
                        student_id = int(attrs[1])
                        disciplina_id_2 = int(attrs[2])
                        nota = Nota(valoare_nota, student_id, disciplina_id_2)
                        if int(nota.disciplina_id()) == int(disciplina_id):
                            lista_note.append(nota)
                return lista_note
        except (FileNotFoundError, IOError) as e:
            print(f"Error loading from file: {e}")

    def get_all_from_all(self):
        try:
            with open(self.__file_name, "r") as file:
                lista_note = []
                for line in file:
                    attrs = line.strip().split(";")
                    if len(attrs) == 3:
                        valoare_nota = int(attrs[0])
                        student_id = int(attrs[1])
                        disciplina_id_2 = int(attrs[2])
                        nota = Nota(valoare_nota, student_id, disciplina_id_2)
                        lista_note.append(nota)
                return lista_note
        except (FileNotFoundError, IOError) as e:
            print(f"Error loading from file: {e}")

    def clean_up(self):
        self.note = []
        self.__store_to_file_note()


def test_get_note_by_disciplina():
    nota_disciplina = FileNotaRepository("test_note.txt")
    nota_disciplina.clean_up()
    nota_disciplina.asignare_nota(Nota(10, 1, 1))
    nota_disciplina.asignare_nota(Nota(9, 2, 2))
    nota_disciplina.asignare_nota(Nota(8, 1, 2))
    assert len(nota_disciplina.get_note_by_disciplina(Disciplina(2, "Romana", "Prof. Ionescu"))) == 2
    assert nota_disciplina.get_note_by_disciplina(Disciplina(2, "Romana", "Prof. Ionescu")) == [Nota(9, 2, 2), Nota(8, 1, 2)]


def test_get_all_from_all():
    nota_disciplina = FileNotaRepository("test_note.txt")
    nota_disciplina.clean_up()
    nota_disciplina.asignare_nota(Nota(10, 1, 1))
    nota_disciplina.asignare_nota(Nota(9, 2, 2))
    nota_disciplina.asignare_nota(Nota(8, 1, 2))
    assert len(nota_disciplina.get_all_from_all()) == 3


def test_studenti_fisier():
    student_repo = FileStudentRepository("test_studenti.txt")
    student_repo.clean_up()
    student_repo.adaugare_student(Student(1, "Andrei"))
    student_repo.adaugare_student(Student(2, "Alex"))
    student_repo.adaugare_student(Student(3, "Andrei"))
    assert student_repo.size() == 3
    student_repo.delete_student(Student(1, "Andrei"))
    assert student_repo.size() == 2
    student_repo.update_student(Student(2, "Andrei"))


test_studenti_fisier()
test_get_note_by_disciplina()
test_get_all_from_all()
