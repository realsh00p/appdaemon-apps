from pynput import keyboard

from button.timer import Timer

class Button:

    def __init__(self):
        self.count = 0
        self.timer = Timer(0.25, self.__finished)

        self.holding = False
        self.pressed = False

        self.listener = keyboard.Listener(on_press=self.__on_press, on_release=self.__on_release)
        self.listener.start()

    def __get_key(self, key):
        try:
            return key.char
        except:
            return key.name

    def __on_press(self, key):
        if self.__get_key(key) == 'ctrl':
            if self.holding:
                self.count = 0
                self.holding = False
            self.pressed = True

            self.timer.reset(start=True)
            self.count = self.count + 1
            print("ctrl pressed, count: " + str(self.count))

    def __on_release(self, key):
        if self.__get_key(key) == 'ctrl':
            self.pressed = False

    def __finished(self):
        if self.pressed:
            self.holding = True
        else:
            self.holding = False

        if self.holding:
            print("hold, count: " + str(self.count))
            self.timer.reset(start=True)
        else:
            print("finished, count: " + str(self.count))
            self.count = 0


def main():
    t1 = Button()
    t1.listener.join()

if __name__ == "__main__":
    main()
