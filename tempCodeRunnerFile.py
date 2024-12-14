
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Configure main frame to stretch dynamically
        main_frame.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=2)

                # Left Section
        left_frame = tk.Frame(main_fr