// Copyright (c) 2022, . and contributors
// For license information, please see license.txt

frappe.ui.form.on('Unit', {
      onload: function(frm) {
        frappe.call({
                method:'craftpms.craft_property_ms.doctype.unit.unit.get_contract',
                args: {
                        'contract': frm.doc.contract,
                        'unit_owner': frm.doc.unit_owner,
                        'contract_start_date': frm.doc.contract_start_date,
                        'contract_end_date': frm.doc.contract_end_date,

                    },
           callback: function(r) {
              frm.set_value("contract", r.message.contract);
              frm.set_value("unit_owner", r.message.unit_owner);
              frm.set_value("contract_start_date", r.message.contract_start_date);
              frm.set_value("contract_end_date", r.message.contract_end_date);
              frm.save()
            }
        });	
      }
});
