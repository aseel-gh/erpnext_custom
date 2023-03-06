frappe.ui.form.on("Sales Invoice",{
    setup: function(frm){
//    alert("Test");

//Frappe Ajax Call:
    frappe.call({
       method:"erpnext_custom.erpnext_custom.doc_event.sales_invoice_event.check_allow_discount",

       callback: function(r){
           frm.set_value ( "additional_discount_percentage", r.message);
           frm.age = r.message;
       }
});
}
})