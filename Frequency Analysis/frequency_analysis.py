# frequency_analysis.py

def analyze_frequency(text):
    """
    Performs frequency analysis on a given piece of text.

    :param text: The input text for frequency analysis.
    :return: A dictionary containing the frequency of each letter.
    """
    frequency = {}

    for char in text:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char, 0) + 1

    total_characters = sum(frequency.values())

    # Calculate frequencies as percentages
    for char, count in frequency.items():
        frequency[char] = (count / total_characters) * 100

    # Sort the dictionary by frequency in descending order
    frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

    return frequency


def main():
    """
    Main function to demonstrate the usage of frequency analysis.
    """
    sample_text = "This is a sample text for frequency analysis."

    # Perform frequency analysis
    frequency_result = analyze_frequency(sample_text)

    # Display the results
    print("Frequency Analysis Result:")
    for char, percentage in frequency_result.items():
        print(f"{char}: {percentage:.2f}%")


if __name__ == "__main__":
    main()
