import re

def find_first_last_number(line):
    # Define a regular expression pattern to match digits and English numbers
    pattern = re.compile(r'\b(?:[0-9]|one|two|three|four|five|six|seven|eight|nine)\b', re.IGNORECASE)

    # Find all matches in the line
    matches = pattern.findall(line)

    if matches:
        # Extract the first and last match
        first_number = str(matches[0])
        last_number = str(matches[-1])

        # Concatenate the first and last numbers
        concatenated_number = int(first_number + last_number)

        return concatenated_number
    else:
        # No numbers found in the line
        return 0

# Read input.txt and process each line
total_sum = 0
with open('input.txt', 'r') as file:
    for line_number, line in enumerate(file, start=1):
        line_sum = find_first_last_number(line)
        total_sum += line_sum

# Print the total sum of concatenated numbers
print(f"Total Sum of Concatenated Numbers: {total_sum}")
