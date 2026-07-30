// Copyright (c) 2026, Sowmiya and contributors
// For license information, please see license.txt
// frappe.ui.form.on("Client", {
//     refresh(frm) {
//         frappe.msgprint("Welcome to Student Form!");
//     }
// });
// frappe.ui.form.on("Client", {
// 	validate(frm) {
//         if(frm.doc.age<0){
//             frappe.throw("Age cannot be negative");
//         }
// 	},
// });
frappe.ui.form.on("Client", {
    last_name(frm) {
        frm.set_value(
            "full_name",
            frm.doc.first_name + " " + frm.doc.last_name
        );
    }
});
frappe.ui.form.on("Client", {
    before_save(frm) {
        // frm.set_value(
        //     "full_name",
        //     frm.doc.first_name + " " + frm.doc.last_name
        // );
        frappe.msgprint("Before Save!");
    }
});
frappe.ui.form.on("Client", {
    after_save(frm) {
        frappe.msgprint("Record Saved Successfully!");
    }
});
frappe.ui.form.on("Client", {
    setup(frm) {
        frappe.msgprint("Setup Event");
    }
});
frappe.ui.form.on("Client", {
    before_load(frm) {
        frappe.msgprint("Before Load");
    }
});
frappe.ui.form.on("Client", {
    onload(frm) {
        frappe.msgprint("Form Loaded");
    }
});
frappe.ui.form.on("Client", {
    refresh(frm) {
        frappe.msgprint("Refresh Event");
    }
});
frappe.ui.form.on("Client", {
    onload_post_render(frm) {
        frappe.msgprint("Form Rendered");
    }
});
frappe.ui.form.on("Client", {
    items_on_form_rendered(frm) {
        console.log("Child Row Opened");
    }
});