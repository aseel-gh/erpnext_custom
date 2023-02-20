import datetime

import frappe
from frappe.utils import getdate


def get_today():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return today


# def validate_reason_for_leaving(doc, method):
#     if doc.status == 'Left':
#         if not doc.reason_for_leaving:
#             frappe.throw("Reason for leaving must be entered")


def validate_create_task(doc, method):
    if doc.status == 'Left':
        task_doc = frappe.new_doc("Task")
        task_doc.subject = "end of service " + str(doc.employee_name)
        task_doc.insert()
        frappe.msgprint("end of service task created")


@frappe.whitelist()
def get_age(birth_day):
    if birth_day < get_today():
        age = int((getdate(get_today()) - getdate(birth_day)).days / 356)
        return age
    else:
        frappe.throw("The date of birth can not be set as today's date!")
