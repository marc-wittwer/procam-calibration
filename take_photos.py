import tkinter as tk
import cv2
import os
from time import sleep


def main():
    window = tk.Tk()
    MainWindow(window)
    window.mainloop()


class MainWindow:
    current_capture_number = 0

    def __init__(self, window):

        print('Load pattern images.')
        self.window = window
        self.cap = cv2.VideoCapture(0)
        self.pattern_images = []
        for i in range(0, 44):
            image_number = ('0' + str(i))[-2:]
            image_name = 'graycode_pattern/pattern_' + image_number + '.png'
            self.pattern_images.append(tk.PhotoImage(file=image_name))
        self.current_pattern_number = 0

        w, h = window.winfo_screenwidth(), window.winfo_screenheight()
        print('Screen width x height: ', w, h)

        self.canvas = tk.Canvas(window, width=w, height=h)
        self.canvas.pack()

        self.image_on_screen = self.canvas.create_image((0, 0), image=self.pattern_images[self.current_pattern_number],
                                                        anchor=tk.NW)
        window.bind("<Key>", self.handle_keypress)

    def take_photo(self):
        ret, frame = self.cap.read()
        cv2.imwrite(
            'capture_' + str(self.current_capture_number) + '/graycode_' + ('0' + str(self.current_pattern_number))[
                                                                           -2:] + '.png', frame)

    def exit_application(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.window.destroy()

    def handle_keypress(self, event):
        if event.char == 'q':
            self.exit_application()

        if event.char == 's':
            folder_name = 'capture_' + str(self.current_capture_number)
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            self.current_pattern_number = 0
            for i in range(len(self.pattern_images)):
                print('Pattern', self.current_pattern_number)
                print('Update pattern')
                self.canvas.itemconfig(self.image_on_screen, image=self.pattern_images[self.current_pattern_number])
                self.window.update()
                print('Take photo')
                sleep(2)
                self.take_photo()
                sleep(2)

                self.current_pattern_number += 1

        if event.char == 'a':
            # Take single photo
            self.canvas.itemconfig(self.image_on_screen, image=self.pattern_images[self.current_pattern_number])
            self.take_photo()
            self.current_pattern_number += 1

        if event.char == 'n':
            self.current_capture_number += 1
            print('Ready to capture next pose capture', self.current_capture_number)

        if event.char == 'r':
            w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
            print('Screen width x height: ', w, h)


if __name__ == '__main__':
    main()
