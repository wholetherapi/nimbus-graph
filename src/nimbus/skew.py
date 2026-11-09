"""Skew-aware workload generation."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List


@dataclass
class SkewWorkload:
    vertices: int
    edges: int
    hot_fraction: float
    seed: int = 7

    def generate(self) -> List[tuple[int, int]]:
        rng = random.Random(self.seed)
        hot = max(1, int(self.vertices * self.hot_fraction))
        edges = []
        for _ in range(self.edges):
            if rng.random() < self.hot_fraction:
                source = rng.randrange(hot)
            else:
                source = rng.randrange(self.vertices)
            target = rng.randrange(self.vertices)
            edges.append((source, target))
        return edges
