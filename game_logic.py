import PySimpleGUI as sg

# Define the column layout
image_column1 = [
    [sg.Image(sg.EMOJI_BASE64_READING), sg.Image(sg.EMOJI_BASE64_READING), sg.Image(sg.EMOJI_BASE64_READING), sg.Image(sg.EMOJI_BASE64_READING), sg.Image(sg.EMOJI_BASE64_READING)]
]

# Define the main layout
layout = [
    [sg.Column(image_column1, element_justification='center')]
]

# Create the window
window = sg.Window('Demo Window', layout, finalize=True)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()