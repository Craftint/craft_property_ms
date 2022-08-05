
import datetime



import frappe
from frappe.model.document import Document

class Unit(Document):
	def validate(self):
		self.set_unit_status()
	
	def set_unit_status(self):

		if (self.contract_start_date and self.contract_end_date):
			if datetime.date.today() < self.contract_start_date:
				self.unit_status = "Booked"
			elif self.contract_start_date <= datetime.date.today() <= self.contract_end_date:
				self.unit_status = "On lease"
			elif self.contract_end_date < datetime.date.today():
				self.unit_status = "Available"
		else:
			self.unit_status = "Available"
		
		
def update_unit_status():
	units = frappe.db.sql("""select name from `tabUnit`""")
	for unit in units:
		doc = frappe.get_doc("Unit", unit.name)
		doc.set_unit_status()
		unitstat = frappe.db.set_value("Unit", doc.name, "unit_status", doc.unit_status)
	return unitstat

	




