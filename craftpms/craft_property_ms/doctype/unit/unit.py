
import datetime
from datetime import datetime


import frappe
from frappe.model.document import Document

class Unit(Document):
	def validate(self):
		self.set_unit_status()
	
	def set_unit_status(self):
		d = "2022-08-18"
		d2 = datetime.strptime(d,"%Y-%m-%d").date()
		if (self.contract_start_date and self.contract_end_date):
			if d2 < self.contract_start_date:
				self.unit_status = "Booked"
			elif self.contract_start_date <= d2 <= self.contract_end_date:
				self.unit_status = "On lease"
			elif self.contract_end_date < d2:
				self.unit_status = "Available"
		else:
			self.unit_status = "Available"
		
		
def update_unit_status():
	units = frappe.db.sql("""select name from `tabUnit`""", as_dict= True)
	for unit in units:
		doc = frappe.get_doc("Unit", unit.name)
		doc.set_unit_status()
		unitst = frappe.db.set_value("Unit", doc.name, "unit_status", doc.unit_status)
	return unitst

	




