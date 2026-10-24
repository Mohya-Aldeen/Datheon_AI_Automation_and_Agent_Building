"""Send awkward leads to the Make 'Lead Intake' webhook.

Each lead tests a different weakness: missing data, vague wording, and
special characters. Check Airtable and Slack afterwards.

Usage:  python scripts/test_edge_cases.py
"""
import time

import requests

from common import get_webhook_url

# Pause between sends. Keep it long if you use "Run once" in Make;
# it can be shorter when the scenario is Active.
DELAY_SECONDS = 15

LEADS = [
    {   # no size, no budget, vague message
        "name": "Omar K",
        "email": "omar@example.com",
        "company": "Unknown Co",
        "company_size": "",
        "budget": "",
        "message": "hi",
        "source": "webhook",
    },
    {   # big company, messy budget wording
        "name": "Lena Fischer",
        "email": "lena@bigcorp.de",
        "company": "BigCorp GmbH",
        "company_size": "around 5000 people",
        "budget": "maybe 100k, not sure yet",
        "message": "We need AI agents to triage 50,000 support tickets per month.",
        "source": "webhook",
    },
    {   # quotation marks and symbols in the text
        "name": 'Ali "The Boss" Hassan',
        "email": "ali@test.com",
        "company": "Café & Co.",
        "company_size": "12",
        "budget": "$3,000",
        "message": 'We\'d like a "smart" assistant -- any ideas?',
        "source": "webhook",
    },
]


def main() -> None:
    url = get_webhook_url()
    for lead in LEADS:
        print(time.strftime("%H:%M:%S"), "sending", lead["company"])
        response = requests.post(url, json=lead, timeout=30)
        print("  status:", response.status_code)
        time.sleep(DELAY_SECONDS)


if __name__ == "__main__":
    main()
