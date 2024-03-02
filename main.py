import tkinter
from PIL import Image, ImageTk
from speedtest import Speedtest

# Setting the window size.
WINDOW_SIZE = '520x500'
# Creating the main window.
window = tkinter.Tk()
window.geometry(WINDOW_SIZE)
window.resizable(width = False, height = False)
# Setting up an external icon.
external_icon = tkinter.PhotoImage(file = 'images/External icon.png')
window.iconphoto(False, external_icon)
# Setting the window title.
window.title("Speed tester")
# Loading the background image.
path_to_background_image = 'images/Background.png'
image_of_background = tkinter.PhotoImage(file = path_to_background_image)
# Creating a label for the background image and packing it.
label_of_background = tkinter.Label(window, image = image_of_background)
label_of_background.pack(padx = 0, pady = 0)
# Creating and setting the download speed label.
label_of_download_speed = tkinter.Label(window,
                                        text = "Download speed: ",
                                        font = 35,
                                        background = '#0b21e3',
                                        foreground = '#f2ebeb')
label_of_download_speed.place(x = 15, y = 105)
# Creating and setting the upload speed label.
label_of_upload_speed = tkinter.Label(window,
                                      text = "Upload speed: ",
                                      font = 35,
                                      background = '#0b21e3',
                                      foreground = '#f2ebeb')
label_of_upload_speed.place(x = 15, y = 130)

# Function for measuring and displaying upload and download speed.
def start():
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download / (10 ** 6), 2)
    upload_speed = round(upload / (10 ** 6), 2)
    # Updating label texts.
    label_of_download_speed.config(text = f"Download speed: {str(download_speed)} MbPs")
    label_of_upload_speed.config(text = f"Upload speed: {str(upload_speed)} MbPs")
# Button to initiate measurement.
button_of_start = tkinter.Button(window,
                                 text = 'Start',
                                 font = 30,
                                 background = '#1ed6c4',
                                 activebackground = '#d61e1e',
                                 activeforeground = '#b9db0f',
                                 command = start)
# Button to initiate measurement.
button_of_start.place(x = 230, y = 250)
# Initiating the main event loop.
window.mainloop()
