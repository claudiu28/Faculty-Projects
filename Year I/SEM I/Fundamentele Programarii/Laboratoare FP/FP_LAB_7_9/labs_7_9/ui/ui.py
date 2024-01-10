class Consola:
    def __init__(self, srv, serv, sern):
        self.__srv = srv
        self.__serv = serv
        self.__sern = sern

    def add(self):
        id_student = int(input("Introduceti id-ul: "))
        name = input("Introduceti numele: ")
        try:
            self.__srv.adaugare_student_service_student(id_student, name)
            print("Studentul a fost adaugat cu succes!")
        except ValueError as e:
            print("Eroarea: ", e)

    def delete(self):
        id_student = int(input("Introduceti id-ul: "))
        try:
            self.__srv.delete_student_service_student(id_student)
            print("Studentul a fost sters cu succes!")
        except ValueError as e:
            print("Eroarea: ", e)

    def update(self):
        id_student = int(input("Introduceti id-ul: "))
        name = input("Introduceti numele pe care il doriti: ")
        try:
            self.__srv.update_student_service_student(id_student, name)
            print("Studentul a fost modificat cu succes!")
        except ValueError as e:
            print("Eroarea: ", e)

    def show(self):
        try:
            print("Lista studentilor:\n")
            for student in self.__srv.get_all_students_srv():
                print(("Student id:", student.getStudentId(), "student name:", student.getName()))
        except AttributeError as e:
            print(e)

    def find(self):
        id_student = int(input("Introduceti id-ul dupa care cautati: "))
        try:
            student = self.__srv.find_student_service_student(id_student)
            print("Studentul cautat este: ", student, "\n")
            print("Studentul a fost gasit cu succes!")

        except ValueError as e:
            print("Eroarea: ", e)

    def add_discipline(self):
        id_discipline = int(input("Introduceti id-ul: "))
        name = input("Introduceti numele: ")
        profesor = input("Introduceti profesorul: ")
        try:
            self.__serv.adaugare_disciplina_service(id_discipline, name, profesor)
            print("Disciplina a fost adaugata cu succes!")
        except ValueError as e:
            print("Eroarea: ", e)

    def delete_discipline(self):
        id_discipline = int(input("Introduceti id-ul: "))
        try:
            self.__serv.delete_discipline_service(id_discipline)
            print("Disciplina a fost stearsa cu succes!")
        except ValueError as e:
            print("Eroarea: ", e)

    def update_discipline(self):
        id_discipline = int(input("Introduceti id-ul: "))
        name = input("Introduceti numele: ")
        profesor = input("Introduceti profesorul: ")
        try:
            self.__serv.update_discipline_service(id_discipline, name, profesor)
            print("Disciplina a fost modificata cu succes!")
        except ValueError as e:
            print("Eroarea: ", e)

    def show_discipline(self):
        try:
            print("Lista disciplinelor: \n")
            discipline = self.__serv.get_all_discipline_service()
            for names in discipline:
                print("(Id-ul disciplinei:", names.getDisciplinaId(), "nume disciplinei:", names.getDisciplinaName(),
                      "profesor:", names.getProfesor(), ")")
        except AttributeError as e:
            print(e)

    def find_discipline_ui(self):
        id_discipline = int(input("Introduceti id-ul dupa care cautati: "))
        try:
            disciplina_gasita = self.__serv.find_discipline_service(id_discipline)
            print("Disciplina cautata este: ", disciplina_gasita, "\n")
        except ValueError as e:
            print("Eroarea: ", e)

    def adaugare_nota(self):
        nota = int(input("Introduceti nota: "))
        id_student = int(input("Introduceti id-ul studentului: "))
        id_disciplina = int(input("Introduceti id-ul disciplinei: "))
        try:
            self.__sern.asignare_nota_service(nota, id_student, id_disciplina)
            print("Nota a fost adaugata cu succes!")
        except ValueError as e:
            print("Eroarea: ", e)

    def random_fct(self):
        try:
            n = int(input("Numaru de studenti aleatori: "))
            self.__srv.random_student(n)
            print("A fost adaugata cu succes!!!")
        except ValueError as e:
            print(e)

    def sort_by_note(self):
        try:
            id_disciplina = int(input("Introduceti id disciplinei: "))
            print("Lista notelor: \n")
            note_studenti = self.__sern.sorted_by_nota(id_disciplina)
            for names in note_studenti:
                print("(Nota:", names.get_nota().getNotaValoare(), "Numele studentului:", names.get_student_name(), ")")
        except AttributeError as e:
            print(e)

    def sort_by_nume(self):
        try:
            id_disciplina = int(input("Introduceti id-ul disciplinei: "))
            print("Lista notelor: \n")
            note_studenti = self.__sern.sorted_by_nume(id_disciplina)
            for names in note_studenti:
                print("(Nota:", names.get_nota().getNotaValoare(), "Numele studentului:", names.get_student_name(), ")")
        except AttributeError as e:
            print(e)

    def top20(self):
        try:
            print("Lista notelor: \n")
            note_studenti = self.__sern.top20()
            for names in note_studenti:
                print("(Nota:", names.get_nota().getNotaValoare(), "Numele studentului:", names.get_student_name(), ")")
        except AttributeError as e:
            print(e)

    def meniu(self):
        while True:

            print("Optinuile disponibile sunt: \n"
                  "Student: \n"
                  "     1. add_student;\n"
                  "     2. delete_student;\n"
                  "     3. update_student;\n"
                  "     4. show_students;\n"
                  "     5. find_students(recursiv);\n"
                  "     6. random_fct(recursiv);\n"
                  "Nota: \n"
                  "     1. add_nota; \n"
                  "     2. ordine_nota \n"
                  "     3. ordine_nume \n"
                  "     4. 20% din copii (command: top) \n"
                  "Disciplina: \n"
                  "     1. add_discipline;\n"
                  "     2. delete_discipline;\n"
                  "     3. update_discipline;\n"
                  "     4. show_discipline;\n"
                  "     5. find_discipline;\n"
                  "x. exit;\n"
                  "")
            optiune = input("Introduceti optiunea: ")
            if optiune == "add_student":
                self.add()
            elif optiune == "delete_student":
                self.delete()
            elif optiune == "update_student":
                self.update()
            elif optiune == "show_students":
                self.show()
            elif optiune == "find_students":
                self.find()
            elif optiune == "add_discipline":
                self.add_discipline()
            elif optiune == "delete_discipline":
                self.delete_discipline()
            elif optiune == "update_discipline":
                self.update_discipline()
            elif optiune == "show_discipline":
                self.show_discipline()
            elif optiune == "find_discipline":
                self.find_discipline_ui()
            elif optiune == "add_nota":
                self.adaugare_nota()
            elif optiune == "top20":
                self.top20()
            elif optiune == "random_fct":
                self.random_fct()
            elif optiune == "ordine_nota":
                self.sort_by_note()
            elif optiune == "ordine_nume":
                self.sort_by_nume()
            elif optiune == "exit":
                print("Bye!!!")
                break
            else:
                print("Optiune invalida!")
