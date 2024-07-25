import FreeSimpleGUI as sg

basket = []
# All the stuff inside your window.
layout = [
            # [sg.Text('')],
            [sg.Text('과일명을 입력해주세요.'), sg.InputText()],
            # [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Submit(),sg.Cancel()]
]


# Create the Window
window = sg.Window('과일가게', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED : #or event == 'Cancel': # if user closes window or clicks cancel
        break
    text_input = values[0]
    basket.append(text_input)
    print('담은 과일은 ', text_input)
    print('과일바구니에는 ', basket,'가 있습니다.')

window.close()

