#!/usr/bin/env -S pipx run
from cowsay import char_funcs


if __name__ == "__main__":
    char_funcs["cow"]("Hello PyBelfast!")
# /// pyproject
# run.requirements = ["cowsay"]
# ///
