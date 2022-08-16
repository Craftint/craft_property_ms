// Copyright (c) 2022, . and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Building's report"] = {
	"filters": [
		{
			fieldname: 'building',
			label: __('Building'),
			fieldtype: 'Link',
			options : "Building",
			width: 200,
			reqd: 0,
		},
		{
			fieldname: 'unit',
			label: __('Unit'),
			fieldtype: 'Link',
			options: "Unit",
			width: 200,
			reqd: 0,
		},
		
	]
};
