from services.services import Services


class Main:
    def __init__(self):
        self.app = Services()

    def mainloop(self):
        self.app.mainloop()


if __name__ == "__main__":
    Main().mainloop()