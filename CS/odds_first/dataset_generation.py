import argparse
import json
import random
import string

def generate_random_string(length: int) -> str:
    random_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
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
        odds = seq[1::2]
        evens = seq[0::2]
        
        dataset.append({"id": i, "string": seq, "odds_first": odds + evens})
        out_file = f"CS/odds_first/datasets/of_{args.length}.jsonl"
    
    with open(out_file, 'w') as file:
        for line in dataset:
            file.write(json.dumps(line) + "\n")
    print(f"Dataset successfully saved to {out_file}.")
    
if __name__ == "__main__":
    main()