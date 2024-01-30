from django.core.management.base import BaseCommand
import subprocess
from termcolor import cprint


class Command(BaseCommand):
    help = "Deploy application version"

    def handle(self, *args, **options):
        cprint("Deploying application version", "green")
        try:
            subprocess.run(["eb", "deploy"], check=True, stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            cprint(f"Failed to deploy application version, Error: {e}", "red")
        else:
            cprint("Application version deployed", "green")
