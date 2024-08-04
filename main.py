<<<<<<< Updated upstream
import PySimpleGUI as sg
import os

sg.theme('black')  # Let's set our own color theme

# Define the relative path to the images folder
IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), 'Guess_Who_PNGs')
black_PNG = os.path.join(IMAGE_FOLDER, 'Solid_black.png')

image_column1 = [
    [sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char1'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char2'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char3'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char4')]
    ]
image_column2 = [
    [sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char5'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char6'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char7'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char8')]
    ]
image_column3 = [
    [sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char9'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char10'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char11'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char12')]
    ]
image_column4 = [
    [sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char13'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char14'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char15'), sg.Image(sg.EMOJI_BASE64_READING, zoom=3, enable_events=True, key='char16')]
    ]
# STEP 1 define the layout
layout = [ 
            [sg.Text('GUESS WHO?',size=(20,), text_color='red', font=('bold', 80), justification='center')],
            [sg.Column(image_column1, element_justification='center')],
            [sg.Column(image_column2, element_justification='center')],
            [sg.Column(image_column3, element_justification='center')],
            [sg.Column(image_column4, element_justification='center')]
         ]

#STEP 2 - create the window
window = sg.Window('Guess_Who.exe', layout, location=(0,0), size=(1920,1080), element_justification='center')

# STEP3 - the event loop
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
      break
    
    if event.startswith('char'):
        # Replace the image associated with the clicked element with Solid_black.png
        window[event].update(filename=black_PNG)
window.close()
=======
from PIL import Image as img

# loads image
image_path = 'portraits/img2.png'
image = img.open(image_path)



# Show the cropped image
image.show()
>>>>>>> Stashed changes
