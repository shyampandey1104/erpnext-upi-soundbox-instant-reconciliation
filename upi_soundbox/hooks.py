# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "upi_soundbox"
app_title = "Erpnext Upi Soundbox Instant Reconciliation"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Upi Soundbox Instant Reconciliation - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/upi_soundbox/css/upi_soundbox.bundle.css"
app_include_js = "/assets/upi_soundbox/js/upi_soundbox.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Erpnext Upi Soundbox Instant Reconciliation Entry": {
        "validate": "upi_soundbox.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "upi_soundbox.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "upi_soundbox.tasks.hourly_sync"
    ],
    "daily": [
        "upi_soundbox.tasks.daily_reconciliation"
    ],
    "weekly": [
        "upi_soundbox.tasks.weekly_digest"
    ]
}
