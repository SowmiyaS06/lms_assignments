frappe.pages['scanner-demo'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'None',
		single_column: true
	});
	// page.add_inner_button("Open Scanner", () => {

    //     new frappe.ui.Scanner({
    //         dialog: true,
    //         multiple: false,

    //         on_scan(data) {

    //             frappe.msgprint(
    //                 "Scanned Value: " + data.decodedText
    //             );

    //             console.log(data);
    //         }

    //     });

    // });
	let scanner;

    page.add_inner_button("Start Scanner", () => {

        scanner = new frappe.ui.Scanner({
            dialog: true,
            multiple: true,

            on_scan(data) {
                console.log("Scanned:", data.decodedText);

                frappe.show_alert({
                    message: "Scanned: " + data.decodedText,
                    indicator: "green"
                });
            }
        });

    });

    page.add_inner_button("Stop Scanner", () => {
        if (scanner) {
            scanner.stop_scan();
            frappe.msgprint("Scanner Stopped");
        }
    });
}