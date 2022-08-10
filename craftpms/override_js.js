frappe.ui.form.on("Contract", {
    onload: function(frm) {
        frm.trigger(
            frm.set_query("unit", function() {
		return {
			filters: {
				unit: "Available"
			}
		};
	    });
	    );
    },
    my_custom_code: function(frm){
        console.log(frm.doc.name)
    }
});
