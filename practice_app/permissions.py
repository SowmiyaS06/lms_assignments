import frappe

def permission_query(user):
    if not user:
        user=frappe.session.user

    return "`tabJob Application`.status='Selected'"


def job_application_has_permission(doc,user=None,permission_type=None):
    if permission_type == "read" and doc.status == "Selected":
        return True

    return False