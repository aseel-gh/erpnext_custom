frappe.ui.form.on("Sales Invoice",{
    validate: function(frm){
//    alert("Test");

//Frappe Ajax Call:
    frappe.call({
       method:"erpnext_custom.erpnext_custom.doc_event.sales_invoice_event.check_allow_discount",
       args:{},

       callback: function(r){
//        if (r.exc){}
       if ( r.message){
           frm.set_value ( "additional_discount_percentage",0);
           frm.set_df_property('additional_discount_account','disabled', 1);
           }
       }
});
}
})