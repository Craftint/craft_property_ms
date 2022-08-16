# Copyright (c) 2022, . and contributors
# For license information, please see license.txt
import frappe
import json
from frappe.model.document import Document

class Leaseapplication(Document):
	pass

@frappe.whitelist()
def get_unit_without_contracts(unit, building, property_details):
	units = []
	#uni = [i.unit for i in property_details]
	contract_units = frappe.db.sql("""select unit from `tabContract`""",as_dict= True)
	units.append(
			dict(
				unit = unit,
				building = building,
			)
			)
	return units


@frappe.whitelist()
def make_contracts(unit, customer, la_start_date, la_end_date):
	#units = json.loads(unit_child_table).get("unit")
	building = frappe.db.get_value('Unit',  {'name': unit}, ['building'])
	contract = frappe.get_doc(
		dict(
			doctype="Contract",
			unit=unit,
			party_name= customer,
			building=building,
			start_date = la_start_date,
			end_date = la_end_date,
			contract_terms = "to be discussed"
		)
	).insert()
	contract.flags.ignore_mandatory = True
	contract.save()

	return 

