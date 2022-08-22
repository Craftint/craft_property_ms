
from frappe import _
from frappe.model.document import Document
from erpnext.crm.doctype.contract.contract import Contract
from datetime import date
from frappe.utils import getdate
import frappe


"""
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






def createinvsche(idx,parent,date, item, invoice_code,amount, paid_by):
	aer = frappe.get_doc(
			dict(
				idx = idx,
				parent = parent,
				doctype="Lease invoice schedule",
				parentfield="lease_invoice",
				parenttype="Lease",
				schedule_date= date,
				lease_item=item,
				invoice_code = invoice_code,
				amount=amount,
				paid_by=paid_by,
			)
		)
	aer.insert()
	aer.save()
	"""
