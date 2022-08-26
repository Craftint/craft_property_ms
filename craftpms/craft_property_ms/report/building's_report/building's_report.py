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
			'fieldtype':'Link',
			'options':"Building",
			'width' : 140
		},
		{
			'label':_('Address'),
			'field_name':'address',
			'fieldtype':'Data',
			'width' : 180
			
		},
		{
			'label':_('Emirate'),
			'field_name':'emirate',
			'fieldtype':'Data',
			'width' : 90
			

		},
		{
			'label':_('Owner'),
			'field_name':'owner',
			'fieldtype':'Data',\
			'width' : 140

		},
		{
			'label':_('N of units'),
			'field_name':'n_units',
			'fieldtype':'Data',
			'width' : 80

		},
		{
			'label':_('Available'),
			'field_name':'available',
			'fieldtype':'Data',
			'width' : 80

		},
		{
			'label':_('On lease'),
			'field_name':'on_lease',
			'fieldtype':'Data',
			'width' : 80

		},
		{
			'label':_('Booked'),
			'field_name':'booked',
			'fieldtype':'Data',
			'width' : 90

		},
		{
			'label':_('Expected'),
			'field_name':'expected',
			'fieldtype':'Currency',
			'width' : 150,
			'default' : 0.00
 
		},
		{
			'label':_('Collected'),
			'field_name':'collected',
			'fieldtype':'Currency',
			'width' : 150,
			'default' : 0.00

		}


	]
	return columns

def get_data(filters):

	conditions = ""
	if (filters.get("building") and filters.get("address")):
		conditions += "where b.name = '%s' and b.address = '%s'" %(filters.building, filters.address)
	else:   
		if (filters.get("building")): conditions += "where b.name = '%s'" %(filters.building)
		if (filters.get("address")): conditions += "where b.address = '%s'" %(filters.address)

	data =  frappe.db.sql(	""" 
					select b.name, b.address, b.emirate, b.building_owner, u.total, u.available, u.on_lease, u.booked, l.rented, s.ere
					from `tabBuilding` b 
					left join (select building, COUNT(name) as total,
					COUNT(IF(unit_status="Available", name, NULL)) as available, 
					COUNT(IF(unit_status="On lease",name,NULL)) as on_lease,
                    COUNT(IF(unit_status="Booked", name, NULL)) as booked 
					from `tabUnit` group by building) as u on b.name = u.building
					left join(select building, sum(total_amount) as rented from `tabLease item` group by building) as l 
					on b.name = l.building
					left join(select building, sum(amount) as ere from `tabLease invoice schedule` where CURRENT_DATE() > schedule_date
					group by building) as s on b.name = s.building order by l.rented DESC %s
					""" %(conditions))    

	return data




