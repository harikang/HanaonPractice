import PySimpleGUI as sg

과일바구니 = []

layout = [[sg.Text('과일명을 입력해주세요.')],
          [sg.InputText()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('과일가게', layout)

event, values = window.read()
window.close()

text_input = values[0]
sg.popup('담은과일 :', text_input)
과일바구니.append(text_input)
sg.popup('과일바구니 :', 과일바구니)
