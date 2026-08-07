frappe.listview_settings["Job Application"] = {
    add_fields: ["applicant_name","status","email","experience","position_applied","current_salary","expected_salary"],
    // filters: [
    //     ["name", "=", "430"]
    // ],

    onload(listview) {

        listview.filter_area.add([
            ["Job Application", "status", "=", "Selected"]
        ]);

        listview.refresh();

    },
get_indicator(doc) {

    if (doc.current_salary > 50000) { //[Label,Color,Filter]
        return ["High Salary", "green", ""];
    }

    return ["Normal", "blue", ""];
},
    before_render() {
    console.log("Before Render Executed");
    },
button: {

    show(doc) { return doc.status != "Rejected";},

    get_label() {return "open";},

    get_description(doc) {return "View " + doc.applicant_name;},

    action(doc) {frappe.msgprint(doc.applicant_name);}

},
    formatters: {
        applicant_name(value) {
            return "<b>" + value + "</b>";}
    },
        primary_action() {
    // frappe.set_route("List", "User");
            frappe.new_doc("Job Application");
    }
    // get_form_link(doc) {
    // return [
    //     "Form","User",
    //     doc.user
    // ];}
};
