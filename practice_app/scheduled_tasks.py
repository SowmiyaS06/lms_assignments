# import frappe


# def my_hourly_task():
#     frappe.log_error(
#         "🔥 SCHEDULER TASK EXECUTED",
#         "Practice Scheduler Test"
#     )

import frappe


def process_todo(todo_name):

    todo = frappe.get_doc("ToDo", todo_name)

    frappe.log_error(
        title="🔥 Background Job Document Test",
        message=f"Processed ToDo: {todo.name}\nDescription: {todo.description}")


def create_todo_and_enqueue():

    todo = frappe.new_doc("ToDo")
    todo.description = "Background Job Test"
    todo.insert()

    frappe.enqueue(
        process_todo,
        todo_name=todo.name,
        queue="short",
        enqueue_after_commit=True
    )

    return todo.name


@frappe.whitelist()
def start_document_job():

    return create_todo_and_enqueue()


