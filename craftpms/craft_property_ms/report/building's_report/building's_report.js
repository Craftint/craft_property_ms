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
			fieldname: 'address',
			label: __('Address'),
			fieldtype: 'Link',
			options : "Address",
			width: 200,
			reqd: 0,
		},
		
	],
	'formatter': function(value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);
		if (data && data.bold) {
			value = value.bold();
		}
		return value;
	}
		
};
