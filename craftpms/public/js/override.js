frappe.ui.form.on("Contract","onload",function(frm){
    frm.fields_dict['unit'].get_query = function(doc) {
        return {
            filters: {
            	"building": frm.doc.building,
                "unit_status": 'Available',
            }
        }
    }
});



