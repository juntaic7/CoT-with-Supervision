import argparse
import json
import random
import string

    
def generate_palindrome_dataset(num_samples: int, length: int) -> list[dict]:
    if length % 2 == 0:
        raise ValueError("Length must be odd to accommodate the '#' marker")
    
    dataset = []
    half_length = (length - 1) // 2
    
    for i in range(num_samples):
        # Generate left half of the string
        left = ''.join(random.choices(string.ascii_lowercase, k=half_length))
        
        # For valid palindromes (40% of samples)
        if random.random() < 0.4:
            # Right side is mirror of left
            right = left[::-1]
            valid = True
        else:
            # For invalid palindromes, shuffle the right side
            right_chars = list(left[::-1])
            while right_chars == list(left[::-1]):  # Ensure it's different from the palindrome
                random.shuffle(right_chars)
            right = ''.join(right_chars)
            valid = False
            
        # Combine left + '#' + right
        seq = f"{left}#{right}"
        
        # Create dictionary entry
        entry = {
            'id': i,
            'string': seq,
            'valid': valid,
        }
        
        dataset.append(entry)
    
    return dataset
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
        help="Lower bound of sample length."
    )
    args = parser.parse_args()

    dataset = generate_palindrome_dataset(args.num, args.length)
    out_file = f"DCF/palindrome/datasets/pal_{args.length}.jsonl"
    
    with open(out_file, "w") as file:
        for item in dataset:
            file.write(json.dumps(item) + '\n')
            
    print(f"Dataset successfully saved to {out_file}")
            
if __name__ == "__main__":
    main()