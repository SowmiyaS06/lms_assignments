import frappe
def daily_maintainance():
    frappe.log_error(title="Daily maintenance",message="Daily maintenance task executed!")
