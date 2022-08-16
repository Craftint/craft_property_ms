// Copyright (c) 2022, . and contributors
// For license information, please see license.txt

frappe.ui.form.on("Lease application", "onload", function(frm) {
	frm.fields_dict['property_details'].grid.get_field('unit').get_query =
			function(doc, cdt, cdn) {
        		var child = locals[cdt][cdn];
				return {
					filters: {
              		  'unit_status': 'Available',
              		  'building': child.building,
				}
				}
			}
			

});


frappe.ui.form.on("Lease application", "onload", function(frm) {
    frm.fields_dict['property_details'].grid.get_field('building').get_query =
			function(doc, cdt, cdn) {
        		var child = locals[cdt][cdn];
				return {
					filters: {
              		  'emirate': child.emiratestate,
              		  
				}
				}
			}
});

frappe.ui.form.on("Lease application", {
	refresh: function(frm) {
	  frm.add_custom_button(__('Contract'), function(){

		frm.call({
			  method: 'craftpms.craft_property_ms.doctype.lease_application.lease_application.get_unit_without_contracts',
			  args: {
				"property_details" : frm.doc.property_details,
				"unit" : frm.doc.property_details[0].unit,
				"building" : frm.doc.property_details[0].building,
			},
			  callback: function(r) {
				
				  const fields = [{
					  label: 'Property details',
					  fieldtype: 'Table',
					  fieldname: 'property_details',
					  description: __('Select'),
					  fields: [{
						  fieldtype: 'Link',
						  fieldname: 'unit',
						  label: __('Unit'),
						  in_list_view: 1
					  }, 
					  {
						  fieldtype: 'Link',
						  fieldname: 'building',
						  label: __('Building'),
						  in_list_view: 1
					  }],
					  data: r.message,
					  get_data: () => {
						  return r.message
					  }
				  }]
				  var d = new frappe.ui.Dialog({
					  title: __('Select unit for creating contracts'),
					  fields: fields,
						  primary_action: function() {
							  var data = {property_details: d.fields_dict.property_details.grid.get_selected_children()};
							  frm.call({
								  method: 'craftpms.craft_property_ms.doctype.lease_application.lease_application.make_contracts',
								  args: {
									  "unit" :data,
									  "customer": frm.doc.customer,
									  "la_start_date": frm.doc.la_start_date,
									  "la_end_date": frm.doc.la_end_date,
								  },
								  freeze: true,
								  callback: function(r) {
									  if(r.message) {
											  frappe.msgprint({
											  title: __('Work Order not created'),
											  message: __('Work Order already created for all items with BOM'),
											  indicator: 'orange'
										  });
									  }
								  }
							  });
						  },
						  primary_action_label: __('Create')
				  });
					d.show();
				}
			 
	
			  });
			  });
			  
		  }	
	  });

			
	
		


/*

primary_action: function() {
	var data = {items: d.fields_dict.property_details.grid.get_selected_children()};
	me.frm.call({
		method: 'make_contracts',
		args: {
			"customer": frm.doc.customer,
			"la_start_date": frm.doc.end_date,
			"la_end_date": frm.doc.la_end_date,
		},
		freeze: true,
		callback: function(r) {
			if(r.message) {
				frappe.msgprint({
					title: __('Work Order not created'),
					message: __('Work Order already created for all items with BOM'),
					indicator: 'orange'
				});
			}
		},

*/


/*


this.frm.call({
			doc: this.frm.doc,
			method: 'craftpms.craft_property_ms.doctype.lease_application.lease_application.get_unit_without_contract',
			callback: function(r) {
				const fields = [{
					label: 'Propertydetails',
					fieldtype: 'Table',
					fieldname: 'property_details',
					description: __('Select'),
					fields: [{
						fieldtype: 'Link',
						fieldname: 'unit',
						label: __('Unit'),
						in_list_view: 1
					}, 
					{
						fieldtype: 'Link',
						fieldname: 'building',
						label: __('Building'),
						in_list_view: 1
					}],
					data: r.message,
					get_data: () => {
						return r.message
					}
				}]
			}
		


*/




		// frm.add_custom_button(__('Unit'), function() {console.log("Running")});





			









//frappe.ui.form.on('Quotation', {
//	cost_center: function (frm) {
 //      $.each(frm.doc.items, function (k, item) {
   //         frappe.model.set_value(item.doctype, item.name, 'cost_center', frm.doc.cost_center);
     //   });
//	},
	
//	validate: function (frm) {
  //      if (frm.doc.items && frm.doc.items.length > 0) {
    //        $.each(frm.doc.items, function (k, item) {
      //          set_wise_qty_html(frm, item.doctype, item.name);
        //    });
        //}

        // Set hardware set wise summary html table
       // if (frm.doc.order_type == 'Door Schedule' && frm.doc.door_types && frm.doc.items && frm.doc.items.length > 0) {
         //   let set_wise_qty = Object.values(frm.doc.door_types.reduce((a, {hardware_set, door_qty}) => {
           //     a[hardware_set] = a[hardware_set] || {hardware_set, door_qty: 0};
             //   a[hardware_set].door_qty += door_qty;
               // return a;
           // }, {}));

          //  let h_list = [];
