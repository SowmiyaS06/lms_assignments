// Copyright (c) 2026, Sowmiya and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Client_Script", {
// 	refresh(frm) {

// 	},
// });
//setup runs only once when the form is initialized in the browser
frappe.ui.form.on("Client_Script", {
    setup(frm) {
        frm.set_query("manager", function () {//set_query is used for filtering
            return {
                filters: {
                    enabled: 1,
                    user_type: "System User"
                }
            };
        });
    }
});

frappe.ui.form.on("Client_Script", {
    before_load(frm) {

        if (!frm.doc.remarks) {
            frm.set_value("remarks", "Loaded using before_load");//set value triggers the field change event
        }

    }
});

frappe.ui.form.on("Client_Script", {
    onload(frm) {
//frm.set_df_property(fieldname, property, value); syntax
        frm.set_df_property("total_salary", "read_only", 1);
        //frm.set_df_property("bonus", "hidden", 1);
        frm.set_df_property("remarks", "reqd", 1);
        frm.set_df_property("employee_name", "label", "Employee Full Name");

    }
});

// frappe.ui.form.on("Client_Script", {
//     refresh(frm) {

//         frm.add_custom_button("Calculate Salary", function () {

//             let total = (frm.doc.salary || 0) + (frm.doc.bonus || 0);

//             frm.set_value("total_salary", total);

//         });

//     }
// });

frappe.ui.form.on("Client_Script", {
    onload_post_render(frm) {

        frm.set_intro(
            "Welcome! Please fill in all employee details.",
            "red"
        );

    }
});

frappe.ui.form.on("Client_Script", {
    validate(frm) {

        if (frm.doc.bonus > frm.doc.salary) {
            frappe.throw("Bonus cannot be greater than Salary.");
        }

    }
});

frappe.ui.form.on("Client_Script", {
    before_save(frm) {

        if (frm.doc.employee_name) {

            frm.set_value(
                "employee_name",
                frm.doc.employee_name.toUpperCase()
            );

        }

    }
});

frappe.ui.form.on("Client_Script", {
    after_save(frm) {

        if (frm.doc.status === "Active") {

            frappe.show_alert({
                message: "Employee is Active",
                indicator: "green"
            });

        } else {

            frappe.show_alert({
                message: "Employee is Inactive",
                indicator: "orange"
            });

        }

    }
});

frappe.ui.form.on("Client_Script", {
    before_submit(frm) {

        if (frm.doc.salary < 10000) {
            frappe.throw("Salary must be at least 10000 before submission.");
        }

    }
});

frappe.ui.form.on("Client_Script", {
    on_submit(frm) {

        frappe.show_alert({
            message: "Employee record submitted successfully!",
            indicator: "green"
        });

    }
});

frappe.ui.form.on("Client_Script", {
    before_cancel(frm) {

        if (frm.doc.status === "Active") {
            frappe.throw("Active employees cannot be cancelled.");
        }

    }
});

frappe.ui.form.on("Client_Script", {
    after_cancel(frm) {

        frappe.show_alert({
            message: "Employee record cancelled successfully!",
            indicator: "red"
        });

    }
});

frappe.ui.form.on("Client_Script", {
    before_discard(frm) {

        if (frm.is_new()) {
            frappe.msgprint("Discarding a new document.");
        }

    }
});

frappe.ui.form.on("Client_Script", {
    timeline_refresh(frm) {

        frm.add_custom_button("Timeline Button", function () {
            frappe.msgprint("Timeline Button Clicked");
        });

    }
});

frappe.ui.form.on("Client_Script", {
    experience(frm) {

        if (frm.doc.experience >= 10) {
            frm.set_value("designation", "Team Lead");
        }
        else if (frm.doc.experience >= 5) {
            frm.set_value("designation", "Senior Developer");
        }
        else {
            frm.set_value("designation", "Junior Developer");
        }

    }
});

frappe.ui.form.on("Project Details", {
    projects_add(frm, cdt, cdn) {

        let row = locals[cdt][cdn];

        row.status = "Pending";

        frm.refresh_field("projects");
    }
});

// frappe.ui.form.on("Project Details", {
//     projects_add(frm, cdt, cdn) {

//         let row = locals[cdt][cdn];

//         row.hours = 8;

//         frm.refresh_field("projects");
//     }
// });

frappe.ui.form.on("Project Details", {
    hours(frm, cdt, cdn) {

        let row = locals[cdt][cdn];

        row.cost = row.hours * 500;

        frm.refresh_field("projects");
    }
});

// frappe.ui.form.on("Project Details", {
//     before_projects_remove(frm, cdt, cdn) {
//         frappe.throw("Delete blocked");
//     }
// });

