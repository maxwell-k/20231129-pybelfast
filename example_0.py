from argparse import ArgumentParser
from pathlib import Path

from yaml import safe_load

REPO = "https://github.com/RobertCraigie/pyright-python"


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file", type=Path)
    with parser.parse_args().file.open() as file:
        configuration = safe_load(file)
    rev = next(i["rev"] for i in configuration["repos"] if i["repo"] == REPO)
    print(rev.removeprefix("v"))
