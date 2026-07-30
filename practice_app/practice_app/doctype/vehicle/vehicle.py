# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Vehicle(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		brands: DF.Literal["Toyota", "Honda", "Hyundai", "Suzuki", "Tata", "BMW", "Audi"]
		customer_name: DF.Data
		fuel_type: DF.Literal["Petrol", "Diesel", "Electric Hybrid"]
		manufacturing_year: DF.Int
		model: DF.Data | None
		registration_date: DF.Date
		status: DF.Literal["Active", "Inactive"]
		vehicle_number: DF.Data
		vehicle_type: DF.Literal["Car", "Bike", "Bus", "Truck", "Van"]
	# end: auto-generated types

	pass
