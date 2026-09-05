# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Course(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		active: DF.Check
		course_name: DF.Data | None
		course_type: DF.Literal["Full Time", "Part Time", "Online"]
		department: DF.Link | None
		duration: DF.Int
		fees: DF.Currency
	# end: auto-generated types

	pass
