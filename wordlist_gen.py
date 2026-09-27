import argparse, itertools

def generate_wordlist(characters, min_length, max_length, output_file):
    with open(output_file, 'w') as file:
        for length in range(min_length, max_length + 1):
            for combination in itertools.product(characters, repeat=length):
                word = ''.join(combination)
                file.write(word + '\n')

parser = argparse.ArgumentParser(description="Generate a custom wordlist similar to crunch.")

parser.add_argument("-c", "--characters", type=str, default="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                    help="Set of characters to include in the worldlist")
parser.add_argument("-min", "--min_length", type=int, default=4, help="Minimum length of the words")
parser.add_argument("-max", "--max_length", type=int, default=6, help="Maximum length of the words")
parser.add_argument("-o", "--output_file", type=str, default="custom_wordlist.txt", help="Output file name")


args = parser.parse_args()

generate_wordlist(args.characters, args.min_length, args.max_length, args.output_file)

print(f"[+] Wordlist generated and saved to {args.output_file}")





















