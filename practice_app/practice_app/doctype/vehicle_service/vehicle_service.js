// Copyright (c) 2026, Sowmiya and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Vehicle Service", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Vehicle Service",{
    refresh(frm){
        if(frm.doc.vehicle_type=="Car"){
            frm.add_custom_button("Change Status",()=>{
                frm.set_value("service_status","Pending")
                 frm.disable_save();
                frappe.msgprint("Status updated")
            },"Actions")
        }
    }
})

frappe.ui.form.on("Vehicle Service", {
    refresh(frm) {
        // if (frm.doc.vehicle_type=="Car") {
        //     frm.enable_save();
        // } else {
        //     frm.disable_save();
        // }
        frm.set_intro("Welcome to the form")
}
});

frappe.ui.form.on("Vehicle Service",{
    refresh(frm){
        // frm.add_custom_button("Email",()=>{
        //     frm.email_doc(`hello ${frm.doc.customer_name}`)
        // },"Actions")
        frm.add_custom_button("Call",()=>{
            frm.call("test_method")
            .then(r=>{
                frappe.msgprint(r.message);
            })
        })
    }
})

frappe.ui.form.on("Vehicle Service",{
    refresh(frm){
        frm.change_custom_button_type("Change Status","Actions","primary")
    }
})

frappe.ui.form.on("Vehicle Service",{
    refresh(frm){
        // frm.remove_custom_button("Change Status","Actions")
        // frm.set_df_property("service_status","reqd",1)
        // frm.toggle_enable("service_status")
        // frm.toggle_reqd("service_type",frm.doc.mechanic=='Peter')
        frm.toggle_display("amount",frm.doc.vehicle_type=='Car')

    }
})

frappe.ui.form.on("Vehicle Service",{
    setup(frm){
        frm.set_query("vehicle",()=>{
            return{
                filters:{status:"Inactive"}
    }})
    }
})

frappe.ui.form.on("Vehicle Service",{
    refresh(frm){
        frm.add_custom_button("Trigger",()=>{
            frm.trigger("msg")
        })
    },
    msg(frm){
        frappe.msgprint("Hello from trigger!")
    }
})