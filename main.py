import PySimpleGUI as sg
import database_interface

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
        [sg.Text("Enter the day:", size=(20, 1)), sg.Input(key="day", do_not_clear=True)],
        [sg.Text("Enter the email:", size=(20, 1)), sg.Input(key="email", do_not_clear=True)],
        [sg.Text("")],
        [sg.Button("Enter", key="run_del", size=(100, 1))]
    ]
    window = sg.Window("Removing a Client", layout, size=(600, 150), modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "run_del":
            database_interface.delete(values["email"])


def add():
    layout = [
        [sg.Text("")],
        [sg.Text("Enter the day:", size=(20, 1)), sg.Input(key="day", do_not_clear=True)],
        [sg.Text("Enter the email:", size=(20, 1)), sg.Input(key="email", do_not_clear=True)],
        [sg.Text("")],
        [sg.Button("Enter", key="run_add", size=(100, 1))]
    ]
    window = sg.Window("Adding a Client", layout, size=(600, 150), modal=True)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "run_add":
            database_interface.insert(values["email"], values["day"])
    window.close()


def main(email, password):
    print(email, password)
    layout = [
        [sg.Text("Message for client: ", size=(15, 1)), sg.Multiline(size=(50, 3), key="_client_", do_not_clear=True),
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
                with open("monday.txt", "r") as file:
                    li = file.readlines()
                    rep = []
                    for x in li:
                        rep.append(x.replace("\n", ""))
                    for i in rep:
                        print(i)
            if values["tuesday"]:
                print("")
                print("SUBJECT: Tuesday Clients")
                print(values["_client_"])
                print("")
                with open("tuesday.txt", "r") as file:
                    li = file.readlines()
                    rep = []
                    for x in li:
                        rep.append(x.replace("\n", ""))
                    print(rep)
            if values["wednesday"]:
                print("")
                print("SUBJECT: Wednesday Clients")
                print(values["_client_"])
                print("")
                with open("wednesday.txt", "r") as file:
                    li = file.readlines()
                    rep = []
                    for x in li:
                        rep.append(x.replace("\n", ""))
                    for i in rep:
                        print(i)
            if values["thursday"]:
                print("")
                print("SUBJECT: Thursday Clients")
                print(values["_client_"])
                print("")
                with open("thursday.txt", "r") as file:
                    li = file.readlines()
                    rep = []
                    for x in li:
                        rep.append(x.replace("\n", ""))
                    for i in rep:
                        print(i)
            if values["friday"]:
                print("")
                print("SUBJECT: Friday Clients")
                print(values["_client_"])
                print("")
                with open("friday.txt", "r") as file:
                    li = file.readlines()
                    rep = []
                    for x in li:
                        rep.append(x.replace("\n", ""))
                    for i in rep:
                        print(i)
    window.close()


def login():
    layout = [
        [sg.Text("")],
        [sg.Text("EMAIL: ", size=(15, 1))],
        [sg.Input(key="_EMAIL_", do_not_clear=True)],
        [sg.Text("PASSWORD: ", size=(15, 1))],
        [sg.Input(key="_password_", do_not_clear=True)],
        [sg.Text("")],
        [sg.Button("Enter", size=(23, 1), key="pass")],
    ]
    window = sg.Window("EMAIL LOGIN", element_justification="c", text_justification="c",
                       size=(600, 200), modal=True).Layout(layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "pass":
            email = values["_EMAIL_"]
            password = values["_password_"]
            main(email, password)

    window.close()


if __name__ == "__main__":
    login()
