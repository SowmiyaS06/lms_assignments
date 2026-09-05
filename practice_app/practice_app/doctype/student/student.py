# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Student(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from practice_app.practice_app.doctype.student_education.student_education import StudentEducation
		from practice_app.practice_app.doctype.student_skill.student_skill import StudentSkill

		course: DF.Link | None
		department: DF.Link | None
		education: DF.Table[StudentEducation]
		email: DF.Data | None
		gender: DF.Literal["Male", "Female", "Others"]
		phone: DF.Phone | None
		resume: DF.Attach | None
		skills: DF.TableMultiSelect[StudentSkill]
		student_name: DF.Data | None
	# end: auto-generated types

	pass
