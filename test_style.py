import os
import subprocess
import re


def test_flake8():
    proc = subprocess.Popen("flake8", stdout=subprocess.PIPE)

    proc.wait()

    out = proc.stdout.read().decode()

    lines = [l.strip() for l in out.split("\n")if l]

    print(out)

    assert not bool(lines)


def test_pylint():
    proc = subprocess.Popen(("pylint --disable=missing-docstring,"
                             "too-many-branches,no-name-in-module,"
                             "attribute-defined-outside-init,"
                             "too-many-instance-attributes"
                             "too-few-public-methods,"
                             "too-many-locals,too-many-arguments,"
                             "too-many-statements,no-member,unused-argument,"
                             " .").split(),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    proc.wait()

    out = proc.stdout.read().decode()

    print(out)

    last_line = [l for l in out.split("\n")if l][-1]

    m = re.match(r"Your code has been rated at 10\.00\/10", last_line.strip())

    assert m is not None
