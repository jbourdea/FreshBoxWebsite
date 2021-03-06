from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from dummy_data import *

from layouts import Layouts

class ProjectorViews(Layouts):

	def __init__(self, request):
		self.request = request

	@view_config(renderer="templates/index.pt")
	def index_view(self):
		return {"page_title": "Home"}

	@view_config(renderer="templates/contact_us.pt", name="contact")
	def company_view(self):
		return {"page_title": "Contact Us"}
		
	@view_config(renderer="templates/manage_accounts.pt",
				 name="users")
	def account_view(self):
		return {"page_title": "Manage Users"}
		
	@view_config(renderer="templates/manage_host_sites.pt", name="hostsites")
	def host_site_view(self):
		return {"page_title": "Manage Host Sites"}

	@view_config(renderer="templates/store.pt", name="store")
	def store_view(self):
		return {"page_title": "Store"}

	@view_config(renderer="templates/about_us.pt", name="about")
	def company_view(self):
		return {"page_title": "About Us"}
			
	@view_config(renderer="templates/login.pt", name="login")
	def login_view(self):
		username = self.request.POST.get('username')
		password = self.request.POST.get('password')
		user = authUser(username, password)
		self.request.session['userType'] = user['credentials'] if user != None else "none"
		self.request.session['userID'] = user['id'] if user != None else "0"
		#self.request.session['userType'] = userType(username,password)
		#self.request.session['userID'] = getUser(username)['id']
		if(userType(username,password) == 'Administrator'):
			return HTTPFound(location='/')
		return {"page_title": "Login"}

	@view_config(renderer="templates/index.pt", name="logout")
	def logout_view(self):
		self.request.session['userType'] = 'none'
		return HTTPFound(location='/')

	@view_config(renderer='templates/test_ajax.pt', name='test_ajax')
	def test_ajax(self):
		return {"page_title": "Test AJAX"}
		
	@view_config(renderer='json', name='test.json')
	def test_json(self):
		return {"data":"This is an AJAX call"}
		
	@view_config(renderer="templates/manage_sales.pt", name="sales")
	def view_sales(self):
		return {"page_title": "Manage Sales"}

	@view_config(renderer="templates/edit_user_info.pt", name="editUser")
	def view_editUser(self):
		return {"page_title": "Edit User"}
		
	@view_config(renderer="templates/edit_host_site.pt", name="editHostSite")
	def view_editHostSite(self):
		return {"page_title": "Edit HostSite"}
		
	@view_config(renderer="templates/edit_sale.pt", name="editSale")
	def view_editSale(self):
		customer_name = self.request.POST.get('customer_name')
		username = self.request.POST.get('username')
		phone = self.request.POST.get('phone')
		small_quant = self.request.POST.get('small_quant')
		large_quant = self.request.POST.get('large_quant')
		addOrder(customer_name, username, phone, large_quant, small_quant)
		return {"page_title": "Edit Sale"}