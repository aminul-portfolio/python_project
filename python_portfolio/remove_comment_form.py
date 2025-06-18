import os
import re

BASE_DIR = os.path.join(os.path.dirname(__file__), 'core', 'templates')

def remove_comment_form(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove any existing include of comment_form.html
    new_content = re.sub(r"\s*{% include ['\"]includes/comment_form\.html['\"] %}\s*", "", content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"🗑️ Removed comment form from: {file_path}")
    else:
        print(f"✅ No comment form found in: {file_path}")

def clean_all():
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith('.html'):
                remove_comment_form(os.path.join(root, file))

if __name__ == "__main__":
    clean_all()
