from itertools import permutations

def generate_wordlist(words, min_length, max_length):
    wordlist = set()
    for i in range(min_length, max_length + 1):
        for combo in permutations(words, i):
            wordlist.add("".join(combo))
    
    with open("wordlist.txt", "w") as f:
        for word in wordlist:
            f.write(word + "\n")

    print(f"{GREEN}[SUCCESS]{RESET} Wordlist saved as wordlist.txt")

generate_wordlist(["admin", "123", "pass"], 1, 3
