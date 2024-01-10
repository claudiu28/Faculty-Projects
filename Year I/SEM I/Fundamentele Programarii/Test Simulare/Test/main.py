from validation import Validation
from file_repo import FileRepo
from service import ServiceImobiliar
from ui import Consola

validation = Validation()
repo = FileRepo("imobiliare.txt")
service = ServiceImobiliar(validation.verificare_tip, repo)
consola = Consola(service)
consola.run()
