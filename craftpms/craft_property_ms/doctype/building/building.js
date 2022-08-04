
frappe.ui.form.on("Building", {
    	refresh: function(frm) {
    		if(frm.doc.building_name !== ""){
			frappe.call({
        			method:'craftpms.craft_property_ms.doctype.building.building.n_units',
        			args: {
            				'building_name': frm.doc.building_name,
      		        	},
       		callback: function(r) {
				frm.set_value("no_of_units", r.message);
			}
        		});
        		
        		frappe.call({
        			method:'craftpms.craft_property_ms.doctype.building.building.available_units',
        			args: {
            				'building_name': frm.doc.building_name,
      		        	},
       		callback: function(r) {
				frm.set_value("available_units", r.message);
			}
        		});
        	}
    	}
});


