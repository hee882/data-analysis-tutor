with open(r'C:\Users\user\Desktop\HDAT-DA\data-analysis-tutor\README.md', 'r', encoding='utf-8') as f:
    text = f.read()

badges = '''
<div align="center">
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/version-v1.0.0-success.svg?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green.svg?style=flat-square" alt="License">
</div>

'''

lines = text.split('\n')
for i, line in enumerate(lines):
    if line.startswith('# '):
        lines.insert(i+1, badges)
        break

with open(r'C:\Users\user\Desktop\HDAT-DA\data-analysis-tutor\README.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
