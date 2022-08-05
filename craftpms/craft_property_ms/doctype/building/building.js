frappe.provide("erpnext")

erpnext.PropertyController = frappe.ui.form.Controller.extend({
	onload: function(frm) {
		frappe.call({
				method:'craftpms.craft_property_ms.doctype.building.building.n_units',
				args: {
						'building_name': frm.doc.building_name,
					  },
		   callback: function(r) {
			frm.set_value("no_of_units", r.message);
			frm.save()
		}
			});
			
			frappe.call({
				method:'craftpms.craft_property_ms.doctype.building.building.available_units',
				args: {
						'building_name': frm.doc.building_name,
					  },
		   callback: function(r) {
			frm.set_value("available_units", r.message);
			frm.save()
		}
			});
			
  	},
	refresh: function(frm) {
		frm.add_custom_button(__('Unit'), this.make_unit, __('Create'));
		frm.page.set_inner_btn_group_as_primary(__('Create'));
		// frm.add_custom_button(__('Unit'), function() {console.log("Running")});
	},

	make_unit: function() {
		frappe.call({
			method: 'craftpms.craft_property_ms.doctype.building.building.make_unit',
			args: {'message': "Hello"},
	})
	}
})


