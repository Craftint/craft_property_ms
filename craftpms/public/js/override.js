frappe.ui.form.on("Contract","onload",function(frm){
    frm.fields_dict['unit'].get_query = function(doc) {
        return {
            filters: {
                "unit_status": 'Available',
            }
        }
    }
});



