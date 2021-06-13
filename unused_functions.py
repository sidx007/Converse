from functions import *
from libraries import *


# elif 'to do' in Listen:
#     data = get_data()
#     if len(data) == 0:
#         speak('Please add items in your to do list!')
#         todo()
#     else:
#         speak('The tasks left to do are.')
#         getdata = get_data()
#         tasks = getdata[0]
#         for i in range(5):
#             tas = getdata[i]
#             fin: str = tas[2]
#             if fin:
#                 pass
#             else:
#               speak(tas[1])
# elif 'update' in Listen:
#     speak('In update mode you can make changes in your to do list. Speak exit to quit.')
#     while True:
#         update_listen = listen()
#         if 'delete' and 'all' in update_listen:
#             clear_all()
#             speak('Done')
#         elif 'delete' in update_listen:
#             getdata1 = get_data()
#             print('serial    |   task')
#             for i in range(5):
#                 tas1 = getdata1[i]
#                 fin1: str = tas1[2]
#                 if fin1:
#                     pass
#                 else:
#                     print(str(tas1[0]) + '         |   ' + tas1[1])
#             speak('What is the serial number of the task')
#         elif 'quit' in update_listen:
#             speak('Ok, Done')
#             break
#         else:
#             pass
def speak(command: str):
    engine = lib.pyttsx3.init()
    engine.say(command)
    print(command)
    engine.runAndWait()


def put_data(one_serial, two_serial, three_serial, four_serial, five_serial, task1, task2, task3, task4, task5):
    conn = psycopg2.connect(host='localhost', dbname='try', user='postgres', password='markiselon888')
    cur = conn.cursor()
    query = '''INSERT INTO try(serial,task,status)VALUES(%s,%s,%s)'''
    cur.execute(query, (one_serial, task1, False))
    cur.execute(query, (two_serial, task2, False))
    cur.execute(query, (three_serial, task3, False))
    cur.execute(query, (four_serial, task4, False))
    cur.execute(query, (five_serial, task5, False))
    print('data inserted')
    conn.commit()


def watson():
    wf = wave.open(output_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def update_data(id):
    conn = psycopg2.connect(host='localhost', dbname='try', user='postgres', password='markiselon888')
    cur = conn.cursor()
    query = '''UPDATE try set status = true where serial = %s'''
    cur.execute(query, id)
    print('data inserted')
    conn.commit()


def get_data():
    conn = psycopg2.connect(host='localhost', dbname='try', user='postgres', password='markiselon888')
    cur = conn.cursor()
    query = '''select*from try '''
    cur.execute(query, )
    row = cur.fetchall()
    return row


def todo():
    root = lib.Tk()
    root.configure(background='grey10')
    background = 'black'
    foreground = "red4"
    root.title('ToDo')

    label('To Do List', 0, 1)
    label('task 1', 1, 0)
    label('task 2', 2, 0)
    label('task 3', 3, 0)
    label('task 4', 4, 0)
    label('task 5', 5, 0)

    task1_entry = lib.Entry(borderwidth=15, width=35, bg="white")
    task2_entry = lib.Entry(borderwidth=15, width=35, bg="white")
    task3_entry = lib.Entry(borderwidth=15, width=35, bg="white")
    task4_entry = lib.Entry(borderwidth=15, width=35, bg="white")
    task5_entry = lib.Entry(borderwidth=15, width=35, bg="white")

    task1_entry.grid(row=1, column=1)
    task2_entry.grid(row=2, column=1)
    task3_entry.grid(row=3, column=1)
    task4_entry.grid(row=4, column=1)
    task5_entry.grid(row=5, column=1)

    button1 = lib.Button(text='save', bg=foreground, fg=background, height=1, width=10, font=4, relief=lib.RIDGE,
                         command=lambda: put_data(1, 2, 3, 4, 5, task1_entry.get(), task2_entry.get(),
                                                  task3_entry.get(), task4_entry.get(), task5_entry.get()))
    button1.grid(row=6, column=1)

    root.mainloop()


update_data('1')
