# Copyright (c) 2022, . and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(filters), get_data(filters)
	return columns, data


def get_columns(filters):
	columns = [
		{
			'label':_('Lease app No'),
			'field_name':'lease_app_num',
			'fieldtype':'Link',
			'options':"Lease application",
			'width' : 140
		},
		{
			'label':_('Customer'),
			'field_name':'customer',
			'fieldtype':'Data',
			'width' : 180
			
		},
		{
			'label':_('Start date'),
			'field_name':'start_date',
			'fieldtype':'Date',
			'width' : 180
			

		},
		{
			'label':_('End date'),
			'field_name':'end_date',
			'fieldtype':'Date',\
			'width' : 180

		},
		{
			'label':_('BUilding'),
			'field_name':'building',
			'fieldtype':'Data',\
			'width' : 180

		},
		{
			'label':_('Unit requested'),
			'field_name':'unit',
			'fieldtype':'unit',\
			'width' : 180

		},
	]
	return columns

def get_data(filters):

	data =  frappe.db.sql(	""" 
					select l.name, u.cstmr, u.start_date, u.end_date, u.building, u.unit
					from `tabUnit Child Table` u 
					left join (select customer, name from `tabLease application` group by customer) as l 
					on u.cstmr = l.customer order by u.start_date, u.cstmr
					""")    

	return data




