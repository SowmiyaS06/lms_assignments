# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class JobApplication(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF
        from practice_app.practice_app.doctype.applicant_skill.applicant_skill import ApplicantSkill

        applicant_name: DF.Data | None
        application_date: DF.Date | None
        current_salary: DF.Currency
        email: DF.Data | None
        expected_salary: DF.Currency
        experience: DF.Float
        hr_remarks: DF.SmallText | None
        interview_date: DF.Date | None
        name: DF.Int | None
        naming_series: DF.Data | None
        phone: DF.Phone | None
        position_applied: DF.Literal["Software Engineer", "Frontend Developer", "Backend Developer", "Full Stack Developer", "Python Developer", "Frappe Developer", "Java Developer", "QA Engineer", "DevOps Engineer", "UI/UX Designer", "Data Analyst", "AI/ML Engineer", "Intern"]
        resume: DF.Attach | None
        skills: DF.Table[ApplicantSkill]
        status: DF.Literal["Draft", "Applied", "Under Review", "Shortlisted", "Interview Scheduled", "Interview Completed", "Selected", "Rejected", "Offer Sent", "Joined", "Cancelled"]
    # end: auto-generated types

    # def before_save(self):
        # doc = frappe.get_doc("Job Application", self.name)
        # frappe.msgprint(doc.applicant_name)
        # frappe.msgprint(f"""
        # Applicant Name: {doc.applicant_name}<br>
        # Email: {doc.email}<br>
        # Phone: {doc.phone}<br>
        # Position Applied: {doc.position_applied}<br>
        # Experience: {doc.experience}<br>
        # Current Salary: {doc.current_salary}<br>
        # Expected Salary: {doc.expected_salary}<br>
        # Application Date: {doc.application_date}<br>
        # Interview Date: {doc.interview_date}<br>
        # Status: {doc.status}<br>
        # HR Remarks: {doc.hr_remarks}
        # """)
        # doc = frappe.get_last_doc("Job Application")

        # frappe.msgprint(f"""
        # Applicant Name: {doc.applicant_name}<br>
        # Email: {doc.email}<br>
        # Position: {doc.position_applied}<br>
        # Status: {doc.status}
        # """)

        # doc = frappe.new_doc("Job Application")

        # doc.applicant_name = "Sowmiya"
        # doc.email = "sowmiya@gmail.com"
        # doc.position_applied = "Frappe Developer"
        # doc.status = "Applied"
        # doc.save()

        # frappe.delete_doc("Job Application", "282")

        # frappe.rename_doc("Job Application","283","200")
        
        # meta = frappe.get_meta("Job Application")
        # field = meta.get_field("status")
        # frappe.msgprint(field.label)
        # frappe.msgprint(field.fieldname)
        # frappe.msgprint(field.fieldtype)
        # frappe.msgprint(field.reqd)
        # frappe.msgprint(field.read_only)
        # frappe.msgprint(field.options)


        # frappe.only_for("Accounts Manager")
        # frappe.msgprint("Welcome System Manager")


# @frappe.whitelist()
# def create_application():
#     doc = frappe.new_doc("Job Application")

#     doc.applicant_name = "Sowmiya"
#     doc.email = "sowmiyaselvaraj9025@gmail.com"
#     doc.phone = "+919876543210"
#     doc.experience = 9.2

#     doc.insert()

#     return doc

# @frappe.whitelist()
# def update_employee():
#     doc = frappe.get_doc("Job Application", "433")

#     doc.applicant_name = "Sowmiya Selvaraj"

#     doc.save()

#     return doc

# @frappe.whitelist()
# def delete_application(docname):
#     doc = frappe.get_doc("Job Application", docname)

#     doc.delete()

#     return "Deleted Successfully"

#     # def before_save(self):
#     #     old_doc = self.get_doc_before_save()
 
#     #     if old_doc and old_doc.current_salary != self.current_salary:
#     #         frappe.msgprint(
#     #         f"Salary changed from {old_doc.current_salary} to {self.current_salary}"
#     #         )

#     #     if self.has_value_changed("status"):
#     #         frappe.msgprint("Status Changed")

# @frappe.whitelist()
# def reload_example():
#     doc = frappe.get_doc("Job Application", "424")
#     frappe.msgprint(doc.status)
#     doc.db_set("status", "Selected")
#     frappe.msgprint("Status updated to 'Selected'")
#     doc.reload()
#     frappe.msgprint(doc.status)  

# @frappe.whitelist()
# def check_write_permission(docname):
#     doc = frappe.get_doc("Job Application", docname)
#     doc.check_permission("write")
#     frappe.msgprint("You have Write Permission")

# @frappe.whitelist()
# def get_application_title(docname):
#     doc = frappe.get_doc("Job Application", docname)
#     title = doc.get_title()
#     frappe.msgprint(str(title))
#     return title

# @frappe.whitelist()
# def update_status(docname):
#     doc = frappe.get_doc("Job Application", docname)
#     doc.status = "Draft"
#     doc.save()
#     doc.notify_update()
#     return "Status Updated"

# @frappe.whitelist()
# def add_skill(docname):

#     doc = frappe.get_doc("Job Application", docname)
#     doc.append("skills", {
#         "skill": "Python",
#         "experience": 3
#     })
#     doc.save()
#     return "Skill Added"

# @frappe.whitelist()
# def get_application_url(docname):
#     doc = frappe.get_doc("Job Application", docname)
#     url = doc.get_url()
#     frappe.msgprint(url)
#     return url

# @frappe.whitelist()
# def add_comment(docname):
#     doc=frappe.get_doc("Job Application", docname)
#     doc.add_comment("Comment", "This is a comment added to the Job Application.")
#     doc.save()
#     return "Comment Added Successfully"

    # def before_save(self):
    #     if self.has_value_changed("status") and self.status == "Selected":
    #         self.add_comment(
    #             "Comment",
    #             "Candidate was selected by the HR Manager."
    #         )

# @frappe.whitelist()
# def select_candidate(docname):

#     doc = frappe.get_doc("Job Application", docname)
#     doc.db_set(
#         "status",
#         "Selected",
#         notify=True
#     )
#     return "Candidate Selected"

    # def on_update(self):
        # self.add_seen()
        # self.add_viewed()
    #     if self.experience >= 5:
    #         self.add_tag("Experienced")
    #     frappe.msgprint(str(self.get_tags()))

