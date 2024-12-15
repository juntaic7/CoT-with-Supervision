import argparse
import json
import random
import string

def generate_random_string(length: int) -> str:
    random_str = ''.join(random.choice(string.ascii_letters) for _ in range(length))
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
        dataset.append({"id": i, "string": seq, "sorted": ''.join(sorted(seq))})
        out_file = f"CS/sorting/datasets/sort_{args.length}.jsonl"
    
    with open(out_file, 'w') as file:
        for line in dataset:
            file.write(json.dumps(line) + "\n")
    print(f"Dataset successfully saved to {out_file}.")
    
if __name__ == "__main__":
    main()