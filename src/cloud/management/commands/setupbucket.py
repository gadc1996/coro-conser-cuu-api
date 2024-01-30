import subprocess
from django.core.management.base import BaseCommand

from src.utils import env


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            subprocess.run(
                [
                    "aws",
                    "s3api",
                    "create-bucket",
                    "--bucket",
                    env("AWS_BUCKET_NAME"),
                    "--region",
                    env("AWS_REGION"),
                    "--create-bucket-configuration",
                    f"LocationConstraint={env('AWS_REGION')}",
                ],
                check=True,
                stderr=subprocess.PIPE,
            )
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e.stderr.decode()}")


if __name__ == "__main__":
    Command().handle()
