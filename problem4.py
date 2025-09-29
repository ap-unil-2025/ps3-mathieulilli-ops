"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    """
    Count total words in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of words
    """
    with open(filename, "r") as f:
        content = f.read()

    words = content.split()   # sépare en liste de mots (par espaces, retours à la ligne, etc.)
    return len(words)


def count_lines(filename):
    """
    Count total lines in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        int: Total number of lines
    """
    with open(filename, "r") as f:
        lines = f.readlines()   # lit toutes les lignes dans une liste
    return len(lines)


def count_characters(filename, include_spaces=True):
    """
    Count characters in the file.

    Args:
        filename (str): Name of the file to analyze
        include_spaces (bool): Whether to include spaces in count

    Returns:
        int: Total number of characters
    """
    with open(filename, "r") as f:
        content = f.read()

    if include_spaces:
        return len(content)
    else:
        return len(content.replace(" ", "").replace("\n", ""))


def find_longest_word(filename):
    """
    Find and return the longest word in the file.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        str: The longest word found
    """
    with open(filename, "r") as f:
        content = f.read()

    # Enlever la ponctuation
    for punct in string.punctuation:
        content = content.replace(punct, "")

    words = content.split()

    if not words:
        return None  # fichier vide

    return max(words, key=len)


def word_frequency(filename):
    """
    Return a dictionary of word frequencies.
    Convert words to lowercase and remove punctuation.

    Args:
        filename (str): Name of the file to analyze

    Returns:
        dict: Dictionary with words as keys and frequencies as values
    """
    import string

    frequency = {}

    with open(filename, "r") as f:
        content = f.read()

    # mettre en minuscules
    content = content.lower()

    # enlever la ponctuation
    for punct in string.punctuation:
        content = content.replace(punct, "")

    # séparer en mots
    words = content.split()

    # compter les occurrences
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency


def analyze_file(filename):
    """
    Perform complete analysis of the file.

    Args:
        filename (str): Name of the file to analyze
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        # Display all analyses
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        # Display top 5 most common words
        print("\nTop 5 most common words:")
        freq = word_frequency(filename)

        # Sort by frequency and get top 5
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()