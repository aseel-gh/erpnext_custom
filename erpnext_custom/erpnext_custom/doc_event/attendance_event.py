import frappe
from frappe.utils import time_diff_in_hours


def get_attendance(doc, method):
    if not doc.check_in or not doc.check_out:
        doc.status = 'Absent'

    if doc.check_in and doc.check_out:
        doc.hours = time_diff_in_hours(doc.check_out, doc.check_in)
        doc.status = 'Present'
