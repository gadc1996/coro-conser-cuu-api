from django.core.management.base import BaseCommand
import os
import subprocess

class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        file_path = os.getenv('GCLOUD_ENV_FILE_PATH', '.env.gcloud')
        service_name = os.getenv('GCLOUD_SERVICE_NAME')

        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.strip():  # ignore empty lines
                key, value = line.strip().split('=')
                command = f"gcloud run services update {service_name} --update-env-vars {key}={value}"
                subprocess.run(command, shell=True)