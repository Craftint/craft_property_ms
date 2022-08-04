
import datetime


import frappe
from frappe.model.document import Document

class Unit(Document):
	def validate(self):
		if (self.contract_start_date and self.contract_end_date):
			if datetime.date.today() < self.contract_start_date:
				self.unit_status = "Booked"
			elif self.contract_start_date <= datetime.date.today() <= self.contract_end_date:
				self.unit_status = "On lease"
		else:
			self.unit_status = "Available"
			

		


