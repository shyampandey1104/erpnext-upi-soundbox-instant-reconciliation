# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "upi_soundbox"
app_title = "Erpnext Upi Soundbox Instant Reconciliation"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Upi Soundbox Instant Reconciliation for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/upi_soundbox/css/upi_soundbox.bundle.css"
app_include_js = "/assets/upi_soundbox/js/upi_soundbox.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "upi_soundbox.engine.on_document_submit",
        "on_cancel": "upi_soundbox.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "upi_soundbox.engine.daily_scheduled_sync"
    ]
}
