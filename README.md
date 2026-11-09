# Nimbus-Graph

Reference implementation of **Nimbus-Graph**, a streaming graph benchmark for
highly skewed arrival patterns.

## Repository layout

- `src/nimbus/bench.py` - benchmark driver and scoring harness.
- `src/nimbus/skew.py` - workload generator with configurable skew.
- `data/workloads/small.json` - a small deterministic workload for smoke tests.
- `experiments/skew_sweep.yaml` - parameters for the skew sweep in the paper.

## Running the harness

```bash
pip install -r requirements.txt
python -m nimbus.bench --workload data/workloads/small.json
```

## License

MIT.
