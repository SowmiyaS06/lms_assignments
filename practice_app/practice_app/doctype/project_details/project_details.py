# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ProjectDetails(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		cost: DF.Currency
		hours: DF.Int
		notes: DF.SmallText | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		project_name: DF.Data | None
		status: DF.Literal["Assigned", "Completed", "Pending"]
	# end: auto-generated types

	pass
