from frappe import _
from frappe.model.document import Document
from erpnext.crm.doctype.contract.contract import Contract
from datetime import date
from frappe.utils import getdate

class CustomContract(Contract):

    def validate(self):
        self.contract_on_lease()
        super().validate()

    def contract_on_lease(self):
        if  getdate(self.start_date) <= date.today() <= getdate(self.end_date):
	        self.is_on_lease = 1
        elif date.today() <= getdate(self.start_date):
            self.is_on_lease = 1 
        else:
            self.is_on_lease = 0
	
	
