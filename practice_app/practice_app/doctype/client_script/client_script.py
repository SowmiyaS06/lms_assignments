# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Client_Script(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF
        from practice_app.practice_app.doctype.project_details.project_details import (
            ProjectDetails,
        )

        age: DF.Int
        amended_from: DF.Link | None
        bonus: DF.Currency
        completed: DF.Check
        date_of_birth: DF.Date | None
        department: DF.Literal["IT", "ECE", "EEE", "CSE", "AIDS", "AIML"]
        designation: DF.Data | None
        email: DF.Data | None
        employee_id: DF.Data | None
        employee_name: DF.Data | None
        experience: DF.Int
        joining_date: DF.Date | None
        manager: DF.Link | None
        phone: DF.Phone | None
        profile_photo: DF.AttachImage | None
        progress: DF.Percent
        projects: DF.Table[ProjectDetails]
        rating: DF.Rating
        remarks: DF.SmallText | None
        resume: DF.Attach | None
        salary: DF.Currency
        status: DF.Literal["Active", "Inactive"]
        total_salary: DF.Currency

    # end: auto-generated types

    @frappe.whitelist()
    def calculate_bonus(self):
        return self.salary * 0.10