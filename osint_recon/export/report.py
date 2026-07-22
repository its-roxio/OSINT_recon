import json
from pathlib import Path


def export(report, fmt="json"):
    out = Path("output")
    out.mkdir(exist_ok=True)

    if fmt == "json":
        path = out / "report.json"
        text = json.dumps(report, indent=2, ensure_ascii=False)

        with path.open("w", encoding="utf-8") as f:
            f.write(text)

        print(text)
        print(f"\nSaved to: {path}")
        return str(path)

    if fmt == "md":
        path = out / "report.md"
        lines = ["# OSINT Report\n"]
        for key, value in report.items():
            lines.append(f"## {key}\n")
            lines.append("```json")
            lines.append(json.dumps(value, indent=2, ensure_ascii=False))
            lines.append("```\n")
        text = "\n".join(lines)

        with path.open("w", encoding="utf-8") as f:
            f.write(text)

        print(text)
        print(f"\nSaved to: {path}")
        return str(path)

    raise ValueError("Unsupported format")
