import argparse
import json
import random

def generate_random_string(length: int) -> str:
    random_str = ''.join(random.choice("ab") for _ in range(length))
    return random_str

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--num",
        type=int,
        help="Number of samples to generate."
    )
    parser.add_argument(
        "-l", "--length",
        required=True,
        type=int,
        help="The length of samples."
    )
    
    args = parser.parse_args()
    
    dataset = []
    for i in range(args.num):
        seq = generate_random_string(args.length)
        dataset.append({"id": i, "string": seq, "duplicate": seq * 2})
    out_file = f"CS/duplicate_string/datasets/dup_{args.length}.jsonl"
    
    with open(out_file, "w") as file:
        for item in dataset:
            file.write(json.dumps(item) + '\n')
            
    print(f"Dataset successfully saved to {out_file}")
    
if __name__ == "__main__":
    main()