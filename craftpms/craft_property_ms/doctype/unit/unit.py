from frappe.utils import (getdate,nowdate,)
from datetime import datetime

import frappe
from frappe.model.document import Document
import erpnext


class Unit(Document):
	def validate(self):
		self.get_contract_details()
		self.delete_contract()
		self.set_unit_status()
	
	def set_unit_status(self):
		if (self.contract_start_date and self.contract_end_date):
			if getdate(nowdate()) < getdate(self.contract_start_date):
				self.unit_status = "Booked"
			elif getdate(self.contract_start_date) <= getdate(nowdate()) <= getdate(self.contract_end_date):
				self.unit_status = "On lease"
			elif getdate(self.contract_end_date) < getdate(nowdate()):
				self.unit_status = "Available"
		elif self.contract and not self.contract_start_date and not self.contract_end_date:	
				self.unit_status = "Booked"
		else: 
			self.unit_status = "Available"
	
	
	def get_contract_details(self):
		contracts = frappe.db.get_list('Contract',filters={"unit": self.name}, pluck ="name")
		for contract2 in contracts:
			contract1 = str(contract2)	
			unit_owners = frappe.db.get_value('Contract',  {'name': contract1}, ['party_name'])
			start_dates = frappe.db.get_value('Contract',  {'name': contract1}, ['start_date'])
			end_dates = frappe.db.get_value('Contract',  {'name': contract1}, ['end_date'])
			self.contract = contract1
			self.unit_owner = unit_owners
			self.contract_start_date = start_dates
			self.contract_end_date = end_dates


	def delete_contract(self):
			unit_contract = frappe.db.get_value('Contract',  {'name': self.contract}, ['unit'])
			if not unit_contract:
				self.contract = None
				self.unit_owner = None
				self.contract_start_date = None
				self.contract_end_date = None

		
			
			#else:	
			###	self.contract_start_date = None
				##self.contract_end_date = None
	
		
def update_unit_status():
	units = frappe.db.sql("""select name from `tabUnit`""", as_dict=True)
	for unit in units:
		doc = frappe.get_doc("Unit", unit.name)
		doc.set_unit_status()
		unitst = frappe.db.set_value("Unit", doc.name, "unit_status", doc.unit_status)
	
def update_contract_details():
	units = frappe.db.sql("""select name from `tabUnit`""", as_dict=True)
	for unit in units:
		doc = frappe.get_doc("Unit", unit.name)
		doc.get_contract_details()
		cntrct = frappe.db.set_value("Unit", doc.name, "contract", doc.contract)
		unt_ownr = frappe.db.set_value("Unit", doc.name, "unit_owner", doc.unit_owner)
		cntrct_strt_dte = frappe.db.set_value("Unit", doc.name, "contract_start_date", doc.contract_start_date)
		cntrct_end_dte = frappe.db.set_value("Unit", doc.name, "contract_end_date", doc.contract_end_date)




def suppression_contract():
	units = frappe.db.sql("""select name from `tabUnit`""", as_dict=True)
	for unit in units:
		doc = frappe.get_doc("Unit", unit.name)
		doc.delete_contract()
		cntrct = frappe.db.set_value("Unit", doc.name, "contract", None)
		unt_ownr = frappe.db.set_value("Unit", doc.name, "unit_owner", None)
		cntrct_strt_dte = frappe.db.set_value("Unit", doc.name, "contract_start_date", None)
		cntrct_end_dte = frappe.db.set_value("Unit", doc.name, "contract_end_date", None)






