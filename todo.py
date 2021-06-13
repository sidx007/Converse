from functions import *
from libraries import *


# todo SELECT COUNT(*) AS RowCnt from try


def speak(command: str):
    engine = lib.pyttsx3.init()
    engine.say(command)
    print(command)
    engine.runAndWait()


def check_data():
    var = check()
    print(var)


def clear_all():
    conn = psycopg2.connect(host='localhost', dbname='try', user='postgres', password='markiselon888')
    cur = conn.cursor()
    query = '''drop table try;'''
    cur.execute(query)
    query1 = '''create table try(serial int,task text, status bool);'''
    cur.execute(query1)
    conn.commit()


def bool_fetch(status):
    conn = psycopg2.connect(host='localhost', dbname='try', user='postgres', password='markiselon888')
    cur = conn.cursor()
    query = '''SELECT * FROM TRY where status=%s'''
    cur.execute(query, status)
    print('done')
    conn.commit()


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


def update_data():
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


    button1 = lib.Button(text='save', bg=foreground, fg=background, height=1, width=10, font=4, relief=lib.RIDGE, command=lambda: put_data(1, 2, 3, 4, 5, task1_entry.get(), task2_entry.get(), task3_entry.get(), task4_entry.get(), task5_entry.get()))
    button1.grid(row=6, column=1)

    root.mainloop()


def to_do_items():
    root = lib.Tk()
    root.configure(background='Grey10')
    root.title('To Do')
    for i in range(5):
        getdata = get_data()
        tas = getdata[i]
        fin: str = tas[2]
        if fin == 'false':
            tkin = lib.Label(text='        ' + tas[1] + '       ', padx=30, pady=50, font='Tahoma', relief=lib.RIDGE, bg='grey10', fg='Red4')
            tkin.pack()
        else:
            pass
    root.mainloop()



if __name__ == '__main__':
    print(get_data())

