# Copyright (c) 2022, . and contributors
# For license information, please see license.txt
from frappe.utils import add_days, add_months
from frappe.model.document import Document
import frappe
import calendar
import time 
from datetime import datetime
from dateutil.rrule import rrule, MONTHLY
class Lease(Document):
	def validate(self):
		self.lease_invoice_schedule()



	def lease_invoice_schedule(self):
		#date_start = datetime.strptime(self.lease_start_date, '%Y-%m-%d')
		#date_end = datetime.strptime(self.lease_end_date, '%Y-%m-%d')
		date_start = self.lease_start_date
		date_end = self.lease_end_date
		diff =  -((date_start.year - date_end.year) * 12 + date_start.month - date_end.month)
		if self.lease_item:
			if diff >= 12:
				self.lease_item[0].amount = (frappe.db.get_value('Unit',  {'name': self.unit}, ['rent_price']))*95/100
				self.lease_item[0].total_amount = (frappe.db.get_value('Unit',  {'name': self.unit}, ['rent_price']))*diff
				self.lease_item[0].paid_by = self.lease_customer
			else:
				self.lease_item[0].amount = frappe.db.get_value('Unit',  {'name': self.unit}, ['rent_price'])
				self.lease_item[0].total_amount = frappe.db.get_value('Unit',  {'name': self.unit}, ['rent_price'])*diff
				elf.lease_item[0].paid_by = self.lease_customer


		end_date = self.lease_end_date
		start_date = self.lease_start_date
		idx = 1
		freq = self.lease_item[0].frequency
		if freq == "Monthly":
			freq_float = 1
			if int(diff) % float(freq_float) != 0:
				frappe.throw("The frequency does not match lease's months period")
		elif freq == "Quaterly":
			freq_float = 4
			if diff % freq_float != 0:
				frappe.throw("The frequency does not match lease's months period")
		elif freq == "Half-yearly":
			freq_float = 6
			if diff % freq_float != 0:
				frappe.throw("The frequency does not match lease's months period")

		elif freq == "Yearly":
			freq_float = 12
			if diff % freq_float != 0:
				frappe.throw("The frequency does not match lease's months period")
	
		idx = 1
		if not self.lease_invoice:
			while start_date < end_date:
				period_end_date = add_days(add_months(start_date, float(freq_float)), -1)
				self.append('lease_invoice',{
					'idx': idx,
					'schedule_date': start_date,
					'lease_item': self.lease_item[0].lease_item,
					'amount': self.lease_item[0].amount* freq_float,
					'paid_by': self.lease_item[0].paid_by,
				})
				start_date = add_days(period_end_date, 1)
				idx += 1

# def aft():
	# a = frappe.db.get_value('Unit',  {'name': "UNit-0013"}, ['contract_start_date'])
	# b = frappe.db.get_value('Unit',  {'name': "UNit-0013"}, ['contract_end_date'])
	# a1 = datetime.strptime(a, '%Y-%m-%d')
	# b1 = datetime.strptime(b, '%Y-%m-%d')


	# t =  -((a1.year - b1.year) * 12 + a1.month - b1.month)
	# print(type(t))

		# for table in [self.lease_invoice]:
		#  	for s in table:
		#  		if not s.invoice_code:
		#  			s.invoice_code = frappe.db.get_value('Lease invoice',  {'posting_date': s.schedule_date}, ['name']),
		#  		else:
		#  			frappe.msgprint("Invoice code already_filled")


	
		frappe.msgprint("Invoice scheduling done.")




				