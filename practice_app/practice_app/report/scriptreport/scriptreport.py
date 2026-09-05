# Copyright (c) 2026, Sowmiya and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	project=frappe.qb.DocType("Project")
	projectemployee=frappe.qb.DocType("Project Employee")
	query=(
		frappe.qb.from_(project)
		.join(projectemployee)
		.on(project.name==projectemployee.parent)
	    .select(
        project.project_name,
    	project.project_manager,
        projectemployee.employee,
        projectemployee.role,
        projectemployee.hours_allocated,
        projectemployee.hours_worked
    )
	)
	columns = get_columns()
	data = query.run(as_dict=True)

	return columns, data


def get_columns() -> list[dict]:
	return [
		{
			"label": _("Project Name"),
			"fieldname": "project_name",
			"fieldtype": "Data",
		},
		{
			"label": _("Project Manager"),
			"fieldname": "project_manager",
			"fieldtype": "Link",
			"options": "Employee",
		},
		{
			"label": _("Employee"),
			"fieldname": "employee",
			"fieldtype": "Link",
			"options": "Employee",
		},
		{
			"label": _("Role"),
			"fieldname": "role",
			"fieldtype": "Data",
		},
		{
			"label": _("Hours Allocated"),
			"fieldname": "hours_allocated",
			"fieldtype": "Float",
		},
		{
			"label": _("Hours Worked"),
			"fieldname": "hours_worked",
			"fieldtype": "Float",
		},
	]

def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	return [
		["Row 1", 1],
		["Row 2", 2],
	]



