# yourapp/management/commands/backup_email.py
import datetime, zipfile
from pathlib import Path
from django.core.mail import EmailMessage
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Dump DB, zip it, and email it"

    def handle(self, *args, **opts):
        stamp = datetime.date.today().isoformat()
        json_path = Path(f"backup_{stamp}.json")
        zip_path = json_path.with_suffix(".zip")

        with open(json_path, "w", encoding="utf-8") as f:
            call_command("dumpdata", "--natural-foreign", "--natural-primary",
                         "--exclude=contenttypes", "--exclude=auth.permission",
                         indent=2, stdout=f)

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
            z.write(json_path)

        msg = EmailMessage(f"Backup {stamp}", "Backup attached.",
                           to=["uchechi130@gmail.com"])
        msg.attach_file(zip_path)
        msg.send()

        json_path.unlink()
        zip_path.unlink()