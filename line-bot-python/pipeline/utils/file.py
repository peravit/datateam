import os
from pathlib import Path
import re
import json


def join_path(*paths):
    seps_regex = r"^[/\\]*|[/\\]*$"

    paths = [re.sub(seps_regex, "", str(p)) for p in paths]

    return os.path.join(os.sep, *paths)


def mkdir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def write_to_file(path, data, mode="w"):
    with open(path, mode) as f:
        f.write(data)


def load_file(path):
    with open(path, "r") as f:
        return f.read()


def write_to_json(path, data, mode="w"):
    with open(path, mode) as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)