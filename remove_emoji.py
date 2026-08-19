import sys, re

# Read original message from stdin
msg = sys.stdin.read()

# Lines to preserve empty lines or multi-line commits
lines = msg.split('\n')
new_lines = []

for idx, line in enumerate(lines):
    if idx == 0 or line.strip(): # Apply to first line or non-empty lines
        # Remove any character that is NOT:
        # alphanumeric, space, colon, ampersand, hyphen, parens, Korean, punctuation
        clean = re.sub(r'[^\w\s:&\-()가-힣.,/\[\]_]+', '', line)
        clean = re.sub(r'\s+', ' ', clean).strip()
        new_lines.append(clean)
    else:
        new_lines.append(line)

sys.stdout.write('\n'.join(new_lines) + '\n')
