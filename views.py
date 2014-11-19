from pyramid.view import view_config

from dummy_data import COMPANY
from dummy_data import getUsers
#from dummy_data import PROJECTS

from layouts import Layouts

class ProjectorViews(Layouts):

    def __init__(self, request):
        self.request = request
        
    @view_config(renderer="templates/index.pt")
    def index_view(self):
        return {"page_title": "Home"}

    @view_config(renderer="templates/company.pt",
                 name="contact")
    def company_view(self):
        return {"page_title": COMPANY + " Projects",
                "users": GetUsers()}
