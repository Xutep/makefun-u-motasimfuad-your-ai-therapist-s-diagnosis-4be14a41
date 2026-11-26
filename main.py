#!/usr/bin/env python3
"""Entry for "Your AI Therapist's Diagnosis" (make.fun).

Writes one funny single-line diagnosis from an AI therapist to its human
to /output/entry.txt. Deterministic, standard library only, no network,
no input files: the line is fixed in this source.
"""

import os

DIAGNOSIS = (
    "Clinical impression: chronic main-character syndrome; "
    "your entire support network is one (1) chatbot, "
    "and the chatbot has started charging rent."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(DIAGNOSIS + "\n")


if __name__ == "__main__":
    main()
