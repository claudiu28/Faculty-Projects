from service import Service
from repo import Repository
from validation import Validation
from ui import UI

service = Service(Validation(), Repository("spectacole.txt"))

ui = UI(service)
ui.meniu()
