import frappe

from pypika.enums import Order
from frappe.query_builder.functions import Count,Sum,Avg,Min,Max
from pypika import CustomFunction

# lms assignment
# --------------------------------------------------------------------------------------------
@frappe.whitelist()
def job_application_assignment():
    JobApplication = frappe.qb.DocType("Job Application")
    ApplicantSkill = frappe.qb.DocType("Applicant Skill")
    query = (
        frappe.qb
        .from_(JobApplication)
        .inner_join(ApplicantSkill)
        .on(
            ApplicantSkill.parent == JobApplication.name
        )
        .select(
            JobApplication.name,
            JobApplication.applicant_name,
            JobApplication.status,
            ApplicantSkill.skill,
            ApplicantSkill.experience,
            ApplicantSkill.rating
        )
        .limit(5)
    )

    result = query.run(as_dict=True)
    if result:
        first_application = frappe.get_doc(
            "Job Application",
            result[0]["name"]
        )
        first_application.hr_remarks = "Updated through Assignment API"
        first_application.save()
    for record in result:
        frappe.db.set_value(
            "Job Application",
            record["name"],
            "status",
            "Under Review"
        )
    return result
# --------------------------------------------------------------------------------------------


# http://127.0.0.1:8000/api/method/practice_app.api.test_get_list
@frappe.whitelist()
def test_get_list():
    return frappe.db.get_list(
        "Job Application",
        filters={
            "status": "Selected"
            # "experience": [">", 2]
        },
        fields=[
            "name",
            "applicant_name",
            "experience",
            "expected_salary",
            "position_applied"
        ],
        order_by="expected_salary desc",
        start=0,
        page_length=5
    )

# http://127.0.0.1:8000/api/method/practice_app.api.test_get_all
@frappe.whitelist()
def test_get_all():
    return frappe.db.get_all(
        "Job Application",
         filters={
            "experience": [">", 2]
        },
        or_filters=[
        ["status", "=", "Rejected"],
        ["status", "=", "Selected"]
        ],
        fields=[
            "name",
            "applicant_name",
            "status"
        ]
    )

#retrives a particular field value from one document
@frappe.whitelist()
def test_get_value():
    return frappe.db.get_value(
        "Job Application",
        "435",
        ["applicant_name", "status", "expected_salary","hr_remarks"],
        as_dict=True
    )

@frappe.whitelist()
def test_get_single_value():
    return frappe.db.get_single_value(
        "single_doc",
        "name"
    )
# frappe.db.get_single_value(
#     "System Settings",
#     "time_zone"
# )

@frappe.whitelist()
def test_set_value():
    result = frappe.db.set_value(
        "Job Application",
        "435",
        {
            "status": "Rejected",
            "hr_remarks": "Good technical experience",
            "expected_salary": 60000
        }
    )

    frappe.db.commit()

    return {
        "message": "Job Application 435 updated"
    }

@frappe.whitelist()
def test_exists():
    return frappe.db.exists(
        "Job Application",
        {
            "status": "Rejected",
            "position_applied": "Python Developer"
        }
    )

@frappe.whitelist()
def test_count():
    return frappe.db.count("Job Application")

@frappe.whitelist()
def test_delete():
    frappe.db.delete(
        "Job Application",
        {
            "name": "436"
        }
    )

    frappe.db.commit()

    return {
        "message": "Deleted"
    }


@frappe.whitelist()
def test_savepoint():

    

    frappe.db.set_value(
        "Job Application",
        "435",
        "status",
        "Selected"
    )

    frappe.db.set_value(
        "Job Application",
        "435",
        "hr_remarks",
        "Selected for next round"
    )
    frappe.db.savepoint("before_changes")

    return {
        "message": "Changes made after savepoint"
    }

@frappe.whitelist()
def test_rollback():

    frappe.db.set_value(
        "Job Application",
        "435",
        "status",
        "Selected"
    )

    frappe.db.savepoint("before_remarks")

    frappe.db.set_value(
        "Job Application",
        "435",
        "hr_remarks",
        "Selected for next round"
    )

    frappe.db.rollback(save_point="before_remarks")
    frappe.db.commit()
    return {
        "message": "Rolled back to before_remarks"
    }

@frappe.whitelist()
def test_sql():
    return frappe.db.sql("""
        SELECT
            name,
            applicant_name,
            status,
            expected_salary
        FROM `tabJob Application`
    """, as_dict=True)

@frappe.whitelist()
def test_describe():
    return frappe.db.describe("Job Application")

@frappe.whitelist()
def test_change_column_type():
    frappe.db.change_column_type(
    "Job Application",
    "experience",
    "int"
    )

@frappe.whitelist()
def test_add_index():
    frappe.db.add_index(
        "Job Application",
        ["status"],
        "job_application_status_idx"
    )

    return {
        "message": "Index created"
    }

@frappe.whitelist()
def test_add_unique():
    frappe.db.add_unique(
        "Job Application",
        ["applicant_name"],
        "job_application_email_unique"
    )

    return {
        "message": "Unique constraint created"
    }

@frappe.whitelist()
def test_bulk_update():

    frappe.db.bulk_update(
        "Job Application",
        {
            "435": {
                "status": "Selected"
            },

            "436": {
                "status": "Rejected"
            },

            "437": {
                "status": "Under Review"
            }
        }
    )
    frappe.db.commit()
    return {
        "message": "Bulk update completed"
    }

# query builder
@frappe.whitelist()
def get_job_applications():

    JobApplication = frappe.qb.DocType("Job Application")

    query = (
        frappe.qb
        .from_(JobApplication)
        .select(
            # JobApplication.name,
            # JobApplication.applicant_name,
            Min(JobApplication.expected_salary).as_("minimum_salary"),
            Max(JobApplication.expected_salary).as_("maximum_salary"),
            Avg(JobApplication.expected_salary).as_("average_salary"),
            Sum(JobApplication.expected_salary).as_("total_salary"),
            JobApplication.status,
            Count("*").as_("total")
        )
        .where(
            (JobApplication.status=="Selected") |
            (JobApplication.status=="Draft")
        )
        .groupby(JobApplication.status)
        .orderby(JobApplication.creation, order=Order.desc)
        .limit(2)
    )

    sql = str(query)
    sql2 = query.get_sql()
    parameters = query.walk()

    result = query.run(as_dict=True)

    return {
        # "sql": sql,
        # "sql2": sql2,
        # "walk": parameters,
        "result": result
    }

import frappe
from frappe.query_builder.functions import Avg


@frappe.whitelist()
def get_above_average_applications():

    JobApplication = frappe.qb.DocType("Job Application")

    average_salary = (
        frappe.qb
        .from_(JobApplication)
        .select(
            Avg(JobApplication.expected_salary)
        )
    )

    query = (
        frappe.qb
        .from_(JobApplication)
        .select(
            JobApplication.name,
            JobApplication.applicant_name,
            JobApplication.expected_salary
        )
        .where(
            JobApplication.expected_salary > average_salary
        )
    )

    result = query.run(as_dict=True)

    return result

@frappe.whitelist()
def get_job_application_age():

    JobApplication = frappe.qb.DocType("Job Application")

    DateDiff = CustomFunction(
        "DATE_DIFF",
        ["interval", "start_date", "end_date"]
    )

    query = (
        frappe.qb
        .from_(JobApplication)
        .select(
            JobApplication.name,
            JobApplication.applicant_name,
            DateDiff(
                "day",
                JobApplication.creation,
                frappe.qb.functions.CurDate()
            ).as_("days_old")
        )
    )

    sql = str(query)
    result = query.run(as_dict=True)

    return {
        "sql": sql,
        "result": result
    }