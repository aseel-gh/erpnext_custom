import frappe


@frappe.whitelist()
def add_custom_remarks(doc, method):
    # frappe.msgprint("test")
    items = ""
    for item in doc.get("items"):
        items = str(items) + ", " + str(item.item_code)
    doc.remarks = str(items)


@frappe.whitelist()
def add_custom_note(doc, method):
    items_note = ""
    for item in doc.items:
        items_note = str(items_note) + str(item.notes) + "\n"
    doc.remarks = str(items_note)


def validate_pos(doc, method):
    if doc.is_pos == 1:
        if len(doc.payments) == 0:
            frappe.throw("This sales invoice is pos, you must add at least one payment.")
        else:
            for payment in doc.payments:
                if payment.amount <= 0:
                    frappe.throw("payment amount can't be zero.")


@frappe.whitelist()
def check_allow_discount(doc, method):
    allow_discount = frappe.db.get_value('Customer', doc.customer, 'allow_discount')
    if allow_discount == 0:
        return 1
        # return "test succeed"
        # return doc.additional_discount_percentage == 0
        # return doc.apply_discount_on == ""

        # doc.discount_amount == 0
