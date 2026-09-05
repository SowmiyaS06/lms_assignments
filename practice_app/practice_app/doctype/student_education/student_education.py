# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class StudentEducation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		institution: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		percentage: DF.Percent
		qualification: DF.Data | None
		year: DF.Int
	# end: auto-generated types

	pass
