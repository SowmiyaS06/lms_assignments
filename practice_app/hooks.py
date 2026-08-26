app_name = "practice_app"
app_title = "Practice App"
app_publisher = "Sowmiya"
app_description = "Practice app for learning frappe"
app_email = "sowmiyaselvaraj9025@gmail.com"
app_license = "mit"
app_include_js = "custom_desk.bundle.js"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "practice_app",
# 		"logo": "/assets/practice_app/logo.png",
# 		"title": "Practice App",
# 		"route": "/practice_app",
# 		"has_permission": "practice_app.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/practice_app/css/practice_app.css"
# app_include_js = "/assets/practice_app/js/practice_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/practice_app/css/practice_app.css"
# web_include_js = "/assets/practice_app/js/practice_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "practice_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "practice_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "practice_app.utils.jinja_methods",
# 	"filters": "practice_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "practice_app.install.before_install"
# after_install = "practice_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "practice_app.uninstall.before_uninstall"
# after_uninstall = "practice_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "practice_app.utils.before_app_install"
# after_app_install = "practice_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "practice_app.utils.before_app_uninstall"
# after_app_uninstall = "practice_app.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "practice_app.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "practice_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"practice_app.tasks.all"
# 	],
# 	"daily": [
# 		"practice_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"practice_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"practice_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"practice_app.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "practice_app.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "practice_app.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "practice_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "practice_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["practice_app.utils.before_request"]
# after_request = ["practice_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["practice_app.utils.before_job"]
# after_job = ["practice_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"practice_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True
export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []
bench_commands = "practice_app.commands:commands"


# ======================================================================================
# LMS Assignment
doc_events={
"Test Document":{
    "validate":"practice_app.api.custom_logic"
}
}
# ======================================================================================


# =======================================================================================
#LMS Assignment Background Jobs
scheduler_events={
    "daily":[
        "practice_app.tasks.daily_maintainance"
    ]
}
# =======================================================================================





# hooks

app_include_js = "/assets/practice_app/js/app.js"

app_include_css = "/assets/practice_app/css/app.css"

web_include_js = "/assets/practice_app/js/app-web.js"
web_include_css = "/assets/practice_app/css/app-web.css"

webform_include_js = {
    "Job Application": "public/js/custom_job_application.js"
}

webform_include_css = {
    "Job Application": "public/css/custom_job_application.css"
}

page_js = {
    "background_jobs": "public/js/custom_background_jobs.js"
}

# sounds = [
#     {
#         "name": "ping",
#         "src": "/assets/practice_app/sounds/ping.mp3",
#         "volume": 0.2
#     }
# ]

before_migrate = "practice_app.migrate.before_migrate"

after_migrate = "practice_app.migrate.after_migrate"

after_build = "practice_app.build.after_build"

# before_tests = "practice_app.tests.test_setup.before_tests"

# before_write_file = "practice_app.overrides.file.before_write"
write_file = "practice_app.overrides.file.write_file"
# delete_file_data_content = "practice_app.overrides.file.delete_file"

# get_sender_details = "practice_app.overrides.email.get_sender_details"
# override_email_send = "practice_app.overrides.email.send"

extend_bootinfo = "practice_app.boot.boot_session"

website_context = {
    "favicon": "/assets/practice_app/images/favicon.png",
    "company_name": "Practice School"
}
update_website_context = "practice_app.overrides.website_context.website_context"
    
extend_website_page_controller_context = {
    "frappe.www.404": "practice_app.pages.context_404"
} 

website_catch_all="404"

# website_path_resolver = "practice_app.practice_app.utils.path_resolver.custom_resolver"

website_route_rules = [
    {
        "from_route": "/job_application/<name>",
        "to_route": "job_application"
    }
]

website_redirects = [
    {
        "source": "/job_application",
        "target": "/test"
    }
]

website_clear_cache = "practice_app.overrides.website.clear_website_cache"

# home_page = "homepage"

portal_menu_items = [
    {
        "title": "Dashboard",
        "route": "/dashboard"
    },
    {
        "title": "Courses",
        "route": "/courses"
    },
    {
        "title": "Attendance",
        "route": "/attendance"
    }
]

brand_html = '<div>Practice School</div>'


# base_template = "practice_app/templates/my_custom_base.html"
braintree_success_page = "practice_app.integrations.braintree_success_page"

# calendars = ["Attendance"]

clear_cache = "practice_app.cache.clear_cache"

default_mail_footer = """
<div>
    Sent via <strong>Practice School</strong>
</div>
"""

on_login = "practice_app.overrides.login.successful_login"

on_session_creation = "practice_app.overrides.login.session_created"

on_logout = "practice_app.overrides.login.user_logged_out"

auth_hooks = [
    "practice_app.overrides.auth.validate_custom_auth"
]

# filters can also be applied for this fixtures
# bench --site school.local export-fixtures
fixtures = [
    "Job Application"
]

permission_query_conditions={
    "Job Application":"practice_app.permissions.permission_query"
}

# frappe.has_permission("Job Application", doc=doc, ptype="write")
has_permission = {
    "Job Application": "practice_app.permissions.job_application_has_permission"
}

doctype_js = {
    "ToDo": "public/js/todo.js"
}

# doc_events = {
#     "ToDo": {
#         "before_insert": "practice_app.crud_events.todo_before_insert",
#         "after_insert": "practice_app.crud_events.todo_after_insert",
#         "on_update": "practice_app.crud_events.todo_on_update",
#         "on_trash": "practice_app.crud_events.todo_on_trash"
#     }
# }

doctype_list_js = {
    "ToDo": "public/js/todo_list.js"
}

ignore_links_on_delete = ["Applicant Skill"] 
# simply tells Frappe not to block the <doctype> deletion because that ToDo has a link to it.

# scheduler_events = {
#     "cron":{
#     "*/2 * * * *": [
#         "practice_app.scheduled_tasks.my_hourly_task"
#     ]
#     }
# }

# additional_timeline_content = {
#     "Job Application": [
#         "practice_app.timeline.job_application_timeline"
#     ]
# }

# extend_doctype_class = {
#     "Job Application": [
#         "practice_app.extensions.job_application.JobApplicationMixin"
#     ]
# }

override_doctype_class = {
    "Job Application":
        "practice_app.overrides.job_application.CustomJobApplication"
}


