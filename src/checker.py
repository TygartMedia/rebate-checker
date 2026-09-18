#!/usr/bin/env python3
"""Rebate Checker — nameplate photo + ZIP in, program verdict out.

Pipeline:
    photo -> equipment identifiers (vision model) -> program-status lookup -> verdict

Current state: scaffold. Extraction and program lookup are stubs with TODO
markers; the CLI and the verdict contract are real.
"""
import argparse
import json
import sys


def extract_equipment(photo_path):
    """TODO: vision-model call. Returns manufacturer, model_number,
    serial_number, fuel_type, capacity — uncertain characters marked as
    uncertain, never presented as certain."""
    print(f"[stub] extracting equipment identifiers from {photo_path} ...", file=sys.stderr)
    return {
        "manufacturer": None,
        "model_number": None,
        "serial_number": None,
        "fuel_type": None,
        "capacity": None,
        "note": "STUB — wire up the vision call (see prompts/first-pass.md)",
    }


def lookup_program(equipment, zip_code):
    """TODO: look up data/programs.json for the equipment + ZIP.

    Verdict is one of: open | reserved | paused | closed | fuel_switch_blocked
    """
    print(f"[stub] looking up program status for ZIP {zip_code} ...", file=sys.stderr)
    return {
        "verdict": "STUB",
        "program": None,
        "note": "STUB — needs the program-status table (see data/README.md)",
    }


def main():
    ap = argparse.ArgumentParser(
        description="Rebate Checker: nameplate photo + ZIP against open rebate programs."
    )
    ap.add_argument("--photo", required=True, help="Path to the nameplate/sticker photo")
    ap.add_argument("--zip", required=True, dest="zip_code", help="Property ZIP code")
    args = ap.parse_args()

    equipment = extract_equipment(args.photo)
    result = lookup_program(equipment, args.zip_code)
    print(json.dumps({"equipment": equipment, "result": result}, indent=2))


if __name__ == "__main__":
    main()
