"""Write the GPS's one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The entry is a single line of plain text (at most 200
characters): the GPS, smug and defensive, blaming the map for sending
the driver down the wrong road.
"""

import os

LINE = "The map swore that cul-de-sac was a shortcut to the wedding, so I took it \u2014 I just follow the dots, and the lake was never in my contract."


def main():
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if len(line) > 200:
        raise SystemExit("entry line exceeds 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
        os.chmod(path, 0o644)
    except OSError as exc:
        raise SystemExit("failed to write entry.txt: %s" % exc)


if __name__ == "__main__":
    main()
