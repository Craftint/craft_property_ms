// Copyright (c) 2022, . and contributors
// For license information, please see license.txt

frappe.ui.form.on('Lease', {
	// refresh: function(frm) {
	// 	cur_frm.add_custom_button(__("Make Invoice Schedule"), function() {
	// 		make_lease_invoice_schedule(cur_frm);
	// 	});

	// }
});

// var make_lease_invoice_schedule = function(frm){
// 	var doc = frm.doc;
// 	frappe.call({
// 		method: "craftpms.craft_property_ms.doctype.lease.lease.lease_invoice_schedule",
// 		args: {leasedoc: frm.doc.name},
// 		callback: function(r){
// 			cur_frm.reload_doc();
// 		}
// 	});
// };