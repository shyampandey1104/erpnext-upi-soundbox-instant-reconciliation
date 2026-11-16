# ERPNext IoT UPI Audio Soundbox & POS Reconciliation Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![IoT](https://img.shields.io/badge/UPI-Audio%20Soundbox%20IoT-teal.svg)](https://frappe.io)

Integrates Paytm, PhonePe, and BharatPe audio soundbox IoT hardware webhooks into ERPNext POS counters for zero-touch invoice payment settlement and real-time voice confirmations.

## Features
- **Zero-Touch Checkout Settlement:** Webhook automatically marks POS tickets paid without requiring cashier confirmation clicks.
- **Multilingual Audio Announcements:** Verifies Hindi, English, and regional voice confirmation scripts.
- **Unmatched Payment Safety Net:** Logs unallocated customer UPI credits safely in unearned income suspense ledgers.

## Tests
```bash
python3 -m unittest discover tests
```
