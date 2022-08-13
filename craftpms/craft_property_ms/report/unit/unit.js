// Copyright (c) 2022, . and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["unit"] = {
	"filters": [
		{
			fieldname: 'unit',
			label: __('Unit'),
			fieldtype: 'Link',
			options : "Unit",
			width: 200,
			reqd: 0,
		},
		{
			fieldname: 'unit_status',
			label: __('Unit status'),
			fieldtype: 'Select',
			options: ["Available","On lease", "Booked"],
			width: 200,
			reqd: 0,
		},
		{
			fieldname: 'date',
			label: __('Date'),
			fieldtype: 'Date',
			width: 200,
			reqd: 0,
		},
		
	]
};
