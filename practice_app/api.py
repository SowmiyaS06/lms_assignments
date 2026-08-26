import frappe

from pypika.enums import Order
from frappe.query_builder.functions import Count,Sum,Avg,Min,Max
from pypika import CustomFunction


# ============================================================================================
# LMS assignment Hooks (hooks.py), Hooks & Controllers (Python)

def custom_logic(doc,method=None):
    frappe.msgprint("Hook executed!")

# ============================================================================================



# =============================================================================================
#lms assignment Utilities (frappe.utils), Jinja API, Routing & Rendering & Search API
@frappe.whitelist()
def get_recent_todos():
    todos = frappe.get_list("ToDo",fields=["name", "description", "owner"],order_by="creation desc",limit_page_length=5)
    for todo in todos:
        todo["email"] = frappe.db.get_value("User",todo["owner"],"email")

    return {
        "timestamp": frappe.utils.now(),
        "records": todos
    }
# =============================================================================================



# lms assignment Document API, Database API, Query Builder & REST API
# lms Realtime & Logging
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
        "sql": sql,
        "sql2": sql2,
        "walk": parameters,
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

# utility functions
# http://127.0.0.1:8000/api/method/practice_app.api.get_current_datetime
# {"message":"2026-08-21 11:52:03.200903"}
from frappe.utils import now,getdate
@frappe.whitelist()
def get_current_datetime():
    return now()

# {"message":"2026-08-21"}
@frappe.whitelist()
def get_date():
    date1 = getdate()
    date2 = getdate("2000-03-18")

    return {
        "current_date": date1,
        "given_date":date2,
        "type": type(date1)
    }
    # return frappe.utils.getdate()


# {"message":"11:58:01.235714"}
@frappe.whitelist()
def get_time():
    return frappe.utils.nowtime()


# today()   - "2026-08-21" - string
# getdate() - datetime.date(2026,8,21) - date object
from frappe.utils import today
@frappe.whitelist()
def test_today():
    return today(),type(today())

# http://127.0.0.1:8000/api/method/practice_app.api.add_days
from frappe.utils import add_to_date
@frappe.whitelist()
def add_days():
    result = add_to_date(today(), days=10)
    return result


# http://127.0.0.1:8000/api/method/practice_app.api.calculate_date_difference?date_1=2025-08-15&date_2=2025-08-25
# both days_diff and date_diff does the same thing
from frappe.utils import date_diff
@frappe.whitelist()
def calculate_date_difference(date_1, date_2):
    difference = date_diff(date_2, date_1)

    return {
        "date_1": date_1,
        "date_2": date_2,
        "difference_in_days": difference
    }


from frappe.utils import month_diff
@frappe.whitelist()
def calculate_month_difference(date_1, date_2):
    difference = month_diff(date_2, date_1)

    return {
        "date_1": date_1,
        "date_2": date_2,
        "difference_in_months": difference
    }

# {"message":{"datetime":"2026-08-21 10:24:37.986303","pretty":"2 hours ago"}}
from frappe.utils import pretty_date
@frappe.whitelist()
def test_pretty_date():
    old_time = add_to_date(now(), hours=-2)
    return {
        "datetime": old_time,
        "pretty": pretty_date(old_time)
    }

# {
#   "message": {
#     "seconds": "50s",
#     "hours": "2h 46m 40s",
#     "days": "11d 13h 46m 40s"
#   }
# }
from frappe.utils import format_duration
@frappe.whitelist()
def test_format_duration():
    return {
        "seconds": format_duration(50),
        "hours": format_duration(10000),
        "days": format_duration(1000000)
    }


# http://127.0.0.1:8000/api/method/practice_app.api.test_comma_and
# "message":{"with_quotes":"'Apple', 'Ball', and 'Cat'","without_quotes":"Apple, Ball, and Cat"}}
from frappe.utils import comma_and
@frappe.whitelist()
def test_comma_and():
    return {
        "with_quotes": comma_and(["Apple", "Ball", "Cat"]),
        "without_quotes": comma_and(
            ["Apple", "Ball", "Cat"],
            add_quotes=False
        )
    }


