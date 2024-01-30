import subprocess
import environ
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        env = environ.Env(
            AWS_BUCKET_NAME=(str, ""),
            AWS_REGION=(str, ""),
        )
        if not env("AWS_BUCKET_NAME"):
            raise ValueError("AWS_BUCKET_NAME is not set")
        if not env("AWS_REGION"):
            raise ValueError("AWS_REGION is not set")
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
