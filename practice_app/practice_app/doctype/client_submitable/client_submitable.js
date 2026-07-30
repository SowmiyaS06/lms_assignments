// Copyright (c) 2026, Sowmiya and contributors
// For license information, please see license.txt

// frappe.ui.form.on("client_submitable", {
// 	refresh(frm) {

// });
frappe.ui.form.on("client_submitable", {
    before_submit(frm) {
        frappe.msgprint("About to Submit");
    }
});
frappe.ui.form.on("client_submitable", {
    on_submit(frm) {
        frappe.msgprint("Document Submitted");
    }
});
frappe.ui.form.on("client_submitable", {
    before_cancel(frm) {
        frappe.msgprint("Before Cancel");
    }
});
frappe.ui.form.on("client_submitable", {
    after_cancel(frm) {
        frappe.msgprint("Document Cancelled");
    }
});
frappe.ui.form.on("client_submitable", {
    before_discard(frm) {
        frappe.msgprint("Before Discard");
    }
});
frappe.ui.form.on("client_submitable", {
    after_discard(frm) {
        frappe.msgprint("Changes Discarded");
    }
});
