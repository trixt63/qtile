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


def get_mpris2_instance():
    try:
        result = subprocess.run(['playerctl', '-l'], capture_output=True, text=True, check=True)
        output_lines = list(result.stdout.splitlines())

        # Find the line that starts with 'firefox'
        firefox_line = next((line for line in output_lines if line.startswith('firefox')), None)

        return firefox_line

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None
    
    
def get_highlight_color(colors):
    """Get the highlight_color (the background color) 
    for the GroupBox when highlight_method='line',
    in case the color scheme does not have 'background_focus_2'
    """
    colors_list = [colors.get('background_focus_2'),
                   colors.get('background_unfocus'),
                   colors.get('background_other')]
    return next(color for color in colors_list if color is not None)

