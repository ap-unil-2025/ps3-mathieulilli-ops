"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        user_input = input("Enter a number (or type 'done' to finish): ").strip()

        # Check if user typed 'done'
        if user_input.lower() == "done":
            break

        try:
            # Try to convert to float and add to list
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            # Handle invalid input gracefully
            print("Invalid input! Please enter a number or 'done' to finish.")

    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}

    # Calculate count
    analysis["count"] = len(numbers)

    # Calculate sum
    analysis["sum"] = sum(numbers)

    # Calculate average
    analysis["average"] = analysis["sum"] / analysis["count"]

    # Find minimum
    analysis["minimum"] = min(numbers)

    # Find maximum
    analysis["maximum"] = max(numbers)

    # Count even and odd numbers
    even_count = sum(1 for n in numbers if n % 2 == 0)
    odd_count = sum(1 for n in numbers if n % 2 != 0)

    analysis["even_count"] = even_count
    analysis["odd_count"] = odd_count

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers: {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()