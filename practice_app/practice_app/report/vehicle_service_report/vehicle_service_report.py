import frappe


def execute(filters=None):
    columns = [
        {
            "label": "Vehicle",
            "fieldname": "vehicle",
            "fieldtype": "Link",
            "options": "Vehicle",
            "width": 150
        },
        {
            "label": "Service Type",
            "fieldname": "service_type",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Mechanic",
            "fieldname": "mechanic",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Amount",
            "fieldname": "amount",
            "fieldtype": "Currency",
            "width": 120
        }
    ]

    data = [
        {
            "vehicle": "TN01AB1234",
            "service_type": "Oil Change",
            "mechanic": "Arun",
            "amount": 1500
        },
        {
            "vehicle": "TN02CD5678",
            "service_type": "Brake Service",
            "mechanic": "Kumar",
            "amount": 2500
        },
        {
            "vehicle": "TN03EF9012",
            "service_type": "General Service",
            "mechanic": "Ravi",
            "amount": 3000
        }
    ]

    return columns, data