from database import DatabaseManager

class QuickFit:
    def __init__(self, db_name="quick_fit.db"):
        """Initialize Quick Fit with SQLite database support."""
        self.db = DatabaseManager(db_name)

    def add_block(self, size, block_id):
        """Add a memory block to the database."""
        return self.db.add_block(size, block_id)

    def allocate(self, process_id, size):
        """Allocate a block of memory to a process using the best-fit strategy."""
        block_id = self.db.allocate_block_best_fit(size)
        if block_id:
            return f"Process {process_id} allocated block {block_id} of size {size}."
        return f"No suitable blocks available for process {process_id} of size {size}."

    def free(self, size, block_id):
        """Free a memory block and add it back to the database."""
        return self.db.free_block(size, block_id)

    def display_memory(self):
        """Retrieve memory block data from the database."""
        return self.db.get_memory_blocks()

    def calculate_statistics(self):
        """Calculate total memory usage statistics."""
        return self.db.get_statistics()

    def defragment(self):
        """Defragment memory by combining adjacent free blocks."""
        return self.db.defragment_memory()

    def close(self):
        """Close the database connection."""
        self.db.close()
