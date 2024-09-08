from tkinter import Tk, Entry,Label,Button

# Create the main window
root = Tk()
root.title("Tkinter Example")

# Set the window size (width x height)
root.geometry("400x100")

# Create a label
label = Label(root, text="Enter Your Name:")
label.pack()


# Create an input box (Entry)
entry = Entry(root)
entry.pack()

# Create a button
button = Button(root, text="Greet Me")
button.pack()

# Run the application
root.mainloop()