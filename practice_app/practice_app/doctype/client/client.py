# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Client(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		age: DF.Int
		first_name: DF.Data | None
		full_name: DF.Data | None
		last_name: DF.Data | None
	# end: auto-generated types

	pass
