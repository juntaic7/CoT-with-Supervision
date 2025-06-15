<!-- omit from toc -->
# Why Prompt Design Matters and Works: A Complexity Analysis of Prompt Search Space in LLMs

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
@misc{zhang2025promptdesignmattersworks,
      title={Why Prompt Design Matters and Works: A Complexity Analysis of Prompt Search Space in LLMs}, 
      author={Xiang Zhang and Juntai Cao and Jiaqi Wei and Chenyu You and Dujian Ding},
      year={2025},
      eprint={2503.10084},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.10084}, 
}
```
