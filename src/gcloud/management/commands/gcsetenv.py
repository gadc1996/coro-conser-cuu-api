from django.core.management.base import BaseCommand
import os
import subprocess
from typing import List

GCLOUD_SERVICE_NAME = os.getenv('GCLOUD_SERVICE_NAME')
GCLOUD_ENV_FILE_PATH = os.getenv('GCLOUD_ENV_FILE_PATH', '.env.gcloud')

class Command(BaseCommand):
    help = 'Set environment variables for Google Cloud Run service'

    def handle(self, *args, **options) -> None:
        self._clear_env_vars()

        try:
            with open(GCLOUD_ENV_FILE_PATH, 'r') as file:
                file_content = file.read()
                self._set_env_vars(file_content.split('\n'))
                
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File {GCLOUD_ENV_FILE_PATH} not found, Please create a file named {GCLOUD_ENV_FILE_PATH} and add environment variables in the format KEY=VALUE or set the environment variable GCLOUD_ENV_FILE_PATH to the path of the file.'))
            return
        
    def _clear_env_vars(self) -> None:
        self.stdout.write(self.style.SUCCESS('Clearing all environment variables'))
        try:
            command = f"gcloud run services update {GCLOUD_SERVICE_NAME} --clear-env-vars"
            subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.stdout.write(self.style.SUCCESS('Successfully cleared all environment variables'))
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR('Failed to clear all environment variables'))
            return
        
    def _set_env_vars(self, lines: List[str]) -> None:
        self.stdout.write(self.style.SUCCESS('Setting environment variables'))
        env_vars = ",".join(line.strip() for line in lines if line.strip())
        try:
            command = f"gcloud run services update {GCLOUD_SERVICE_NAME} --update-env-vars {env_vars}"
            subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.stdout.write(self.style.SUCCESS(f'Successfully set {env_vars}'))
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR(f'Failed to set {env_vars}'))
            return