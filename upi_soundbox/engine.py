"""IoT UPI Audio Soundbox Webhook Listener & POS Invoice Auto-Settlement Engine."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class SoundboxAudioNotification:
    soundbox_device_id: str
    store_counter_id: str
    payer_upi_vpa: str
    amount_received: float
    bank_txn_id: str
    currency: str = "INR"
    language_locale: str = "hi-IN"  # Hindi audio announcement


@dataclass
class SoundboxSettlementResult:
    matched_pos_invoice: Optional[str]
    amount_settled: float
    voice_announcement_text: str
    is_settled: bool
    status: str  # AUTO_SETTLED_SUCCESS, UNMATCHED_OPEN_CREDIT, UNDERPAYMENT_ERROR


class UPISoundboxReconciliationEngine:
    """Listens for hardware audio soundbox payment webhooks and auto-closes pending POS counter invoices."""

    def reconcile_soundbox_payment(
        self,
        notification: SoundboxAudioNotification,
        pending_pos_invoices: List[Dict[str, Any]]
    ) -> SoundboxSettlementResult:
        # pending_pos_invoices: [{"invoice_no": "POS-01", "outstanding_amount": 150.0}]
        matched_inv = None

        for inv in pending_pos_invoices:
            if abs(inv["outstanding_amount"] - notification.amount_received) < 0.01:
                matched_inv = inv["invoice_no"]
                break

        if matched_inv:
            voice_txt = f"{notification.amount_received:.0f} rupaye prapt hue" if notification.language_locale.startswith("hi") else f"Received {notification.amount_received:.0f} rupees"
            return SoundboxSettlementResult(
                matched_pos_invoice=matched_inv,
                amount_settled=notification.amount_received,
                voice_announcement_text=voice_txt,
                is_settled=True,
                status="AUTO_SETTLED_SUCCESS"
            )
        else:
            voice_txt = f"{notification.amount_received:.0f} rupaye prapt hue"
            return SoundboxSettlementResult(
                matched_pos_invoice=None,
                amount_settled=notification.amount_received,
                voice_announcement_text=voice_txt,
                is_settled=False,
                status="UNMATCHED_OPEN_CREDIT"
            )
