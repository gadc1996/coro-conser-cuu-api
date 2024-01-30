import subprocess
from django.core.management.base import BaseCommand

from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            subprocess.run(
                [
                    "aws",
                    "s3api",
                    "create-bucket",
                    "--bucket",
                    settings.ENV("AWS_BUCKET_NAME"),
                    "--region",
                    settings.ENV("AWS_REGION"),
                    "--create-bucket-configuration",
                    f"LocationConstraint={settings.ENV('AWS_REGION')}",
                ],
                check=True,
                stderr=subprocess.PIPE,
            )
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e.stderr.decode()}")


if __name__ == "__main__":
    Command().handle()
