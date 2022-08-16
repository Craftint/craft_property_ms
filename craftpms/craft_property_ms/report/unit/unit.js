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
		
	],
	"formatter": function(value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);

		if (data && data.indent == 0.0) {
			value = $(`<span>${value}</span>`);
			var $value = $(value).css("font-weight", "bold");
			value = $value.wrap("<p></p>").parent().html();
		}

		return value;
	}
	
}