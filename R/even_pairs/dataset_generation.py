import argparse
import json
import random

def generate_sample(length: int) -> str:
    """Generates a random string of 'a' and 'b' with length between min_len and max_len."""
    sample = ''.join(random.choice('ab') for _ in range(length))
    return sample

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--num",
        type=int,
        required=True,
        help="Number of samples to generate." 
    )
    parser.add_argument(
        "-l", "--length",
        type=int,
        required=True,
        help="Length of the samples."
    )
    
    args = parser.parse_args()
    dataset = []
    
    for i in range(args.num):
        seq = generate_sample(args.length)
        dataset.append({"id": i, "string": seq, "count": seq.count('ab') + seq.count('ba')})
    out_file = f"R/even_pairs/datasets/ep_{args.length}.jsonl"
    
    with open(out_file, "w") as file:
        for item in dataset:
            file.write(json.dumps(item) + '\n')
            
    print(f"Dataset successfully saved to {out_file}")
            
if __name__ == "__main__":
    main()