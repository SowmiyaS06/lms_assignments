import frappe


def before_tests():
    if not frappe.db.exists("Student", {"student_name": "Test Student"}):
        frappe.get_doc({
            "doctype": "Student",
            "student_name": "Test Student",
            "age": 20
        }).insert(ignore_permissions=True)

    frappe.db.commit()