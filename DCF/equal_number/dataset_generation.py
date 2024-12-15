import argparse
import json
import random

def is_valid_sequence(seq: str) -> bool:
    # Check if counts are equal at the end
    if seq.count('0') != seq.count('1'):
        return False
    
    # Check prefix condition
    count_0 = 0
    count_1 = 0
    for char in seq:
        if char == '0':
            count_0 += 1
        else:
            count_1 += 1
        if count_0 < count_1:
            return False
    return True

def generate_valid_string(length:int) -> str:
    """Generate a valid string of a given length."""
    if length % 2 != 0:
        raise ValueError("Length must be even to balance 0s and 1s.")
    
    string = []
    count_0, count_1 = 0, 0
    
    for _ in range(length):
        remaining = length - len(string)  # Remaining slots to fill
        if count_0 == count_1:
            # Must add 0 to maintain the prefix constraint
            string.append('0')
            count_0 += 1
        elif count_0 < length // 2 and (remaining - 1 >= (length // 2 - count_1)):
            # Add 0 if it won't prevent balancing
            string.append('0')
            count_0 += 1
        else:
            # Add 1 if adding more 0s would make balancing impossible
            string.append('1')
            count_1 += 1
    
    return ''.join(string)

def generate_invalid_sequence(length: int) -> str:
    if length % 2 != 0:
        return None
    
    # Create a list with equal numbers of 0s and 1s
    seq = ['0'] * (length // 2) + ['1'] * (length // 2)
    
    # Keep shuffling until we get an invalid sequence
    max_attempts = 100
    while max_attempts > 0:
        random.shuffle(seq)
        if not is_valid_sequence(''.join(seq)):
            return ''.join(seq)
        max_attempts -= 1
    
    return None

def generate_samples(n_samples: int, length: int, target_true_ratio: float = 0.4) -> list[dict[str, any]]:
    dataset = []
    n_true = int(n_samples * target_true_ratio)
    n_false = n_samples - n_true
    
    # Generate valid sequences
    true_count = 0
    while true_count < n_true:
        seq = generate_valid_string(length)
        if is_valid_sequence(seq):
            dataset.append({'string': seq, 'valid': True})
            true_count += 1
    
    # Generate invalid sequences
    false_count = 0
    while false_count < n_false:
        seq = generate_invalid_sequence(length)
        if seq is not None and not is_valid_sequence(seq):
            dataset.append({'string': seq, 'valid': False})
            false_count += 1

    random.shuffle(dataset)
    return dataset
def main():
    parser = argparse.ArgumentParser(description="Generate a dataset of reversing string task.")
    parser.add_argument(
        "-n", "--num",
        type=int,
        help="Number of samples to generate."
    )
    parser.add_argument(
        "-l", "--length",
        required=True,
        type=int,
        help="Lower bound of sample length."
    )
    parser.add_argument(
        "-r", "--ratio",
        default=0.4,
        type=float,
        help="Select the percentage of valid sequence."
    )
    args = parser.parse_args()

    length = args.length
    dataset = generate_samples(1000, length)
    for idx, sample in enumerate(dataset):
        sample['id'] = idx

    # Verify the distribution
    true_count = sum(1 for sample in dataset if sample['valid'])
    print(f"Total samples: {len(dataset)}")
    print(f"Valid sequences (True): {true_count} ({true_count/len(dataset)*100:.1f}%)")
    print(f"Invalid sequences (False): {len(dataset)-true_count} ({(len(dataset)-true_count)/len(dataset)*100:.1f}%)")

    # Verify all sequences have equal numbers of 0s and 1s
    all_balanced = all(sample['string'].count('0') == sample['string'].count('1') for sample in dataset)
    print(f"\nAll sequences have equal 0s and 1s: {all_balanced}")
    out_file = f"DCF/equal_number/datasets/en_{args.length}.jsonl"
    
    with open(out_file, "w") as file:
        for item in dataset:
            file.write(json.dumps(item) + '\n')
            
    print(f"Dataset successfully saved to {out_file}")
            
if __name__ == "__main__":
    main()
