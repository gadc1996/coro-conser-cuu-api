import subprocess
from termcolor import cprint


def clean():
    command = ["eb", "terminate", "--all", "--force"]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        cprint(
            "Failed to clean up AWS Elastic Beanstalk application and environment",
            "red",
        )
    else:
        cprint("Cleaned up AWS Elastic Beanstalk application and environment", "green")


if __name__ == "__main__":
    clean()
