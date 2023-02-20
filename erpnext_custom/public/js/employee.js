frappe.ui.form.on("Employee",{
    get_age: function(frm){
    //alert("get_age2");

//Frappe Ajax Call:
    frappe.call({
       method:"erpnext_custom.erpnext_custom.doc_event.employee_event.get_age",
       args:{
           birth_day: frm.doc.date_of_birth
       },
       callback: function(r){
           frm.set_value ( "age", r.message);
           frm.age = r.message;
       }
});
}
})