frappe.query_reports["Unit report"] = {
	"filters": [
		{
			fieldname: "unit_status",
			label: __("units_status"),
			fieldtype: "Select",
			options:"Item Group",
			default: "",
		},
		{
			fieldname: "item_code",
			label: __("Item"),
			fieldtype: "Link",
			options:"Item Group",
			default: "",
		},
