import os
from collections import defaultdict

class Node():
    def __init__(self):
        self.count = 0 

def freqAnal():
    cipher = "RN PBYNXARLMRB RGQA, TNXAQPBL RGB SNWWNDQXI SWMI: TA2107{E0V_S0VXP_7G3_SL3UVBXTE_NS_RG3_S14I}. HE ARVPEQXI RGB SLBUVBXTE NS WBRRBLA QX MX BXTLECRBP YBAAMIB MXP TNYCMLQXI RGBY RN RGB JXNDX SLBUVBXTE PQARLQHVRQNX NS WBRRBLA QX BXIWQAG, NXB TMX NSRBX PBRBLYQXB RGB AVHARQRVRQNX CMRRBLX VABP HE RGB TQCGBL"
    
    # Output text initialized with underscores
    output_text = ['_'] * len(cipher)
    replacements = []  # Stack to keep track of replacements

    # Function to calculate and print the top 7 frequencies
    def print_top_frequencies(text, ignored_chars):
        freqDict = defaultdict(Node)
        for char in text:
            if char not in ignored_chars and char != '_':  # Ignore replaced characters and underscores
                curr = freqDict[char]
                curr.count += 1

        freqList = [(char, node.count) for char, node in freqDict.items()]
        freqList.sort(key=lambda x: x[1], reverse=True)

        print("\nTop 7 Most Frequent Characters:")
        for char, count in freqList[:7]:
            print(f"'{char}': {count}")

    # Set to hold ignored characters
    ignored_chars = set()

    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print("Cipher Text:")
        print(cipher)
        print("\nOutput Text:")
        print(''.join(output_text))
        print_top_frequencies(cipher, ignored_chars)
        # Input for character replacement or undo
        user_input = input("\nEnter replacement (e.g., e:g) or 'h' for help: ")
        if user_input.lower() =='h' or user_input.lower() == 'help':
            os.system('cls' if os.name == 'nt' else 'clear')           
            print('ciphertext:guess: replacements')
            print('undo(ciphertext:guess): undo move stated')
            print('q/quit: close program')
            print('history: sees past move in a set')
            print('h: help\n')
            continue
        if user_input.lower() == 'q' or user_input.lower() == 'quit':
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        if user_input.lower() == 'history':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(set(replacements))
            continue
        
        try:
            if user_input.startswith("undo(") and user_input.endswith(")"):
                # Handle undo
                undo_input = user_input[5:-1]
                dst, src = undo_input.split(':')
                print((dst, src))
                if len(src) != 1 or len(dst) != 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Please enter a single character replacement")
                    continue

                # Reverse the last replacement (dst to src)
                if (dst, src) in replacements:
                    replacements.remove((dst, src))  # Remove the inverse replacement

                    # Restore all instances of the original character in the cipher
                    for i in range(len(cipher)):
                        if output_text[i] == src:
                            output_text[i] = '_'  # Remove the character from output
                            cipher = cipher[:i] + dst + cipher[i+1:]  # Restore the original character
                            ignored_chars.discard(dst)  # Allow the character to be counted again

                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Undo successful.")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"No inverse replacement found for '{dst}:{src}'.")
                continue

            # Handle replacement
            src, dst = user_input.split(':')
            if len(src) != 1 or len(dst) != 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Please enter a single character replacement.")
                continue

            # Update the output text and cipher text
            for i in range(len(cipher)):
                if cipher[i] == src:
                    output_text[i] = dst  # Add new character to output
                    cipher = cipher[:i] + '_' + cipher[i+1:]  # Replace character with '_'
                    ignored_chars.add(src)  # Add replaced character to ignored set
                    replacements.append((src, dst))  # Record the replacement

            os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid format. Please use 'source:destination' format.")

# Call the function
freqAnal()
