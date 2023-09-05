import PySimpleGUI as sg

sg.theme("black")

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
saturday = []


def delete():
    layout = [
        [sg.Text("")],
        [sg.Text("Enter the day:", size=(20, 1)), sg.Input(key="_day_", do_not_clear=True)],
        [sg.Text("Enter the email:", size=(20, 1)), sg.Input(key="_number_", do_not_clear=True)],
        [sg.Text("")],
        [sg.Button("Enter", key="run_del", size=(100, 1))]
    ]
    window = sg.Window("Removing a Client", layout, size=(600, 150), modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "run_del":
            day = values["_day_"]
            if day == "monday":
                text = values["_number_"]
                with open("monday.txt", "r") as f:
                    li = f.readlines()
                    rep = []
                    for x in li:
                        rep.append(x.replace("\n", ""))
                    for i in rep:
                        if i == text:
                            rep.remove(i)
                            print(rep)
                with open("monday.txt", "w") as f:
                    for i in rep:
                        f.write(i + "\n")


def add():
    layout = [
        [sg.Text("")],
        [sg.Text("Enter the day:", size=(20, 1)), sg.Input(key="_day_", do_not_clear=True)],
        [sg.Text("Enter the email:", size=(20, 1)), sg.Input(key="_number_", do_not_clear=True)],
        [sg.Text("")],
        [sg.Button("Enter", key="run_add", size=(100, 1))]
    ]
    window = sg.Window("Adding a Client", layout, size=(600, 150), modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "run_add":
            day = values["_day_"]
            if day == "monday":
                text = values["_number_"]
                monday.append(text)
                with open("monday.txt", "a") as f:
                    for i in monday:
                        f.write(i)
            if day == "tuesday":
                text = values["_number_"]
                monday.append(text)
                with open("tuesday.txt", "a") as f:
                    for i in monday:
                        f.write(i)
            if day == "wednesday":
                text = values["_number_"]
                monday.append(text)
                with open("wednesday.txt", "a") as f:
                    for i in monday:
                        f.write(i)
            if day == "thursday":
                text = values["_number_"]
                monday.append(text)
                with open("thursday.txt", "a") as f:
                    for i in monday:
                        f.write(i)
            if day == "friday":
                text = values["_number_"]
                monday.append(text)
                with open("friday.txt", "a") as f:
                    for i in monday:
                        f.write(i)
    window.close()


def main():
    layout = [
        [sg.Text("Message for client: ", size=(15, 1)), sg.Input(key="_client_", do_not_clear=True),
         sg.Button("Enter", key="pass", size=(23, 1))],
        [sg.Text("")],
        [sg.Text("DAYS OF THE WEEK", size=(100, 1), justification='c')],
        [sg.Radio("Monday", "RADIO", key="monday", size=(11, 1)),
         sg.Radio("Tuesday", "RADIO", key="tuesday", size=(11, 1)),
         sg.Radio("Wednesday", "RADIO", key="wednesday", size=(11, 1)),
         sg.Radio("Thursday", "RADIO", key="thursday", size=(11, 1)),
         sg.Radio("Friday", "RADIO", key="friday", size=(11, 1))],
        [sg.Text("")],
        [sg.Text("ADD/REMOVE CLIENT", size=(100, 1), justification='c')],
        [sg.Button("Add Client", key="add", size=(35, 1)),
         sg.Button("Delete Client", key="del", size=(35, 1))],
    ]
    window = sg.Window("Client Message Board", layout, size=(600, 300), modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "add":
            add()
        if event == "del":
            delete()
        if event == "pass":
            if values["monday"]:
                print(values["_client_"])
    window.close()


if __name__ == "__main__":
    main()
