import smtplib
from tkinter import *
from threading import Thread

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x600')
        self.title('Mail services')
        # main canvas
        self.root = Canvas(self)
        self.root.place(relx=0, rely=0, relwidth=1, relheight=1)

        # to frame
        self.to_frame = Frame(self.root)
        self.to_frame.place(relx=.2, rely=.1, relwidth=.5)
        # to label and input box
        self.to_label = Label(self.to_frame, text='To:')
        self.to_label.grid(row=0, column=0)
        self.to = Entry(self.to_frame)
        self.to.grid(column=1, row=0, ipadx=76)

        #log in and pass
        self.log_pass_frame = Frame(self, bg='white')
        self.log_pass_frame.place(relx=.2, rely=0, relwidth=.5)

        Label(self.log_pass_frame, text='Log in:').grid(row=0, column=0, ipadx=20, ipady=0)
        self.log = Entry(self.log_pass_frame)
        self.log.grid(column=1, row=0, ipadx=46)
        Label(self.log_pass_frame, text='Password:').grid(column=0, row=1, ipadx=12)
        self.pas = Entry(self.log_pass_frame)
        self.pas.grid(row=1, column=1, ipadx=46)

        # message box
        self.message_box = Frame(self.root)
        self.message_box.place(relx=.2, rely=.2,  relwidth=.5, relheight=.4)
        self.subject = Text(self.message_box, bg='white', height=2)

        self.subject.grid(row=3, column=0)
        self.subject.insert(INSERT, 'Subject:')
        self.body = Text(self.message_box)
        self.body.place(rely=.1, relwidth=1, relheight=1)

        # response frame
        self.res_frame = Frame(self.root, bg='white')
        self.res_frame.place(relx=.2, rely=.7, relwidth=.5, relheight=.2)
        # response widget
        self.response = Text(self.res_frame, bd=0)
        self.response.place(relx=0, rely=.2)
        # response label
        self.res_label = Label(self.res_frame, text='Response:')
        self.res_label.place(relx=0, rely=0)


        #  button
        Button(self.root, text='Send', command=self.call_send_email).place(relx=.3, rely=.9, relwidth=.2,)

    def call_send_email(self):
        to = self.to.get()
        log = self.log.get()
        pas = self.pas.get()
        msg = str(self.subject.get('1.0', END) +'\n'+self.body.get('1.0', END))
        print(msg)
        thread1 = Thread(target=self.send_email, args=(to, msg, log, pas,))
        thread1.start()


    def send_email(self, to, log, pas, msg):
        to = to
        msg = msg
        log = log
        pas = pas
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            self.response.insert(INSERT, 'Log in ......')
            self.response.tag_add('color', '1.0', '2.3')
            self.response.tag_config('color', background='LightGreen', foreground='black')
            server.login(log, pas)
            self.response.insert(INSERT, 'Sending email ......')
            self.response.tag_add('color', '1.0', '2.0')
            self.response.tag_config('color', background='LightGreen', foreground='black')
            server.sendmail(log, to, msg)
            self.response.insert(INSERT, 'Send email ......')
            self.response.tag_add('color', '1.0', '2.3')
            self.response.tag_config('color', background='LightGreen', foreground='black')
            server.quit()
        except Exception as e:
            print(e)
            self.response.insert(INSERT, '\n'+str(e))
            self.response.tag_add('error', '1.0', '3.0')
            self.response.tag_config('error', background='Red', foreground='black')


if __name__ == '__main__':
    app = App()
    app.mainloop()



