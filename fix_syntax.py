import os

repo_path = r'C:\Users\user\Desktop\HDAT-DA\data-analysis-tutor'
style_path = os.path.join(repo_path, 'src', 'style.py')

with open(style_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure it ends with """ properly
if not content.strip().endswith('"""'):
    content += '\n"""\n'
    with open(style_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed missing quotes!")
else:
    print("Quotes are already there?")
