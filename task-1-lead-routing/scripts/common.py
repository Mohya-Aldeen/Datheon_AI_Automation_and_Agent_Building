"""Shared helper: read the Make webhook URL without hard-coding it in the repo."""
import os
import sys
from pathlib import Path


def get_webhook_url() -> str:
    """Return WEBHOOK_URL from the environment, or from a local .env file."""
    url = os.environ.get("WEBHOOK_URL")

    if not url:
        for folder in [Path.cwd(), *Path(__file__).resolve().parents]:
            env_file = folder / ".env"
            if env_file.is_file():
                for line in env_file.read_text(encoding="utf-8").splitlines():
                    line = line.strip()
                    if line.startswith("WEBHOOK_URL="):
                        url = line.split("=", 1)[1].strip().strip('"').strip("'")
                        break
            if url:
                break

    if not url or "YOUR_WEBHOOK_ID" in url or not url.startswith("https://"):
        sys.exit(
            "WEBHOOK_URL is not set.\n"
            "Copy .env.example to .env and paste your Make 'Lead Intake' webhook address,\n"
            'or in PowerShell run:  $env:WEBHOOK_URL = "https://hook.eu1.make.com/..."'
        )
    return url
