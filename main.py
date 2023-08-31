import PySimpleGUI as sg

sg.theme("black")


def page():
    layout = [
        [sg.Text("Message for client: ", size=(15, 1)), sg.Input(key="_client_", do_not_clear=True),
         sg.Button("Enter", key="pass", size=(23, 1))],
        [sg.Text("")],
        [sg.Button("Monday", key="monday", size=(23, 1)),
         sg.Button("Tuesday", key="tuesday", size=(23, 1)),
         sg.Button("Wednesday", key="wednesday", size=(23, 1))],
         [sg.Button("Thursday", key="thursday", size=(23, 1)),
         sg.Button("Friday", key="friday", size=(23, 1)),
         sg.Button("Saturday", key="saturday", size=(23, 1))],
        [sg.Text("")],
        [sg.Button("Add Client", key="add", size=(35, 1)),
         sg.Button("Delete Client", key="del", size=(35, 1))],
    ]
    window = sg.Window("Message Board", layout, size=(600, 200), modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()


def main():
    layout = [
        [sg.Text("Message for client: ", size=(15, 1)), sg.Input(key="_client_", do_not_clear=True),
         sg.Button("Enter", key="pass", size=(23, 1))],
        [sg.Text("")],
        [sg.Button("Monday", key="monday", size=(23, 1)),
         sg.Button("Tuesday", key="tuesday", size=(23, 1)),
         sg.Button("Wednesday", key="wednesday", size=(23, 1))],
         [sg.Button("Thursday", key="thursday", size=(23, 1)),
         sg.Button("Friday", key="friday", size=(23, 1)),
         sg.Button("Saturday", key="saturday", size=(23, 1))],
        [sg.Text("")],
        [sg.Button("Add Client", key="add", size=(35, 1)),
         sg.Button("Delete Client", key="del", size=(35, 1))],
    ]
    window = sg.Window("Client Message Board", layout, size=(600, 150), modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()


if __name__ == "__main__":
    main()
