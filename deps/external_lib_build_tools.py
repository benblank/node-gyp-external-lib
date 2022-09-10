# This script exists because gyp appears to lack the ability to run an action in
# a specific directory. This can be worked around for make with the --directory
# flag, but the configure script can only be run from its directory.

import os
import re
import subprocess
import sys


MAIN_TARGET = "../external_lib.a"
TARGET_PATTERN = re.compile(r"(\S+):\s+(.+)")
# TARGET_PATTERN = re.compile(r"(\S+):(?:\s+(.+))?")


def run_make(read_database_only=False):
    # Allowing gyp's make flags (specifically -r, which disables implicit rules)
    # prevents object files from being built.
    env = os.environ.copy()

    if "MAKEFLAGS" in env:
        env.pop("MAKEFLAGS")

    extra_args = ["--print-data-base"] if read_database_only else []

    try:
        completed = subprocess.run(
            [
                "make",
                *extra_args,
                "--file=../external_lib.mk",
                "dummy_for_database_reading" if read_database_only else MAIN_TARGET,
            ],
            check=True,
            env=env,
            text=read_database_only,
            capture_output=read_database_only,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        if read_database_only:
            if error.stdout:
                print(error.stdout)

            if error.stderr:
                print(error.stderr, file=sys.stderr)

        raise

    # Anything on stdout isn't of use to the caller, so simply dump it back out.
    if completed.stderr:
        print(completed.stderr, file=sys.stderr)

    return completed.stdout


def get_make_database():
    raw_database = run_make(read_database_only=True)
    lines = raw_database.split("\n")
    possible_matches = (TARGET_PATTERN.fullmatch(line) for line in lines)

    return {
        match.group(1): match.group(2).split(" ")
        for match in possible_matches
        if match is not None and match.group(1) != "make"
    }


def resolve_target(start, database):
    resolved = set()
    unresolved = {start}

    while unresolved:
        target = next(iter(unresolved))

        if target in database:
            unresolved.update(database[target])
        else:
            resolved.add(target)

        unresolved.remove(target)

    return list(resolved)


def main(dir, toolname):
    try:
        os.chdir(dir)
    except FileNotFoundError:
        print(
            "Could not find source directory.",
            file=sys.stderr,
        )

        sys.exit(1)

    if toolname == "get_sources":
        print(" ".join(resolve_target(MAIN_TARGET, get_make_database())))
    elif toolname == "get_outputs":
        print(" ".join(get_make_database()[MAIN_TARGET]))
    elif toolname == "compile":
        run_make()
    else:
        print(f"Unrecognized tool {repr(toolname)}.", file=sys.stderr)

        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Wrong number of arguments.", file=sys.stderr)

        exit(1)

    main(sys.argv[1], sys.argv[2])
