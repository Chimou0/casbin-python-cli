import subprocess


def get_base_tag():
    try:
        command = ["git", "describe", "--tags", "--abbrev=0"]

        tag = subprocess.check_output(
            command, text=True, stderr=subprocess.PIPE
        ).strip()

        if tag.startswith("v"):
            return tag[1:]
        return tag

    except subprocess.CalledProcessError:
        print("Error: Failed to find any git tags.")
        return None


__version__ = get_base_tag()
