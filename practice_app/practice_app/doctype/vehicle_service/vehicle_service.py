# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class VehicleService(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount: DF.Currency
		brand: DF.Data | None
		customer_name: DF.Data | None
		discount: DF.Currency
		labour_charge: DF.Currency
		mechanic: DF.Literal["John", "David", "Kumar", "Ahmed", "Peter"]
		naming_series: DF.Literal["GS-.#####", "OC-.#####", "BS-.#####", "ER-.#####", "WA-.#####", "AC-.#####", "WS-.#####"]
		net_amount: DF.Currency
		payment_mode: DF.Literal["Cash", "Card", "UPI", "Bank", "Transfer"]
		rating: DF.Rating
		service_date: DF.Date | None
		service_id: DF.Data | None
		service_status: DF.Literal["Pending", "In Progress", "Completed", "Cancelled"]
		service_type: DF.Literal["General Service", "Oil Change", "Brake Service", "Engine Repair", "Wheel Alignment", "AC Service", "Washing"]
		spare_perts_cost: DF.Currency
		tax: DF.Currency
		vehicle: DF.Link | None
		vehicle_type: DF.Data | None
	# end: auto-generated types

	pass

	@frappe.whitelist()
	def test_method(self):
		return "Hello from python"