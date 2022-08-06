from frappe.utils import (getdate,nowdate,)
from datetime import datetime

import frappe
from frappe.model.document import Document
import erpnext

class Unit(Document):
	def validate(self):
		self.set_start_date()
		self.set_unit_status()
	
	def set_unit_status(self):
		if (self.contract_start_date and self.contract_end_date):
			if getdate(nowdate()) < getdate(self.contract_start_date):
				self.unit_status = "Booked"
			elif getdate(self.contract_start_date) <= getdate(nowdate()) <= getdate(self.contract_end_date):
				self.unit_status = "On lease"
			elif getdate(self.contract_end_date) < getdate(nowdate()):
				self.unit_status = "Available"
		else:
			self.unit_status = "Available"
	#todo
	#trying to get contract details when creating a contract to unit doctype in order to update unit status
	 
	def set_start_date(self):
		units_contract = frappe.db.sql("""select unit from `tabContract`""", as_dict = True)
		units = frappe.db.sql("""select name from `tabUnit`""")
		for unit_contract in units_contract:
			for unit in units:
				if unit == unit_contract:
					doc = frappe.get_doc("Unit", unit.name)
					contract_name =frappe.db.sql("""SELECT name FROM `tabContract` WHERE {} = {}""".format(unit_contract,unit))
					frappe.db.set_value("Unit", doc.name, "contract_number", contract_name)
			frappe.db.commit()
		print(frappe.db.sql("""select contract from `tabUnit`""", as_dict = True))
		


		
		
def update_unit_status():

	units = frappe.db.sql("""select name from `tabUnit`""", as_dict=True)
	for unit in units:
		doc = frappe.get_doc("Unit", unit.name)
		doc.set_unit_status()
		unitst = frappe.db.set_value("Unit", doc.name, "unit_status", doc.unit_status)
		print(doc)
		
	








