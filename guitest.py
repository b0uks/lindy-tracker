import PySimpleGUI as sg

sg.theme('DarkAmber')    # Keep things interesting for your userskitchen ware

a = [(1, 'hello', 'active'), (2, 'bruh', 'active'), (3, 'gooooo', 'dead')]


def list_items():
    new_list = []
    for tuple in a:
        if tuple[2].lower() == 'active':
            new_list.append([sg.Text(f'id:{tuple[0]} {tuple[1]}', text_color='white', background_color='green', font='Courier 15')])
        else:
            new_list.append([sg.Text(tuple[1], text_color='white', background_color='red', font='Courier 15')])
    return new_list


col_layout = [[sg.Table(values=a, headings=['id','listing name', 'status'], auto_size_columns=True,
                        max_col_width=300, justification='center')]]

layout = [[sg.Column(col_layout, size=(800, 800), scrollable=True)],]

window = sg.Window('Table', no_titlebar=False, location=(350, 318), grab_anywhere=False).Layout(layout)


while True:                             # The Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    print(values.get('-IN-'))

    # for i in range(1000):  # this is your "work loop" that you want to monitor
    #     sg.one_line_progress_meter('One Line Meter Example', i + 1, 100000)


window.close