# http://127.0.0.1:8000/api/method/practice_app.api.amount_in_words
from frappe.utils import money_in_words
@frappe.whitelist()
def amount_in_words():
    return {
        "inr": money_in_words(900),
        "usd": money_in_words(900.50, "USD"),
        "usd_cents": money_in_words(900.50, "USD", "Cents")
    }

# http://127.0.0.1:8000/api/method/practice_app.api.test_validate_json
from frappe.utils import validate_json_string
@frappe.whitelist()
def test_validate_json():
    try:
        # validate_json_string('[{"name": "Sowmi", "age": 21}]')
        validate_json_string('{name: "Sowmi"}')
        return "Valid JSON"
    except frappe.ValidationError:
        return "Invalid JSON"


# http://127.0.0.1:8000/api/method/practice_app.api.test_random_string
from frappe.utils import random_string
@frappe.whitelist()
def test_random_string():
    return random_string(10)


# from frappe.utils import mask_string
# @frappe.whitelist()
# def test_mask_string():
#     return mask_string("1234567890",mask_char="#",show_first=2,show_last=2)

# http://127.0.0.1:8000/api/method/practice_app.api.test_unique
from frappe.utils import unique
@frappe.whitelist()
def test_unique():
    # unique(("Apple", "Apple", "Banana", "Apple")) also preserves order so we use unique instead of set
    return unique([1, 2, 3, 1, 1, 4, 2])


from frappe.utils.pdf import get_pdf
@frappe.whitelist()
def test_get_pdf():
    html = """
    <h1>Student Report</h1>
    <p>Name: Sowmi</p>
    <p>Department: Information Technology</p>
    """
    frappe.local.response.filename = "student_report.pdf"
    frappe.local.response.filecontent = get_pdf(html)
    frappe.local.response.type = "pdf"


# http://127.0.0.1:8000/api/method/practice_app.api.test_get_abbr
from frappe.utils import get_abbr
@frappe.whitelist()
def test_get_abbr():
    return {
        "single": get_abbr("Gavin"),
        "multiple": get_abbr("Coca Cola Company"),
        "custom": get_abbr("Mohammad Hussain Nagaria", max_len=3)
    }


# http://127.0.0.1:8000/api/method/practice_app.api.check_url?url=https://google.com
# http://127.0.0.1:8000/api/method/practice_app.api.check_url?url=google
from frappe.utils import validate_url
@frappe.whitelist()
def check_url(url):
    result = validate_url(url)

    return {
        "url": url,
        "valid": result
    }


# http://127.0.0.1:8000/api/method/practice_app.api.check_email
from frappe.utils import validate_email_address
@frappe.whitelist()
def check_email():
    return {
        "valid": validate_email_address("sowmi@example.com"),
        "invalid": validate_email_address("hello"),
        "multiple": validate_email_address(
            "sowmi@example.com, test@example.com"
        )
    }

# http://127.0.0.1:8000/api/method/practice_app.api.check_phone
from frappe.utils import validate_phone_number
@frappe.whitelist()
def check_phone():
    return {
        "valid": validate_phone_number("+91-75385837"),
        "invalid": validate_phone_number("invalid")
    }


# {"message":[83,111,119,109,105]} byte values
@frappe.whitelist()
def test_cache():
    cache = frappe.cache()
    cache.set("student_name", "Sowmi")
    return cache.get("student_name")


@frappe.whitelist()
def test_sendmail():
    frappe.sendmail(
        recipients=["your-email@example.com"],
        subject="Test Email from Frappe",
        message="Hello! This email was sent using frappe.sendmail()."
    )
    return "Email sent successfully"



from frappe.utils import get_filtered_list_url
@frappe.whitelist()
def test_filtered_list_url():
    return get_filtered_list_url(
        "Work Order",
        [
            "MFG-WO-2025-00027",
            "MFG-WO-2025-00028"
        ]
    )



