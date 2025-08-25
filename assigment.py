def add_neuroanatomy_fact(line):
    # Simple enrichment: add a neuroanatomy fact to each line
    facts = [
        "The hippocampus is crucial for memory formation.",
        "The cerebellum coordinates voluntary movements.",
        "The amygdala processes emotions like fear and pleasure.",
        "The corpus callosum connects the brain's two hemispheres.",
        "The prefrontal cortex is key to decision-making and personality."
    ]
    import random
    return f"{line.strip()} — Fact: {random.choice(facts)}\n"

def main():
    input_filename = input("Enter the filename containing neuroanatomy notes: ")

    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
        return
    except IOError:
        print(f"❌ Error: The file '{input_filename}' could not be read.")
        return

    output_filename = "enhanced_neuroanatomy_notes.txt"
    try:
        with open(output_filename, 'w') as outfile:
            for line in lines:
                modified_line = add_neuroanatomy_fact(line)
                outfile.write(modified_line)
        print(f"✅ Success! Modified notes saved to '{output_filename}'.")
    except IOError:
        print(f"❌ Error: Could not write to '{output_filename}'.")

if __name__ == "__main__":
    main()