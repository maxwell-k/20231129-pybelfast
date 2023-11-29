# SPDX-License-Identifier: MPL-2.0
# SPDX-FileCopyrightText: 2023 Keith Maxwell
from pathlib import Path
from shutil import rmtree

import nox

MARP_CLI = (
    "npm",
    "exec",
    "--prefer-offline",
    "--yes",
    "--",
    "@marp-team/marp-cli@latest",
    "--html",
    "--allow-local-files",
)
PYTHON_VERSION = "3.12"
SITE = Path("_site")
VIRTUAL_ENVIRONMENT = ".venv"

PYTHON = Path(VIRTUAL_ENVIRONMENT).absolute() / "bin" / "python"


nox.options.sessions = (
    "reuse",
    "html",
    "pdf",
)
nox.options.stop_on_first_error = True


@nox.session()
def reuse(session) -> None:
    """Check this repository for compliance"""
    session.install("reuse")
    session.run("reuse", "lint")


@nox.session(python=False)
def html(session) -> None:
    """Render as index.html"""
    session.run(
        *MARP_CLI,
        f"--output={SITE}/index.html",
        "index.md",
    )


@nox.session(python=False)
def pdf(session) -> None:
    """Render as index.pdf"""
    session.run(
        *MARP_CLI,
        "--pdf",
        "--theme=a4.css",
        f"--output={SITE}/index.pdf",
        "index.md",
    )


@nox.session(python=False)
def serve(session) -> None:
    """Serve at http://localhost:8080/"""
    session.run(
        "npm",
        "exec",
        "--prefer-offline" "--yes",
        "--",
        "@marp-team/marp-cli@latest",
        "--html",
        "--watch",
        "--server",
        ".",
    )


@nox.session(python=False)
def dev(session) -> None:
    """Set up a virtual environment for noxfile.py"""
    rmtree(VIRTUAL_ENVIRONMENT, ignore_errors=True)
    session.run(
        f"python{PYTHON_VERSION}",
        "-m",
        "venv",
        "--upgrade-deps",
        VIRTUAL_ENVIRONMENT,
    )
    session.run(
        PYTHON,
        "-m",
        "pip",
        "install",
        "--use-pep517",
        "black",
        "flake8",
        "nox",
        "reorder-python-imports",
        "reuse",
    )