# _________________________________________________________________________________________________
# Jinja API

@frappe.whitelist()
def currency_format(currency):
    return frappe.format(
        currency,
        {"fieldtype": "Currency"}
    )

@frappe.whitelist
def format_date(date):
    return frappe.format_date(date)

@frappe.whitelist
def geturl():
    return frappe.get_url()

@frappe.whitelist()
def get_job():
    job = frappe.get_doc("Job Application","446")
    return job    

@frappe.whitelist()
def get_job_all():
    job=frappe.get_all(
        "Job Application",
        fields=["applicant_name"]
    )
    return job

@frappe.whitelist()
def get_job_list():
    job=frappe.get_list(
        "Job Application",
        fields=["applicant_name","status"]
    )
    return job

@frappe.whitelist()
def get_applicant_name():
    applicant = frappe.db.get_value("Job Application","446","applicant_name")
    return applicant

@frappe.whitelist()
def single_doc():
    timezone=frappe.get_single_value("System Settings","timezone")
    return timezone

@frappe.whitelist()
def system_settings():
    country=frappe.get_system_settings("country")
    if country=="India":
        return "razorpay",country
    else:
        return "Paypal"


@frappe.whitelist()
def get_job_meta():
    meta = frappe.get_meta("Job Application")
    return {
        "doctype": meta.name,
        "fields": len(meta.fields)
    }

from frappe.utils import get_fullname
@frappe.whitelist()
def get_current_user_info():
    return {
        "user": frappe.session.user,
        "fullname": frappe.get_fullname()
    }

# ------------------------------------------------------------------------------------------
@frappe.whitelist()
def  get_vehicle():
    query=frappe.qb.get_query("Vehicle Service",
    fields=[
        "name", "customer_name as customer", "brand","vehicle.registration_date as date",
        # same for max,min,abs,
            # {
            #     "SUM":"amount",
            #     "as":"total"
            # },
            # {
            #     "AVG": "amount",
            #     "as": "average_amount"
            # },
            # {
            #     "CONCAT":["customer_name","' '","amount"],
            #     "as":"bill"
            # }
            ],
            filters=[
            ["service_type", "!=", "General Service"]
            # "and",
            # ["service_status", "=", "Completed"]
        ],order_by="customer_name asc",
        limit=6,
        ignore_permissions=False
        # user="test@example.com"
        )
    vehicle=query.run(as_dict=True)
    sql_string = query.get_sql()
    # return sql_string
    return vehicle

@frappe.whitelist()
def get_applicants():
    query = frappe.qb.get_query(
        "Job Application",
        fields=["name","applicant_name",{
            "skills":["skill","experience"],
        }, {
            "IFNULL":["hr_remarks","'no remarks'"],
            "as":"hr_remarks"
        },
        {
            "EXTRACT": ["'YEAR'", "application_date"],
            "as": "application_year"
       },
       {
           "NOW":[],
           "as":"now"
       }])

    job = query.run(as_dict=True)

    return job


@frappe.whitelist()
def get_vehicle_services():
    vehicle = frappe.qb.DocType("Vehicle Service")#pypika object
    query = frappe.qb.get_query(
        "Vehicle Service",
        fields=[
            "name",
            "customer_name",
            "amount"
        ],
        filters=vehicle.amount > 5000
    )
    result = query.run(as_dict=True)
    return result




# ------------------------------------------------------------------------------------
def process_todo(todo_name):
    todo = frappe.get_doc("ToDo", todo_name)
    frappe.log_error(
        title="🔥 Background Job Document Test",
        message=f"Processed ToDo: {todo.name}\nDescription: {todo.description}"
    )

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





@frappe.whitelist()
def test_job_application_permissions():

    query = frappe.qb.get_query(
        "Job Application",
        fields=[
            "name",
            "applicant_name",
            "email_id",
            "job_title",
            "owner"
        ],
        ignore_permissions=False
    )

    return {
        "sql": query.get_sql(),
        "results": query.run(as_dict=True)
    }





