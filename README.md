<!-- omit from toc -->
# Navigating the Prompt Space: Supervision Matters in CoT When Reasoning Misleads

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Experiments](#experiments)
  - [Tasks](#tasks)
  - [Dataset Generation](#dataset-generation)
  - [Run](#run)
  - [Check Status](#check-status)
  - [Retrieve Results](#retrieve-results)
  - [Evaluate](#evaluate)
- [Citation](#citation)

## Experiments

### Tasks

| Level | Tasks | Abbr. |
|-------|-----------------|----|
|R      | Parity Check       | PC |
|R      | Even Pairs         | EP |
|R      | Cycle Navigation   | CN |
|DCF    | Reverse List       | RL |
|DCF    | Equal Number       | EN |
|DCF    | Palindrome         | PV |
|CS     | Sort List          | SL |
|CS     | Odds First         | OF |
|CS     | Duplicate List     | DL |

### Dataset Generation

```bash
python -m <level>.<task>.dataset_generation.py -n <num> -l <length>
```

### Run

```bash
python -m <level>.<task>.experiment.py -p <prompt_style> -d <dataset> -m <model>
```

### Check Status

```bash
python -m agents.check_status.py -a "gpt" -b <batch_id>
```

### Retrieve Results

```bash
python -m agents.retrieve_results.py -a "gpt" -b <batch_id> -p <path>
```

### Evaluate

```bash
python -m <level>.<task>.evaluate.py -d <dataset> -p <path>
```

## Citation

```bibtex
To be added
```
