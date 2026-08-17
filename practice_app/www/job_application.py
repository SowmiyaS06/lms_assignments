import frappe

def get_context(context):
    application_name = frappe.form_dict.name

    context.application = frappe.get_doc(
        "Job Application",
        application_name
    )

    return context