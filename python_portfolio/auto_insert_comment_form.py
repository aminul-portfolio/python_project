import os

COMMENT_INCLUDE = '{% include \'includes/comment_form.html\' %}'
TARGET_DIV_ID = 'id="exampleCards"'

def insert_comment_after_last_card(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if any(COMMENT_INCLUDE in line for line in lines):
        print(f"⚠️ Skipping (already included): {file_path}")
        return

    inside_example_block = False
    last_card_end_index = -1

    for i, line in enumerate(lines):
        if TARGET_DIV_ID in line:
            inside_example_block = True

        if inside_example_block:
            if '<div class="card' in line:
                current_card_index = i
            if '</div>' in line:
                last_card_end_index = i

        if inside_example_block and '</div>' in line and 'id="exampleCards"' in line:
            break  # End of examples section

    if last_card_end_index != -1:
        lines.insert(last_card_end_index + 1, f'  {COMMENT_INCLUDE}\n')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f"✅ Inserted in: {file_path}")
    else:
        print(f"⏭️ No .card blocks found inside #exampleCards in {file_path}")


def process_html_directory(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.html'):
                full_path = os.path.join(root, file)
                insert_comment_after_last_card(full_path)


# 🔁 Set the correct path to your template root
TEMPLATE_FOLDER = os.path.join(os.getcwd(), 'core', 'templates')
process_html_directory(TEMPLATE_FOLDER)
