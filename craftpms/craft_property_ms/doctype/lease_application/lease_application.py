# Copyright (c) 2022, . and contributors
# For license information, please see license.txt
import frappe
import json
from frappe.model.document import Document

class Leaseapplication(Document):


	@frappe.whitelist()
	def get_unit_without_contracts(self):
		units = []
		#uni = [i.unit for i in property_details]
		contract_units = frappe.db.sql("""select unit from `tabContract`""",as_dict= True)
		unit =  [i.unit for i in self.property_details]
		for table in [self.property_details]:
			for i in table:
				units.append(
						dict(
							unit = i.unit,
							building = i.building,
							start_date = i.start_date,
							end_date = i.end_date,
						)
						)
		return units
	pass


@frappe.whitelist()
def make_contracts(unit, customer, start_date, end_date):
	#units = json.loads(unit_child_table).get("unit")
	building = frappe.db.get_value('Unit',  {'name': unit}, ['building'])
	contract = frappe.get_doc(
		dict(
			doctype="Contract",
			unit=unit,
			party_name= customer,
			building=building,
			start_date = start_date,
			end_date = end_date,
			contract_terms = "to be discussed"
		)
	).insert()
	contract.flags.ignore_mandatory = True
	contract.save()

	return building

