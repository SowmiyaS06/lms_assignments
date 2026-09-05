# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Admission(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		admission_date: DF.Date | None
		amended_from: DF.Link | None
		course: DF.Link | None
		fees: DF.Currency
		has_scholarship: DF.Check
		scholarship_amount: DF.Currency
		statu: DF.Literal["Pending", "Approved", "Rejected"]
		student: DF.Link | None
		workflow_state: DF.Literal["Pending", "Approved", "Rejected"]
	# end: auto-generated types

	pass
