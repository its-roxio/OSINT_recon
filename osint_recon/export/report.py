import json
from pathlib import Path


def export(report, fmt="json"):
    out = Path("output")
    out.mkdir(exist_ok=True)

    if fmt == "json":
        path = out / "report.json"
        with path.open("w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        return str(path)

    if fmt == "md":
        path = out / "report.md"
        with path.open("w", encoding="utf-8") as f:
            f.write("# OSINT Report\n\n")
            for key, value in report.items():
                f.write(f"## {key}\n\n")
                f.write("```json\n")
                f.write(json.dumps(value, indent=2, ensure_ascii=False))
                f.write("\n```\n\n")
        return str(path)

    raise ValueError("Unsupported format")
