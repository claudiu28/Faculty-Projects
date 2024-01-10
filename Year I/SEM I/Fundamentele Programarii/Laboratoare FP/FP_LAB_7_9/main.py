from labs_7_9.ui import ui
from labs_7_9.utils.controller import ServiceStudent, ServiceDiscipline, ServiceNote
from labs_7_9.repo.file_repository import FileStudentRepository, FileDisciplinaRepository, FileNotaRepository
from labs_7_9.domain.validation import StudentValidation, DisciplinaValidation, NoteValidation


student_repository = FileStudentRepository("studenti.txt")
disciplina_repository = FileDisciplinaRepository("discipline.txt")
note_repository = FileNotaRepository("note.txt")

service_student = ServiceStudent(StudentValidation(), student_repository)
service_discipline = ServiceDiscipline(DisciplinaValidation(), disciplina_repository)
serivice_note = ServiceNote(NoteValidation(), note_repository, student_repository, disciplina_repository)
consola = ui.Consola(service_student, service_discipline, serivice_note)
consola.meniu().run()
