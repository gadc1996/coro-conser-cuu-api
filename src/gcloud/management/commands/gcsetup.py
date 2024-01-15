from typing import Any
from django.core.management.base import BaseCommand
import os
import subprocess

class Command(BaseCommand):
    help = 'Perform setup for Google Cloud Run service'
    
    def handle(self, *args: Any, **options: Any) -> None:
        self._login()
        self._set_project()
        self._set_region()

    
    def _login(self) -> None:
        try:
            subprocess.run('gcloud auth login', shell=True, check=True)
            self.stdout.write(self.style.SUCCESS('Successfully authenticated with Google Cloud.'))
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR('Failed to authenticate with Google Cloud.'))
            return
    
    def _set_project(self) -> None:
        project_id = os.getenv('GCLOUD_PROJECT_ID')
        if not project_id:
            self.stdout.write(self.style.ERROR('GCLOUD_PROJECT_ID environment variable is not set.'))
            return
        try:
            command = f'gcloud config set project {project_id}'
            subprocess.run(command, shell=True, check=True)
            self.stdout.write(self.style.SUCCESS(f'Successfully set project to {project_id}.'))
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR(f'Failed to set project to {project_id}.'))
            return
        
    def _set_region(self) -> None:
        region = os.getenv('GCLOUD_REGION')
        if not region:
            self.stdout.write(self.style.ERROR('GCLOUD_REGION environment variable is not set.'))
            return
        try:
            command = f'gcloud config set run/region {region}'
            subprocess.run(command, shell=True, check=True)
            self.stdout.write(self.style.SUCCESS(f'Successfully set region to {region}.'))
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR(f'Failed to set region to {region}.'))
            return