frappe.pages["realtime-page-demo"].on_page_load = function(wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Scanner Demo",
        single_column: true
    });

    page.add_inner_button("Open Scanner", () => {

        new frappe.ui.Scanner({
            dialog: true,
            multiple: false,

            on_scan(data) {

                frappe.msgprint(
                    "Scanned Value: " + data.decodedText
                );

                console.log(data);
            }

        });

    });

};