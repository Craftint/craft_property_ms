# Copyright (c) 2022, . and contributors
# For license information, please see license.txt
import frappe
import json
from frappe.model.document import Document
from datetime import datetime

class Leaseapplication(Document):
	def validate(self):
		# unit =  [i.unit for i in self.property_details]
		# for table in [self.property_details]:
		# 	for i in table: 
		# 		un_cont = frappe.db.get_value('Contract',  {'unit': i.unit}, ['unit'])
		# 		sd = frappe.db.get_value('Contract',  {'unit': i.unit}, ['start_date'])
		# 		ed = frappe.db.get_value('Contract',  {'unit': i.unit}, ['end_date'])
		# 		lsd = datetime.strptime(i.start_date, '%Y-%m-%d')
		# 		led = datetime.strptime(i.end_date, '%Y-%m-%d')
		# 		csd = datetime.combine(sd, datetime.min.time())
		# 		ced = datetime.combine(ed, datetime.min.time())
		# 	if un_cont:
		# 		if csd < lsd < ced:
		# 			frappe.throw("You can't use this period, please select another")
		# 		elif csd < led < ced:
		# 			frappe.throw("You can't use this period, please select another period or unit")
		# 		elif csd < lsd < ced and csd < led < ced:
		# 			frappe.throw("You can't use this period, please select another period or unit")
		# 		break
		

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

