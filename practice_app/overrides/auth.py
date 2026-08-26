import frappe


def validate_custom_auth():
    print("🔥 AUTH HOOK EXECUTED")

    if frappe.request:
        print("Request received:", frappe.request.path)