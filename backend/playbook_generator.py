import os

def save_playbook(content):

    os.makedirs("ansible", exist_ok=True)

    file_path = "ansible/generated_playbook.yml"

    with open(file_path, "w") as file:
        file.write(content)

    return file_path