frappe.ui.form.on('Purchase Order', {
	setup: function(frm) {

	frm.set_query("supplier", function() {
			return{
				"filters": {
					"supplier_type": "Company"
				}
			}
		});
	}
})