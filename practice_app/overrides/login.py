import frappe

def successful_login(login_manager):
    print("=====================================")
    print("🔥 ON_LOGIN HOOK EXECUTED")
    print("Logged in user:", frappe.session.user)
    print("=====================================")

def session_created(login_manager):
    print("=====================================")
    print("🔥 SESSION CREATION HOOK EXECUTED")
    print("Session user:", frappe.session.user)
    print("=====================================")


def user_logged_out(login_manager):
    print("=====================================")
    print("Logout hook executed")
    print("Logout user:", frappe.session.user)
    print("=====================================")
