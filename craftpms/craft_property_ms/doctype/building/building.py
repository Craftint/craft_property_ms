# Copyright (c) 2022, . and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Building(Document):
	pass
	
@frappe.whitelist()
def n_units(building_name= None):
	no_of_units = frappe.db.count('Unit',filters={"building_name": building_name})
	return no_of_units
			
@frappe.whitelist()		
def available_units(building_name= None):
	available_units = frappe.db.count('Unit',filters={"building_name": building_name, "unit_status": "Available"})
	return available_units


