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
			'label':_('Building'),
			'field_name':'building',
			'fieldtype':'Data',
			'width':250,
		},
		{
			'label':_('N of units'),
			'field_name':'n_units',
			'fieldtype':'Data',
			'width':250
		},
		{
			'label':_('Available'),
			'field_name':'available',
			'fieldtype':'Data',
			'width':250
		},
		{
			'label':_('rent'),
			'field_name':'arasvailable',
			'fieldtype':'Data',
			'width':250
		},


	]
	return columns

def get_data(filters):
	data =  frappe.db.sql(""" 
					Select b.building, b.no_of_units, b.available_units                    
					from `tabBuilding` b
					left join (select count(u.name) from `tabUnit` u where u.unit_status = 'On Lease' and u.building = b.name""")    
				

	return data


	'''select pe.name, pii.item_code, pii.item_name, per.reference_name, pii.batch_no, pe.posting_date, pi.supplier_name, pe.mode_of_payment, pii.qty, pii.stock_uom, pii.rate, pe.paid_amount, pii.amount
	 	from `tabPayment Entry` pe 
		left join `tabPayment Entry Reference` per on pe.name = per.parent
	# 	left join `tabPurchase Invoice Item` pii on per.reference_name = pii.parent
	# 	left join `tabPurchase Invoice` pi on per.reference_name = pi.name where pe.name is not null {}
	# 	'''


	