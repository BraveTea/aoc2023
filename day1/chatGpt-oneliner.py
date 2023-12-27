print(sum(int(str(m[0]) + str(m[-1])) if m else 0 for m in (re.findall(r'\b(?:[0-9]|one|two|three|four|five|six|seven|eight|nine)\b', line, re.IGNORECASE) for line in open('input.txt', 'r'))))
