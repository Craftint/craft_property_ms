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
def make_contracts(customer, la_start_date, la_end_date):
	units = json.loads(craftpms.craft_property_ms.doctype.unit_child_doc.unit_child_table).get("unit")
	out = []

	for i in units:
		contract = frappe.get_doc(
			dict(
				doctype="Contract",
				unit=i["unit"],
				party_name= customer,
				building=i["building"],
				start_date = la_start_date,
				end_date = la_end_date,
			)
		).insert()
		contract.flags.ignore_mandatory = True
		contract.save()

	return [p.name for p in out]

