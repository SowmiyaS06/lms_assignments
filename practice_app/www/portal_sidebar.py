import frappe

def get_context(context):
    context.show_sidebar = True
    context.title = "Portal Test"
    return context