frappe.ui.form.on("Project Details", {
    hours(frm, cdt, cdn) {
        frappe.throw("Hours event is working");
    }
});

frappe.ui.form.on("Project Details", {
    projects_remove(frm, cdt, cdn) {
        frappe.throw("projects_remove fired");
    }
});

// frappe.ui.form.on("Project Details", {
//     projects_move(frm) {

//         frm.doc.projects.forEach((row, index) => {
//             row.project_no = index + 1;
//         });

//         frm.refresh_field("projects");
//     }
// });

frappe.ui.form.on("Project Details", {
    projects_move(frm) {
        frappe.msgprint("Row Moved");
    }
});

frappe.ui.form.on("Project Details", {
    form_render(frm, cdt, cdn) {

        let row = locals[cdt][cdn];

        if (row.status === "Completed") {
            frappe.meta.get_docfield(
                "Project Details",
                "cost",
                frm.doc.name
            ).read_only = 1;

            frm.refresh_field("projects");
        }

    }
});

frappe.ui.form.on("Client_Script", {
    status(frm) {

        frm.toggle_enable(
            "salary",
            frm.doc.status === "Active"
        );

    }
});

frappe.ui.form.on("Client_Script", {
    status(frm) {

        frm.toggle_display(
            "remarks",
            frm.doc.status === "Inactive"
        );

    }
});

frappe.ui.form.on("Client_Script", {
    department(frm) {

        frm.toggle_reqd(
            "manager",
            frm.doc.department === "IT"
        );

    }
});

// frappe.ui.form.on("Client_Script", {
//     refresh(frm) {

//         frm.doc.salary = 50000;

//         frm.refresh_field("salary");

//     }
// });

// frappe.ui.form.on("Client_Script", {
//     refresh(frm) {

//         frm.add_custom_button("Add Overtime", function () {

//             frm.doc.projects.forEach(row => {
//                 row.hours = (row.hours || 0) + 2;
//             });

//             frm.refresh_field("projects");

//         });

//     }
// });

// frappe.ui.form.on("Client_Script", {
//     refresh(frm) {

//         frm.add_custom_button("Add Default Project", function () {

//             let row = frm.add_child("projects");

//             row.project_name = "ERP Development";
//             row.hours = 8;
//             row.cost = 4000;
//             row.status = "Pending";

//             frm.refresh_field("projects");

//         });

//     }
// });

frappe.ui.form.on("Client_Script", {
    refresh(frm) {
        frm.add_custom_button("Send Email", () => {
            frm.email_doc();
        });
    },

    get_email_recipients(frm, field) {

        if (field === "recipients") {
            return [
                frm.doc.email
            ];
        }

        if (field === "cc") {
            return [
                "manager@company.com",
                "hr@company.com"
            ];
        }

    }
});

frappe.ui.form.on("Client_Script", {
    refresh(frm) {

        frm.add_custom_button("Calculate Bonus", function () {

            frm.call("calculate_bonus")
                .then(r => {

                    frm.set_value("bonus", r.message);

                });

        });

    }
});

frappe.ui.form.on("Client_Script", {
    refresh(frm) {

        frm.add_custom_button("Remove All Projects", function () {

            frappe.confirm(
                "Are you sure you want to remove all projects?",
                function () {

                    frm.clear_table("projects");

                    frm.refresh_field("projects");

                }
            );

        });

    }
});

frappe.ui.form.on("Client_Script", {

    salary(frm) {
        frm.trigger("calculate_total_salary");
    },

    bonus(frm) {
        frm.trigger("calculate_total_salary");
    },

    calculate_total_salary(frm) {

        frm.set_value(
            "total_salary",
            (frm.doc.salary || 0) + (frm.doc.bonus || 0)
        );

    }

});


frappe.ui.form.on("Client_Script", {

    refresh(frm) {

        frm.add_custom_button("Activate", function () {

            frm.call("activate_employee")
                    

        });

    }

});

frappe.ui.form.on("Client_Script", {

    refresh(frm) {

        frm.add_custom_button("Add Default Project", function () {

            frm.add_child("projects", {
                project_name: "ERP",
                status: "Pending"
            });

            // frm.refresh_field("projects");

            frm.save();

        });

    }

});

frappe.ui.form.on("Client_Script", {

    refresh(frm) {

        frm.add_custom_button("Reload Document", function () {

            if (frm.is_dirty()) {

                frappe.confirm(

                    "You have unsaved changes. Continue?",

                    function () {
                        frm.reload_doc();
                    }

                );

            } else {

                frm.reload_doc();

            }

        });

    }

});

frappe.ui.form.on("Client_Script", {

    refresh(frm) {

        if (frm.is_new()) {

            frm.set_value("status", "Active");

        }

    }

});

