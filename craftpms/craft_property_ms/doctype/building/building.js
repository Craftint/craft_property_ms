frappe.provide("erpnext")

erpnext.PropertyController = frappe.ui.form.Controller.extend({
	onload: function() {
		frappe.call({
				method:'craftpms.craft_property_ms.doctype.building.building.n_units',
				args: {
						'building_name': this.frm.doc.building_name,
					  },
		   callback: function(r) {
			this.frm.set_value("no_of_units", r.message);
			this.frm.save()
		}
			});
			
			frappe.call({
				method:'craftpms.craft_property_ms.doctype.building.building.available_units',
				args: {
						'building_name': this.frm.doc.building_name,
					  },
		   callback: function(r) {
			this.frm.set_value("available_units", r.message);
			this.frm.save()
		}
			});
			
  	},
	refresh: function() {
		this.frm.add_custom_button(__('Unit'), this.make_unit, __('Create'));
		this.frm.page.set_inner_btn_group_as_primary(__('Create'));
		// this.frm.add_custom_button(__('Unit'), function() {console.log("Running")});
	},

	make_unit: function() {
		console.log("Running")
	}
})


