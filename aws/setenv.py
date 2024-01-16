from os import environ
from pathlib import Path
import subprocess

AWS_ENV_FILE = environ.get('AWS_ENV_FILE', '.env.aws')

def main():
    file_path = Path(__file__).resolve().parent.parent / AWS_ENV_FILE

    try:
        with open(file_path) as file:
            lines = file.readlines()

        env_vars = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
        command = ['eb', 'setenv']
        command.extend(env_vars)
        subprocess.run(command, check=True)
        

        
    except FileNotFoundError:
        print(f"File {AWS_ENV_FILE} was not found, please create it, file name can be set using env variable AWS_ENV_FILE.")
        
if __name__ == '__main__':
    main()