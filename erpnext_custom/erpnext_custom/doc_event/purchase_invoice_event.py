import frappe


def create_purchase_receipt(doc, method):
    purchase_receipt = frappe.new_doc("Purchase Receipt")
    purchase_receipt.supplier = doc.supplier

    for purchase_invoice_item in doc.items:
        purchase_receipt.append("items", {"item_code": purchase_invoice_item.item_code,
                                         "received_qty": purchase_invoice_item.qty})

    purchase_receipt.insert(ignore_permissions=True)
