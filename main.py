import PySimpleGUI as sg
import os
import random

sg.theme('black')  


IMAGE_FOLDER = os.path.join(os.path.dirname(__file__), 'Guess_Who_PNGs')


all_images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().startswith('img')]


if len(all_images) < 12:
    raise ValueError("Not enough images in the folder. Please add at least 12 PNG images.")


random.shuffle(all_images)


random_image = os.path.join(IMAGE_FOLDER, random.choice(all_images))


image_column1 = [
    [sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[0]), size=(200, 200), enable_events=True, key='char1'),
     sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[1]), size=(200,200), enable_events=True, key='char2'),
     sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[2]), size=(200,200), enable_events=True, key='char3'),
     sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[3]), size=(200,200), enable_events=True, key='char4')],
    [sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[4]), size=(200,200), enable_events=True, key='char5'),
     sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[5]), size=(200,200), enable_events=True, key='char6'),
     sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[6]), size=(200,200), enable_events=True, key='char7'),
     sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[7]), size=(200,200), enable_events=True, key='char8')],
    [sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[8]), size=(200,200), enable_events=True, key='char9'),
     sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[9]), size=(200,200), enable_events=True, key='char10'),
     sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[10]), size=(200,200), enable_events=True, key='char11'),
     sg.Image(filename=os.path.join(IMAGE_FOLDER, all_images[11]), size=(200,200), enable_events=True, key='char12')],
]


black_PNG = os.path.join(IMAGE_FOLDER, 'Solid_black.png')


layout = [
    [sg.Text('GUESS WHO?', size=(20,), text_color='red', font=('bold', 50), justification='center')],
    [
        sg.Column(
            [[sg.Text('Player Character', text_color='red', font=('bold', 20), justification='center')],
             [sg.Image(filename=random_image, size=(300, 200), key='PlayerChar')]],
            element_justification='center', vertical_alignment='center'
        ),
        sg.Column(image_column1, element_justification='center')
    ],
    [sg.Button('Exit')]
]


window = sg.Window('Guess Who', layout, location=(0,0), size=(1920,1080), element_justification='center')


while True:
    event, values = window.read()   
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break
    
    if event.startswith('char'):
        window[event].update(filename=black_PNG)

window.close()