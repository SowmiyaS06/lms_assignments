// Copyright (c) 2026, Sowmiya and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Job Application", {
// 	refresh(frm) {

// 	},
// });
// frappe.ui.form.on("Job Application", {
//     refresh(frm) {
//         frm.add_custom_button("Create Application", function() {
//             frappe.call({
//                 method: "practice_app.practice_app.doctype.job_application.job_application.create_application"
//             });
//         });
//     }
// });

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {
//         frm.add_custom_button("Update Employee", function () {
//             frappe.call({
//                 method: "practice_app.practice_app.doctype.job_application.job_application.update_employee",
//                 callback: function(r) {
//                     frappe.msgprint("Updated Successfully");
//                     frm.reload_doc();
//                 }
//             });
//         });
//     }
// });

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {
//         frm.add_custom_button("Delete Application", function () {

//             frappe.call({
//                 method: "practice_app.practice_app.doctype.job_application.job_application.delete_application",
//                 args: {
//                     docname: frm.doc.name
//                 },
//                 callback: function(r) {
//                     frappe.msgprint(r.message);
//                 }
//             });

//         });
//     }
// });

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {
//         frm.add_custom_button("Reload Demo", function () {

//             frappe.call({
//                 method: "practice_app.practice_app.doctype.job_application.job_application.reload_example",
//                 args: {
//                     docname: frm.doc.name
//                 },
//                 callback: function(r) {
//                     frappe.msgprint("Current Status: " + r.message);

//                     frm.reload_doc();
//                 }
//             });

//         });
//     }
// });

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {

//         frm.add_custom_button("Check Write Permission", function () {

//             frappe.call({
//                 method: "practice_app.practice_app.doctype.job_application.job_application.check_write_permission",
//                 args: {
//                     docname: frm.doc.name
//                 },
//                 callback: function(r) {
//                     frappe.msgprint(r.message);
//                 }
//             });

//         });

//     }
// });

frappe.ui.form.on("Job Application", {
    refresh(frm) {

        frm.add_custom_button("Get Title", function () {

            frappe.call({
                method: "practice_app.practice_app.doctype.job_application.job_application.get_application_title",
                args: {
                    docname: frm.doc.name
                },
                callback: function(r) {
                    frappe.msgprint("Title: " + r.message);
                }
            });

        });

    }
});

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {
//         frm.add_custom_button("Notify Update", function () {
//             frappe.call({
//                 method: "practice_app.practice_app.doctype.job_application.job_application.update_status",
//                 args: {
//                     docname: frm.doc.name
//                 },
//                 callback: function(r) {
//                     frappe.msgprint(r.message);
//                     frm.reload_doc();
//                 }
//             });
//         });
//     }
// });

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {

//         frm.add_custom_button("Add Skill", function () {

//             frappe.call({
//                 method: "practice_app.practice_app.doctype.job_application.job_application.add_skill",
//                 args: {
//                     docname: frm.doc.name
//                 },
//                 callback: function(r) {

//                     frappe.msgprint(r.message);

//                     frm.reload_doc();

//                 }
//             });

//         });

//     }
// });

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {

//         frm.add_custom_button("Get URL", function () {

//             frappe.call({
//                 method: "practice_app.practice_app.doctype.job_application.job_application.get_application_url",
//                 args: {
//                     docname: frm.doc.name
//                 },
//                 callback: function(r) {
//                     frappe.msgprint(r.message);
//                 }
//             });

//         });

//     }
// });

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {
//         frm.add_custom_button("Add Comment", function () {
//             frappe.call({
//                 method: "practice_app.practice_app.doctype.job_application.job_application.add_comment",
//                 args: {
//                     docname: frm.doc.name
//                 },
//                 callback: function(r) {
//                     frappe.msgprint(r.message);
//                     frm.reload_doc();
//                 }
//             });
//         });
//     }
// });

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {

//         frm.add_custom_button("Select Candidate", function () {

//             frappe.call({
//                 method: "practice_app.practice_app.doctype.job_application.job_application.select_candidate",
//                 args: {
//                     docname: frm.doc.name
//                 },
//                 callback: function(r) {
//                     frappe.msgprint(r.message);
//                     frm.reload_doc();
//                 }
//             });

//         });

//     }
// });

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {

//         frappe.ui.form.make_control({
//             parent: frm.fields_dict.dynamic_controls.$wrapper,
//             df: {
//                 label: "LinkedIn Profile",
//                 fieldname: "linkedin_profile",
//                 fieldtype: "Data"
//             },
//             render_input: true
//         });

//     }
// });

// custom utilities
// frappe.ui.form.on("Job Application", {
// refresh(frm) {
//         console.log(frappe.get_route());
//     }
// });

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {
//         frm.add_custom_button("Go to Applicants", () => {
//             frappe.set_route("List","Client_Script","List");
//             // frappe.set_route([part1,part2,part3],
//             // {
//             //     fieldname: "value"
//             // }
//             // );
//             //frappe.set_route(part1,part2,part3)
//             //part1-form,list,query-report,report,dashboard-view,workspace
//             //part2-names of part1
//             //part3-may be document name or the types of views(list,kanban,report...)
//         });
//     }
// });

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {
//         let formatted = frappe.format(
//             frm.doc.expected_salary,
//             { fieldtype: "Currency"}
//         );
//         console.log(formatted);
//         let formatted_date = frappe.format(
//     frm.doc.interview_date,
//     {
//         fieldtype: "Date"
//     }
// );

// console.log(formatted_date);
//     }
// });
// Fieldtype	Raw Value	Formatted Output
// Date	"2026-08-05"	05-08-2026 (or your configured date format)
// Datetime	"2026-08-05 14:30:00"	05-08-2026 02:30 PM
// Time	"14:30:00"	02:30 PM
// Currency	50000	₹50,000.00
// Float	25.6789	25.68 (depends on precision)
// Int	12345	12,345
// Percent	85	85%
// Check	1	Yes
// Check	0	No
// Duration	3600	1 Hour (depends on duration settings)
// Link	"EMP-0001"	EMP-0001 (rendered as a clickable link in supported UI)
// Data	"Sowmiya"	Sowmiya
// Email	"abc@gmail.com"	abc@gmail.com
// Phone	"9876543210"	9876543210
// URL	"https://frappe.io"	Clickable URL (in supported UI)
// Rating	4	★★★★☆ (depends on where it's rendered)

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {

//         frappe.require(
//             "/assets/practice_app/js/salary_calculator.js",
//             () => {

//                 calculate_salary();

//             }
//         );

//     }
// });

// frappe.provide("frappe.student.utils");
// frappe.student.utils.sayHello = function () {
//     console.log("Hello");
// };

// dialog api
// frappe.ui.form.on("Job Application", {
//     refresh(frm) {
//         frm.add_custom_button("Apply Job", function () {
//         let d = new frappe.ui.Dialog({
//         title: "Job Application",
//         fields: [
//                     {
//                         label: "Applicant Name",
//                         fieldname: "applicant_name",
//                         fieldtype: "Data",
//                         reqd: 1
//                     },
//                     {
//                         label: "Email",
//                         fieldname: "email",
//                         fieldtype: "Data",
//                         reqd: 1
//                     },
//                     {
//                         label: "Phone",
//                         fieldname: "phone",
//                         fieldtype: "Phone"
//                     },
//                     {
//                         label: "Position",
//                         fieldname: "position_applied",
//                         fieldtype: "Select",
//                         options: [
//                             "Software Engineer",
//                             "Frontend Developer",
//                             "Backend Developer",
//                             "Full Stack Developer",
//                             "Python Developer",
//                             "Frappe Developer",
//                             "Java Developer",
//                             "QA Engineer",
//                             "DevOps Engineer",
//                             "UI/UX Designer",
//                             "Data Analyst",
//                             "AI/ML Engineer",
//                             "Intern"
//                         ].join("\n"),
//                         reqd: 1
//                     },
//                     {
//                         label: "Experience",
//                         fieldname: "experience",
//                         fieldtype: "Float"
//                     },
//                     {
//                         label: "Expected Salary",
//                         fieldname: "expected_salary",
//                         fieldtype: "Currency"
//                     },
//                     {
//     label: "Application Date",
//     fieldname: "application_date",
//     fieldtype: "Date",
//     default: frappe.datetime.get_today()
// }
//                 ],
//                 size: "small",
//                 primary_action_label: "Submit",
//                 primary_action(values) {
//                     if (values.expected_salary < 10000) {
//     frappe.msgprint({
//         title: "Invalid Salary",
//         indicator: "red",
//         message: "Expected salary should be at least ₹10,000"
//     });
//     return;
// }
//         console.log(values);
//             frappe.msgprint({
//                 title: "Application Submitted",
//                 indicator: "green",
//                 message: `
//                     <b>Applicant :</b> ${frm.doc.applicant_name}<br>
//                     <b>Position :</b> ${frm.doc.position_applied}<br>
//                     <b>Status :</b> ${frm.doc.status}
//                 `});
//                     d.hide();}
//             });
//             d.show();

//         });

//     }

// });

frappe.ui.form.on("Job Application", {

    refresh(frm) {

        frm.add_custom_button("Applicant Prompt", function () {

            frappe.prompt(
                "Applicant Name",

                ({ value }) => {

                    console.log(value);

                    frappe.msgprint(
                        "Applicant : " + value
                    );

                }
            );

        });

    }

});
frappe.ui.form.on("Job Application", {

    refresh(frm) {

        frm.add_custom_button("Reject Applicant", function () {

            frappe.confirm(

                `Are you sure you want to reject
                <b>${frm.doc.applicant_name}</b>?`,

                function () {

                    frappe.msgprint({
                        title: "Applicant Rejected",
                        indicator: "red",
                        message:
                        `${frm.doc.applicant_name} has been rejected.`
                    });

                },

                function () {

                    frappe.msgprint({
                        title: "Cancelled",
                        indicator: "blue",
                        message:
                        "No changes were made."
                    });

                }

            );

        });

    }

});

frappe.ui.form.on("Job Application", {
    refresh(frm) {
        frm.add_custom_button("Process", () => {

       let current = 0;

let interval = setInterval(() => {

    current++;

    frappe.show_progress(

        "Uploading Resumes",

        current,

        10,

        `Uploading Resume ${current}`

    );

    if (current === 10) {

        clearInterval(interval);

        frappe.show_alert({
            message: "Upload Completed",
            indicator: "green"
        }, 5);
    }
}, 100);
        });
    }
});

frappe.ui.form.on("Job Application", {

    refresh(frm) {

        frm.add_custom_button("New Applicant", () => {

            frappe.new_doc("Job Application");

        });

    }

});

// frappe.call({
//     method: "practice_app.api.get_student",
//     args: {
//         name: "435"
//     }
// }).then(r => {
//     console.log(r.message);
// });

// frappe.ui.form.on("Job Application",{
//     refresh(frm){
//         frm.add_custom_button("Change Status",()=>{
//             frm.set_value("status","Selected");
//             frappe.msgprint("Status changed to Selected");
//         })
//         frm.refresh_field("status");
//     }
// })

frappe.ui.form.on("Job Application",{
    refresh(frm){
        if(frm.doc.status=="Draft"){
            frm.add_custom_button("Apply",()=>{
                frm.set_value("status","Applied");
                frappe.msgprint("Employee status changed to applied");
            })
        }
        frm.refresh_field("status");
    }
})