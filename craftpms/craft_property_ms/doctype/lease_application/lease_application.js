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
