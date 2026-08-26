import frappe


def todo_before_insert(doc, method=None):
    print("BEFORE INSERT")
    print("Description:", doc.description)


def todo_after_insert(doc, method=None):
    print("AFTER INSERT")
    print("Created ToDo:", doc.name)


def todo_on_update(doc, method=None):
    print("ON UPDATE")
    print("Updated ToDo:", doc.name)


def todo_on_trash(doc, method=None):
    print("ON TRASH")
    print("Deleted ToDo:", doc.name)