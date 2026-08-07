# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ApplicantSkill(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		experience: DF.Float
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		rating: DF.Rating
		skill: DF.Data | None
	# end: auto-generated types

	pass
