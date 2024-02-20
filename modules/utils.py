import subprocess


def get_firefox_instance():
    # Run the playerctl command and capture the output
    try:
        result = subprocess.run(['playerctl', '-l'], capture_output=True, text=True, check=True)
        output_lines = result.stdout.splitlines()

        # Find the line that starts with 'firefox'
        firefox_line = next((line for line in output_lines if line.startswith('firefox')), None)

        return firefox_line

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

