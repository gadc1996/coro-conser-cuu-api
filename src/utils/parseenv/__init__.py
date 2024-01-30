from typing import List


class EnvFile:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def _load(self) -> List[str]:
        try:
            with open(self.file_path) as file:
                lines = file.readlines()

            env_vars = [
                line.strip()
                for line in lines
                if line.strip() and not line.startswith("#")
            ]
            return env_vars
        except FileNotFoundError:
            raise (
                f"File {self.file_path} was not found, please create it, file name can be set using env variable AWS_ENV_FILE."
            )

    def as_list(self) -> List[str]:
        return self._load()

    def as_string(self, separator=",") -> str:
        env_vars = self._load()
        return separator.join(env_vars)
