// frappe.pages['page_api_test'].on_page_load = function(wrapper) {
//     let page = frappe.ui.make_app_page({
//         parent: wrapper,
//         title: "Page API",
//         single_column: true
//     // });

//     // page.set_title("Job Dashboard");
//     // page.set_title_sub("August 2026");

//     page.set_indicator("Running", "green");

//     page.set_primary_action("Create Job", function () {
//         frappe.msgprint("Primary Action Clicked");
//     });

//     page.set_secondary_action("Refresh", function () {
//         frappe.msgprint("Refresh Clicked");
//     });


//     page.add_menu_item("Send Email", function () {
//         frappe.msgprint("Email Menu Clicked");
//     });
//     page.add_menu_item("Standard Item", function () {
//         frappe.msgprint("Standard Menu Clicked");
//     });


//     page.add_action_item("Delete", function () {
//         frappe.msgprint("Delete Clicked");
//     });
//     page.add_action_item("Export", function () {
//         frappe.msgprint("Export Clicked");
//     });






	

//     page.add_inner_button("Update Status", function () {
//         frappe.msgprint("Status Updated");
//     });
//     page.add_inner_button("New Applicant", function () {
//         frappe.msgprint("New Applicant");
//     }, "Create");
//     page.add_inner_button("Reject Applicant", function () {
//         frappe.msgprint("Rejected");
//     }, "Actions");

//     page.change_inner_button_type(
//         "Update Status",null,"primary");

//     page.change_inner_button_type("Reject Applicant","Actions","danger");

//     let status = page.add_field({
//         label: "Status",
//         fieldname: "status",
//         fieldtype: "Select",
//         options: [
//             "Open",
//             "Under Review",
//             "Selected",
//             "Rejected"
//         ],
//         change() {
//             console.log("Status :", status.get_value());
//         }
//     });

//     let experience = page.add_field({
//         label: "Experience",
//         fieldname: "experience",
//         fieldtype: "Int",
//         change() {
//             console.log("Experience :", experience.get_value());
//         }
//     });

// }; 
frappe.pages["page-api-test"].on_page_load = function (wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Realtime Chart",
        single_column: true
    });

    $(page.body).html(`<div id="chart"></div>`);

    const data = {
        datasets: [
            {
                name: "Random Number",
                values: []
            }
        ]
    };

    let chart = new frappe.ui.RealtimeChart(
        "#chart",
        "demo",
        8,
        {
            title: "Realtime Demo",
            data: data,
            type: "line",
            height: 250
        }
    );

    let i = 1;

    setInterval(() => {

        chart.update_chart(
            i,
            [Math.floor(Math.random() * 100)]
        );

        i++;

    }, 1000);

};