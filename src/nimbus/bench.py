"""Benchmark driver for Nimbus-Graph."""

from __future__ import annotations

import argparse
import json
import time
from collections import defaultdict
from pathlib import Path

from .skew import SkewWorkload


def run_ingestion(edges, report_every: int = 1000):
    adjacency = defaultdict(list)
    start = time.perf_counter()
    for index, (source, target) in enumerate(edges, start=1):
        adjacency[source].append(target)
        if index % report_every == 0:
            elapsed = time.perf_counter() - start
            print(f"ingested={index} rate={index / max(elapsed, 1e-9):.0f}/s")
    elapsed = time.perf_counter() - start
    return {"edges": len(edges), "seconds": elapsed, "rate": len(edges) / max(elapsed, 1e-9)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workload", required=True)
    args = parser.parse_args()
    spec = json.loads(Path(args.workload).read_text())
    workload = SkewWorkload(**spec)
    result = run_ingestion(workload.generate())
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
