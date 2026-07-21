import json
import re
from collections import Counter
from pathlib import Path

REPORT = Path("/app/report.json")
LOG = Path("/app/access.log")


def expected_report():
    paths = Counter()
    ips = set()
    total = 0

    with LOG.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            total += 1
            ips.add(line.split()[0])

            m = re.search(r'(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1

    return {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0],
    }


def test_report_exists():
    assert REPORT.exists(), "no report.json found"


def test_report_contents():
    data = json.loads(REPORT.read_text())
    assert data == expected_report()