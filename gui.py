import tkinter as tk
from tkinter import messagebox, ttk
from quick_fit import QuickFit

class QuickFitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quick Fit Memory Management")
        self.root.geometry("800x600")

        self.quick_fit = QuickFit()

        # Title Section
        tk.Label(
            root,
            text="Quick Fit Memory Management",
            font=("Oswald", 37, "bold"),
            
            fg="#000000",
            justify="center"
        ).pack(fill=tk.X, pady=20)

        # Main Frame
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Configure main frame to stretch dynamically
        main_frame.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=2)

                # Left Section
        left_frame = tk.Frame(main_frame, bg="#ede8f5", relief="solid", bd=1)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Add Block Section
        add_block_frame = tk.Frame(left_frame, pady=5, padx=5, bg="#f0f8ff")
        add_block_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        tk.Label(add_block_frame, text="Add Memory Block", font=("Arial", 18, "bold"), fg="#000000", bg="#f0f8ff", anchor="center").pack(pady=5)

        tk.Label(add_block_frame, text="Block Size:", font=("Arial", 10, "bold"), bg="#f0f8ff", anchor="e").pack()
        self.add_size = tk.Entry(add_block_frame, width=10, justify="center")
        self.add_size.pack(pady=5)

        tk.Label(add_block_frame, text="Block ID:", font=("Arial", 10, "bold"), bg="#f0f8ff", anchor="e").pack()
        self.add_id = tk.Entry(add_block_frame, width=10, justify="center")
        self.add_id.pack(pady=5)

        tk.Button(add_block_frame, text="Add Block", command=self.add_block, bg="#f2ca73", fg="#000000", font=("Arial", 11, "bold")).pack(pady=5)

        # Allocate Memory Section
        allocate_frame = tk.Frame(left_frame, pady=5, padx=5, bg="#e6ffe6")
        allocate_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        tk.Label(allocate_frame, text="Allocate Memory", font=("Arial", 18, "bold"), fg="#000000", bg="#e6ffe6", anchor="center").pack(pady=5)

        tk.Label(allocate_frame, text="Process ID:", font=("Arial", 10, "bold"), bg="#e6ffe6", anchor="e").pack()
        self.alloc_process = tk.Entry(allocate_frame, width=10, justify="center")
        self.alloc_process.pack(pady=5)

        tk.Label(allocate_frame, text="Size:", font=("Arial", 10, "bold"), bg="#e6ffe6", anchor="e").pack()
        self.alloc_size = tk.Entry(allocate_frame, width=10, justify="center")
        self.alloc_size.pack(pady=5)

        tk.Button(allocate_frame, text="Allocate Memory", command=self.allocate_memory, bg="#bedb3d", fg="#000000", font=("Arial", 11, "bold")).pack(pady=5)

        # Free Memory Section
        free_frame = tk.Frame(left_frame, pady=5, padx=5, bg="#fff5e6")
        free_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        tk.Label(free_frame, text="Free Memory Block", font=("Arial", 18, "bold"), fg="#000000", bg="#fff5e6", anchor="center").pack(pady=5)

        tk.Label(free_frame, text="Block Size:", font=("Arial", 10, "bold"), bg="#fff5e6", anchor="e").pack()
        self.free_size = tk.Entry(free_frame, width=10, justify="center")
        self.free_size.pack(pady=5)

        tk.Label(free_frame, text="Block ID:", font=("Arial", 10, "bold"), bg="#fff5e6", anchor="e").pack()
        self.free_id = tk.Entry(free_frame, width=10, justify="center")
        self.free_id.pack(pady=5)

        tk.Button(free_frame, text="Free Block", command=self.free_memory, bg="#ac9321", fg="#000000", font=("Arial", 11, "bold")).pack(pady=5)

        # Right Section
        right_frame = tk.Frame(main_frame, bg="#fce4ec", relief="solid", bd=1)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Allow content in the right frame to resize
        right_frame.rowconfigure(0, weight=3)
        right_frame.rowconfigure(1, weight=1)
        right_frame.rowconfigure(2, weight=1)
        right_frame.columnconfigure(0, weight=1)

        # Display Memory Section
        display_frame = tk.Frame(right_frame, pady=5, padx=5, bg="#d6eaf8")
        display_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 10))  
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))  

        tk.Label(display_frame, text="Memory Status", font=("Arial", 18, "bold"), fg="#000000", bg="#d6eaf8").pack(pady=5)
        self.tree_memory = ttk.Treeview(display_frame, columns=("Size", "Blocks"), show="headings", height=6)
        self.tree_memory.heading("Size", text="Block Size (KB)")
        self.tree_memory.heading("Blocks", text="Available Blocks (IDs)")
        self.tree_memory.column("Size", width=100, anchor=tk.CENTER)
        self.tree_memory.column("Blocks", width=200, anchor=tk.CENTER)
        self.tree_memory.pack(fill=tk.BOTH, expand=True)

        # Memory Statistics Section
        stats_frame = tk.Frame(right_frame, pady=5, padx=5, bg="#eaf4e3")
        stats_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        tk.Label(stats_frame, text="Memory Statistics", font=("Arial", 18, "bold"), fg="#000000", bg="#eaf4e3").pack(pady=5)
        self.stats_label = tk.Label(stats_frame, text="Total Blocks: 0, Total Size: 0 KB", font=("Arial", 12, "bold"), fg="#000000", bg="#eaf4e3")
        self.stats_label.pack(fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(right_frame, pady=5, padx=5, bg="#e8f8f5")
        button_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        tk.Button(button_frame, text="Refresh Memory Status", command=self.display_memory, bg="#8c71f8", fg="#000000", font=("Arial", 11, "bold")).pack(anchor="center", pady=5)
        tk.Button(button_frame, text="Defragment Memory", command=self.defragment_memory, bg="#0ddad3", fg="#000000", font=("Arial", 11, "bold")).pack(anchor="center", pady=5)

    def add_block(self):
        size = self.add_size.get()
        block_id = self.add_id.get()
        if size.isdigit() and block_id:
            message = self.quick_fit.add_block(int(size), block_id)
            messagebox.showinfo("Add Block", message)
            self.display_memory()
        else:
            messagebox.showerror("Invalid Input", "Please enter valid size and block ID.")

    def allocate_memory(self):
        process_id = self.alloc_process.get()
        size = self.alloc_size.get()
        if size.isdigit() and process_id:
            message = self.quick_fit.allocate(process_id, int(size))
            messagebox.showinfo("Allocate Memory", message)
            self.display_memory()
        else:
            messagebox.showerror("Invalid Input", "Please enter valid process ID and size.")

    def free_memory(self):
        size = self.free_size.get()
        block_id = self.free_id.get()
        if size.isdigit() and block_id:
            message = self.quick_fit.free(int(size), block_id)
            messagebox.showinfo("Free Memory", message)
            self.display_memory()
        else:
            messagebox.showerror("Invalid Input", "Please enter valid size and block ID.")

    def display_memory(self):
        for row in self.tree_memory.get_children():
            self.tree_memory.delete(row)
        memory_status = self.quick_fit.display_memory()
        for size, blocks in memory_status.items():
            self.tree_memory.insert("", tk.END, values=(size, ", ".join(blocks)))

        total_blocks, total_sizes = self.quick_fit.calculate_statistics()
        self.stats_label.config(text=f"Total Blocks: {total_blocks}, Total Size: {total_sizes} KB")

    def defragment_memory(self):
        message = self.quick_fit.defragment()
        messagebox.showinfo("Defragment Memory", message)
        self.display_memory()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuickFitGUI(root)
    root.mainloop()
