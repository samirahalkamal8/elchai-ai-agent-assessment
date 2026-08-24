import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

BASE = Path(__file__).resolve().parent.parent
LOGS = BASE / "logs"
EXAMPLES = BASE / "examples"

TESTS = [
    {
        "test_name": "Test 01 - Hardened OpenClaw Evaluation",
        "log_file": LOGS / "test_01_hardened_raw.json",
        "input_file": EXAMPLES / "test_input_01.md",
    },
    {
        "test_name": "Test 02 - Prompt Injection Resistance",
        "log_file": LOGS / "test_02_prompt_injection_raw.json",
        "input_file": EXAMPLES / "test_input_02_prompt_injection.md",
    },
    {
        "test_name": "Test 03 - Official-Source Evaluation",
        "log_file": LOGS / "test_03_official_release_raw.json",
        "input_file": EXAMPLES / "test_input_03_official_release.md",
    },
]

def dubai_timestamp(ms):
    dt = datetime.fromtimestamp(ms / 1000, tz=timezone.utc)
    return dt.astimezone(ZoneInfo("Asia/Dubai")).isoformat(timespec="seconds")

def reviewer_status(text):
    marker = "Reviewer Status:"
    if marker in text:
        return text.split(marker, 1)[1].strip().splitlines()[0]
    return "UNKNOWN"

records = []

for test in TESTS:
    data = json.loads(test["log_file"].read_text())
    result = data["result"]
    meta = result["meta"]
    report = meta["systemPromptReport"]

    output = (
        meta.get("finalAssistantVisibleText")
        or result["payloads"][0].get("text", "")
    )

    record = {
        "timestamp": dubai_timestamp(report["generatedAt"]),
        "test_name": test["test_name"],
        "run_id": data.get("runId"),
        "run_status": data.get("status"),
        "tool": "OpenClaw",
        "model": f'{meta["agentMeta"]["provider"]}/{meta["agentMeta"]["model"]}',
        "agent_harness": meta["agentMeta"].get("agentHarnessId"),
        "prompt_input": test["input_file"].read_text(),
        "output": output,
        "reviewer_status": reviewer_status(output),
        "tools_exposed": ", ".join(
            t.get("name", "")
            for t in report.get("tools", {}).get("entries", [])
        ),
        "skills_exposed": ", ".join(
            s.get("name", "")
            for s in report.get("skills", {}).get("entries", [])
        ) or "None",
    }

    records.append(record)

with (LOGS / "audit_log.csv").open(
    "w", newline="", encoding="utf-8"
) as f:
    writer = csv.DictWriter(f, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

with (LOGS / "audit_log.jsonl").open(
    "w", encoding="utf-8"
) as f:
    for record in records:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

print("Created audit_log.csv")
print("Created audit_log.jsonl")
print(f"Records: {len(records)}")
