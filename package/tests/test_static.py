from pathlib import Path
import shlex
import subprocess

base_dir = Path(__file__).parent.parent


# TODO: set cwd?
def call(cmd: list[str]):
    result = subprocess.run(cmd, cwd=base_dir, check=False)
    print("command run:", shlex.join(cmd) + " 2>&1")
    assert result.returncode == 0, f"{cmd[0]} returned an error"


def pyright(path: Path):
    call(["pyright", str(path), "-p", str(path)])


def static_type_analysis(path: Path):
    pyright(path)


def doc_linter(path: Path):
    ruff(path)


def ruff(path: Path):
    call(["ruff", "check", str(path)])


def pylama(path: Path):
    call(["pylama", str(path)])


def linters(path: Path):
    ruff(path)
    pylama(path)


def test_static():
    static_type_analysis(base_dir)


def test_ruff():
    ruff(base_dir)


def test_lama():
    pylama(base_dir)
