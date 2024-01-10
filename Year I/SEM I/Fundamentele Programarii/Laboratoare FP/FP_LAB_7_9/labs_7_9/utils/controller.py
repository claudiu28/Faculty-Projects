from labs_7_9.domain.domain import Student, Disciplina, Nota, Data
import random


class ServiceStudent:
    # optiuni de baza student (create, delete, update, find)
    def __init__(self, validation, repository):
        self.validator = validation
        self.repository = repository

    def adaugare_student_service_student(self, student_id, student_name):
        student = Student(student_id, student_name)
        if not self.validator.eroare_student(student):
            self.repository.adaugare_student(student)
        else:
            raise ValueError("Studentul nu poate fi adaugat!")

    def delete_student_service_student(self, student_id):
        student = Student(student_id, None)
        if int(student_id) >= 0:
            self.repository.delete_student(student)
        else:
            raise ValueError("Studentul nu poate fi sters!")

    def update_student_service_student(self, student_id, student_name):
        student = Student(student_id, student_name)
        if not self.validator.eroare_student(student):
            self.repository.update_student(student)
        else:
            raise ValueError("Studentul nu poate fi modificat!")

    def find_student_service_student(self, student_id, index=0):
        students = self.repository.get_all_students()  # lista de studenti

        if index >= len(students):
            raise ValueError("Studentul nu poate fi gasit!")

        if students[index].getStudentId() == student_id:
            return students[index]

        return self.find_student_service_student(student_id, index + 1)

    def get_all_students_srv(self):
        return self.repository.get_all_students()

    def random_student(self, numar):
        if numar == 0:
            return

        minim = 1
        maxim = 100
        id_aleator = random.randint(minim, maxim)
        caractere_posibile = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lungime_sir = 10

        nume_aleatoriu = ''.join(random.choice(caractere_posibile) for _ in range(lungime_sir))
        if id_aleator not in self.get_all_students_srv():
            self.adaugare_student_service_student(id_aleator, nume_aleatoriu)

        self.random_student(numar - 1)


class ServiceDiscipline:
    # optiuni de baza discipline (create, delete, update)
    def __init__(self, valid, repository):
        self.validator = valid
        self.repository = repository

    def adaugare_disciplina_service(self, discipline_id, discipline_name, profesor):
        disciplina = Disciplina(discipline_id, discipline_name, profesor)
        if not self.validator.eroare_disciplina(disciplina):
            self.repository.adaugare_disciplina(disciplina)
        else:
            raise ValueError("Disciplina nu poate fi adaugata!")

    def delete_discipline_service(self, discipline_id):
        discipline = Disciplina(discipline_id, None, None)
        if int(discipline_id) >= 0:
            self.repository.delete_disciplina(discipline)
        else:
            raise ValueError("Disciplina nu poate fi stearsa!")

    def update_discipline_service(self, discipline_id, discipline_name, profesor):
        discipline = Disciplina(discipline_id, discipline_name, profesor)
        if not self.validator.eroare_disciplina(discipline):
            self.repository.update_disciplina(discipline)
        else:
            raise ValueError("Disciplina nu poate fi modificata!")

    def find_discipline_service(self, discipline_id):
        discipline = Disciplina(discipline_id, None, None)
        if int(discipline_id) >= 0:
            return self.repository.find_disciplina(discipline)
        else:
            raise ValueError("Disciplina nu poate fi gasita!")

    def get_all_discipline_service(self):
        return self.repository.get_all_discipline()


class ServiceNote:
    def __init__(self, validator, repository, repo_student, repo_disciplina):
        self.validator = validator
        self.repository = repository
        self.repo_disciplina = repo_disciplina
        self.repo_student = repo_student

    def asignare_nota_service(self, nota_valoare, student_id, disciplina_id):
        nota = Nota(nota_valoare, student_id, disciplina_id)
        if self.validator.eroare_nota(nota):
            raise ValueError("Datele notei nu sunt valide.")
        self.repository.asignare_nota(nota)

    def sorted_by_nota(self, discipline_id):

        final = []
        lista = self.repository.get_note_by_disciplina(Disciplina(discipline_id, None, None))

        for element in lista:
            student_id = element.student_id()
            student = self.repo_student.find_student(Student(student_id, None))
            if student is not None:
                final.append(Data(discipline_id, student, element))
        final_f = sorted(final, key=lambda x: (-x.get_nota().getNotaValoare(), x.get_student_name()), reverse=True)
        return final_f

    def sorted_by_nume(self, discipline_id):
        final = []
        lista = self.repository.get_note_by_disciplina(Disciplina(discipline_id, None, None))
        for element in lista:
            student_id = element.student_id()
            student = self.repo_student.find_student(Student(student_id, None))
            if student is not None:
                final.append(Data(discipline_id, student, element))
        final = sorted(final, key=lambda x: x.get_student_name(), reverse=False)
        return final

    def top20(self):
        sume_note = {}
        numar_note = {}

        lista = self.repository.get_all_from_all()
        for element in lista:
            student_id = element.student_id()
            nota_valoare = element.getNotaValoare()
            sume_note.setdefault(student_id, 0)
            numar_note.setdefault(student_id, 0)
            sume_note[student_id] += nota_valoare
            numar_note[student_id] += 1

        medii = {student_id: suma / numar_note[student_id] for student_id, suma in sume_note.items()}
        medii_list = list(medii.items())

        medii_sortate = sorted(medii_list, key=lambda x: x[1], reverse=True)

        numar_top = max(1, int(len(medii_sortate) * 0.20))
        top_20 = medii_sortate[:numar_top]
        final = []
        for student_id, medie in top_20:
            student = self.repo_student.find_student(Student(student_id, None))
            if student:
                student.setName(student.getName())
                final.append(Data(None, student, Nota(medie, None, None)))
        return final
