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

// frappe.ui.form.on("Job Application", {
//     refresh(frm) {

//         frm.add_custom_button("Get Title", function () {

//             frappe.call({
//                 method: "practice_app.practice_app.doctype.job_application.job_application.get_application_title",
//                 args: {
//                     docname: frm.doc.name
//                 },
//                 callback: function(r) {
//                     frappe.msgprint("Title: " + r.message);
//                 }
//             });

//         });

//     }
// });

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

//custom utilities
frappe.ui.form.on("Job Application", {
refresh(frm) {
        console.log(frappe.get_route());
    }
});

frappe.ui.form.on("Job Application", {
    refresh(frm) {
        frm.add_custom_button("Go to Applicants", () => {
            frappe.set_route("List","Client_Script","List");
            // frappe.set_route([part1,part2,part3],
            // {
            //     fieldname: "value"
            // }
            // );
            //frappe.set_route(part1,part2,part3)
            //part1-form,list,query-report,report,dashboard-view,workspace
            //part2-names of part1
            //part3-may be document name or the types of views(list,kanban,report...)
        });
    }
});

frappe.ui.form.on("Job Application", {
    refresh(frm) {
        let formatted = frappe.format(
            frm.doc.expected_salary,
            { fieldtype: "Currency"}
        );
        console.log(formatted);
        let formatted_date = frappe.format(
    frm.doc.interview_date,
    {
        fieldtype: "Date"
    }
);

console.log(formatted_date);
    }
});
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