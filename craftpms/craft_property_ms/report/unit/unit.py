# Copyright (c) 2022, . and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import (getdate,nowdate,)

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data




def get_columns(filters):
	columns = [
		{
			'label':_('Unit'),
			'field_name':'unit',
			'fieldtype':'Data',

			'width':250,
		},
		{
			'label':_('Unit_status'),
			'field_name':'unit_status',
			'fieldtype':'Select',
			'options': ["Available","On lease", "Booked"],
			'width':250,
		},
		{
			'label':_('Building'),
			'field_name':'building',
			'fieldtype':'Link',
			'options':"Building",
			'width':250
		},
		{
			'label':_('Start Date'),
			'field_name':'contract_start_date',
			'fieldtype':'Date',
			'width':250,
		},
		{
			'label':_('End Date'),
			'field_name':'contract_end_date',
			'fieldtype':'Date',
			'width':250,
		}
	]
	return columns
		
def get_data(filters):
	conditions = ""
	if (filters.get("unit_status") and filters.get("unit")):
		 conditions += "where name = '%s' and unit_status = '%s'  " %(filters.unit, filters.unit_status)
	else:
		if (filters.get("unit_status")): conditions += "where unit_status = '%s' "%(filters.unit_status)
		if (filters.get("unit")) : conditions += "where name = '%s'"%(filters.unit)
	#	if (filters.get("date")) : conditions += "where (%s between contract_start_date and contract_end_date) "%(filters.date)

	data = frappe.db.sql(""" 
						Select name, unit_status, building, contract_start_date, contract_end_date
						from `tabUnit` %s""" %(conditions))
	return data

