# Copyright (c) 2022, . and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Lease(Document):
	pass
	def validate(self):
		if self.unit:
			self.building = frappe.db.sql("""select building from `tabUnit` where name = %s """,(self.unit))
		else: 
			self.building = " "

	
