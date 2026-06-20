#!/usr/bin/env python3

import json
import sys

for notebook_path in sys.argv[1:]:
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    # Remove notebook-level metadata
    nb["metadata"] = {}

    for cell in nb.get("cells", []):

        # Remove execution information
        if "execution_count" in cell:
            cell["execution_count"] = None

        if "outputs" in cell:
            cell["outputs"] = []

        # Remove cell metadata
        cell["metadata"] = {}

        # Remove cell IDs
        cell.pop("id", None)

    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(
            nb,
            f,
            indent=1,
            ensure_ascii=False
        )
        f.write("\n")