# Copyright (c) 2022, . and contributors
# For license information, please see license.txt
from frappe.utils import add_days, add_months
from frappe.model.document import Document
import frappe
import calendar
from craftpms.override import createinvsche

import time 
class Lease(Document):
	def validate(self):
		self.lease_invoice_schedule()

	def lease_invoice_schedule(self):
		if self.lease_item[0].lease_item == "RENT":
			self.lease_item[0].amount = frappe.db.get_value('Unit',  {'name': self.unit}, ['rent_price'])

		end_date = self.lease_end_date
		start_date = self.lease_start_date
		idx = 1
		freq = self.lease_item[0].frequency
		if freq == "Monthly":
			freq_float = 1
		elif freq == "Quaterly":
			freq_float = 4
		elif freq == "Half-yearly":
			freq_float = 6
		elif freq == "Yearly":
			freq_float = 12

		idx = 1
		if not self.lease_invoice:
			while start_date < end_date:
				period_end_date = add_days(add_months(start_date, float(freq_float)), -1)
				self.append('lease_invoice',{
					'idx': idx,
					'schedule_date': start_date,
					'lease_item': self.lease_item[0].lease_item,
					'amount': self.lease_item[0].amount,
					'paid_by': self.lease_item[0].paid_by,
				})
				start_date = add_days(period_end_date, 1)
				idx += 1
			
	
		frappe.msgprint("Invoice scheduling done.")

	

# @frappe.whitelist()
# def lease_invoice_schedule(leasedoc):
# 	lease = frappe.get_doc("Lease", str(leasedoc))
# 	end_date = lease.lease_end_date
# 	start_date = lease.lease_start_date
# 	idx = 1
# 	freq = lease.lease_item[0].frequency
# 	if freq == "Monthly":
# 		freq_float = 1
# 	elif freq == "Quaterly":
# 		freq_float = 4
# 	elif freq == "Half-yearly":
# 		freq_float = 6
# 	elif freq == "Yearly":
# 		freq_float = 12

# 	idx = 1
# 	if not lease.lease_invoice:
# 		while start_date < end_date:
# 			period_end_date = add_days(add_months(start_date, float(freq_float)), -1)
# 			lease.append('lease_invoice',{
# 				'idx': idx,
# 				'schedule_date': start_date,
# 				'lease_item': lease.lease_item[0].lease_item,
# 				'amount': lease.lease_item[0].amount,
# 				'paid_by': lease.lease_item[0].paid_by,
# 			})
# 			start_date = add_days(period_end_date, 1)
# 			idx += 1
		
# 	return idx

				