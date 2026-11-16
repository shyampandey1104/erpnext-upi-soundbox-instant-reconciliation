import unittest
from upi_soundbox.engine import UPISoundboxReconciliationEngine, SoundboxAudioNotification

class TestUPISoundbox(unittest.TestCase):
    def test_instant_pos_soundbox_settlement(self):
        engine = UPISoundboxReconciliationEngine()
        notif = SoundboxAudioNotification(
            soundbox_device_id="SBOX-PAYTM-MUM01",
            store_counter_id="COUNTER-01",
            payer_upi_vpa="customer@okicici",
            amount_received=350.0,
            bank_txn_id="TXN-UPI-99881122",
            language_locale="hi-IN"
        )

        open_bills = [
            {"invoice_no": "POS-INV-88", "outstanding_amount": 120.0},
            {"invoice_no": "POS-INV-89", "outstanding_amount": 350.0}
        ]

        res = engine.reconcile_soundbox_payment(notif, open_bills)
        self.assertTrue(res.is_settled)
        self.assertEqual(res.matched_pos_invoice, "POS-INV-89")
        self.assertIn("350 rupaye prapt hue", res.voice_announcement_text)
        self.assertEqual(res.status, "AUTO_SETTLED_SUCCESS")

if __name__ == "__main__":
    unittest.main()
