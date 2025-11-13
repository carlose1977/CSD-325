"""
---

# CSD325-T301 - Week 10.2 Assignment: Tkinter and GUI Forms

---

**Professor**: John Woods<br>
**@Copyright**: BELLEVUE.edu<br>
**Modified By**: Carlos E. Escamilla<br>
**Email**: CEEscamilla@my365.BELLEVUE.edu<br>
**OS**: Windows 11 x64<br>
**Processor**: i9-13900<br>
**GPU**: NVIDIA GeForce RTX 3060<br>
**IDE**: DataSpell 2025.2<br>
**Interpreter**: Python 3.12<br>
**Libraries Managed by**: Miniforge3

---

**Version**:
- 1.0.0 - 2025.09.08 Week1: Programming Logic
- 1.0.1 - 2025.09.15 Week2: Documenting Debugging
- 1.0.2 - 2025.09.22 Week3: Brownfield Development
- 1.0.3 - 2025.09.29 Week4: CSV Read and Matplotlib
- 1.0.4 - 2025.10.06 Week5: Forest Fire Simulation 1
- 1.0.5 - 2025.10.13 Week6: Forest Fire Simulation 2
- 1.0.6 - 2025.10.20 Week7: Test Cases
- 1.0.7 - 2025.10.27 Week8: JSON Practice
- 1.0.8 - 2025.11.03 Week9: JSON and Application Programming Interfaces (APIs)
- 1.0.9 - 2025.11.10 Week10: Tkinter and GUI Forms

**Description**:
Read through the end of Section 2 in the tutorial and copy the code in Listing 2.2 Our Scrolling To-Do.
Paste into your Python program and save to your module-10 directory. Run the program, add a couple of tasks,
and take a screenshot of the output and paste into the Word document.

Using the other items in the reading list, complete the following modifications:
- ✅ Change the Title of the window to your last name-ToDo. Ex. Sampson-ToDo
- ✅ Change the color of the menu items, two (2) complementary colors work best.
- ✅ Currently, the user clicks the left mouse button to delete a task.. change that to the right mouse button.
- ✅ Provide instructions in the label on how to delete a task.
- ✅ We want the user to exit correctly, so add a menu item of File -> Exit. When clicked, Exit will end the program.
- ✅ Run the program, add a few tasks and take a screenshot. Paste that screenshot into your Word document.
- ✅ As the program is running, delete a task, then take a screenshot. Paste that screenshot into your Word document.

"""

# ==================================================
# GUI A To-Do List: 2.2 Scrolling and Deleting
# ==================================================
import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)

        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title("Escamilla-ToDo")
        self.geometry("300x400")

        # ADDED: Create menu bar with File -> Exit
        self.create_menu()

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")

        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")

        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # MODIFIED: Updated instructions to indicate right-click to delete
        # todo1 = tk.Label(self.tasks_frame, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)
        todo1 = tk.Label(self.tasks_frame, text="--- Add Items Here (Right-click to Delete) ---", bg="#20B2AA", fg="white", pady=10)

        # MODIFIED: Changed from Button-1 (left-click) to Button-3 (right-click)
        # todo1.bind("<Button-1>", self.remove_task)
        todo1.bind("<Button-3>", self.remove_task)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # MODIFIED: Changed color scheme to complementary colors (navy blue and light sea green)
        # self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]
        self.colour_schemes = [{"bg": "#20B2AA", "fg": "white"}, {"bg": "#FF6B6B", "fg": "white"}]

    # ADDED: Method to create menu bar
    def create_menu(self):
        """Create menu bar with File -> Exit option"""
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create File menu with complementary colors
        file_menu = tk.Menu(menubar, tearoff=0, bg="#20B2AA", fg="white", activebackground="#FF6B6B", activeforeground="white")
        menubar.add_cascade(label="File", menu=file_menu)

        # Add Exit option that closes the application
        file_menu.add_command(label="Exit", command=self.quit_application)

    # ADDED: Method to properly exit the application
    def quit_application(self):
        """Exit the application properly"""
        if msg.askyesno("Exit", "Are you sure you want to exit?"):
            self.quit()
            self.destroy()

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)

            self.set_task_colour(len(self.tasks), new_task)

            # MODIFIED: Changed from Button-1 (left-click) to Button-3 (right-click)
            # new_task.bind("<Button-1>", self.remove_task)
            new_task.bind("<Button-3>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)

        my_scheme_choice = self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.tasks_canvas.yview_scroll(move, "units")


if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()


