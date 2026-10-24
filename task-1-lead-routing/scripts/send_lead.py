"""Send one sample lead to the Make 'Lead Intake' webhook.

Usage:  python scripts/send_lead.py

If you get 410, the Make scenario is not listening: click "Run once" in Make
first (and send right away), or switch the scenario to Active.
"""
import requests

from common import get_webhook_url

lead = {
    "name": "Sara Ahmed",
    "email": "sara@acmelogistics.com",
    "company": "Acme Logistics",
    "company_size": "250 employees",
    "budget": "$20,000 per year",
    "message": "We process about 2,000 invoices a month by hand and want to automate it.",
    "source": "webhook",
}

response = requests.post(get_webhook_url(), json=lead, timeout=30)
print(response.status_code, response.text)
