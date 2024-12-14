import sqlite3

class DatabaseManager:
    def __init__(self, db_name="quick_fit.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self._connect()
        self.create_tables()

    def _connect(self):
        """Establish a connection to the SQLite database."""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def _disconnect(self):
        """Close the connection to the SQLite database."""
        if self.connection:
            self.connection.close()

    def create_tables(self):
        """Create tables for memory management."""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS memory_blocks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                size INTEGER NOT NULL,
                block_id TEXT NOT NULL UNIQUE
            )
            """
        )
        self.connection.commit()

    def add_block(self, size, block_id):
        """Add a memory block to the database."""
        try:
            self.cursor.execute(
                "INSERT INTO memory_blocks (size, block_id) VALUES (?, ?)",
                (size, block_id)
            )
            self.connection.commit()
            return f"Block {block_id} of size {size} added."
        except sqlite3.IntegrityError:
            return f"Block ID {block_id} already exists. Cannot add."

    def allocate_block_best_fit(self, size):
        """Allocate a block using the best-fit strategy."""
        self.cursor.execute(
            """
            SELECT block_id, size FROM memory_blocks WHERE size >= ? 
            ORDER BY size ASC LIMIT 1
            """,
            (size,)
        )
        result = self.cursor.fetchone()
        if result:
            block_id = result[0]
            self.cursor.execute(
                "DELETE FROM memory_blocks WHERE block_id = ?", (block_id,)
            )
            self.connection.commit()
            return block_id
        return None

    def free_block(self, size, block_id):
        """Free a block and add it back to the database."""
        try:
            self.cursor.execute(
                "INSERT INTO memory_blocks (size, block_id) VALUES (?, ?)",
                (size, block_id)
            )
            self.connection.commit()
            return f"Block {block_id} of size {size} freed and added back to the list."
        except sqlite3.IntegrityError:
            return f"Block {block_id} is already free."

    def get_memory_blocks(self):
        """Retrieve the current memory blocks grouped by size."""
        self.cursor.execute(
            """
            SELECT size, GROUP_CONCAT(block_id) as blocks 
            FROM memory_blocks GROUP BY size ORDER BY size ASC
            """
        )
        return {row[0]: row[1].split(",") if row[1] else [] for row in self.cursor.fetchall()}

    def get_statistics(self):
        """Retrieve statistics about the memory blocks."""
        self.cursor.execute("SELECT COUNT(*), SUM(size) FROM memory_blocks")
        total_blocks, total_size = self.cursor.fetchone()
        return total_blocks, total_size or 0

    def defragment_memory(self):
        """Combine adjacent free blocks of the same size."""
        self.cursor.execute(
            """
            SELECT size, COUNT(*) FROM memory_blocks GROUP BY size HAVING COUNT(*) > 1
            """
        )
        blocks_to_combine = self.cursor.fetchall()
        combined_count = 0

        for size, count in blocks_to_combine:
            new_size = size * count
            new_block_id = f"defragmented-{size}-{count}"
            self.cursor.execute(
                "DELETE FROM memory_blocks WHERE size = ?", (size,)
            )
            self.cursor.execute(
                "INSERT INTO memory_blocks (size, block_id) VALUES (?, ?)",
                (new_size, new_block_id)
            )
            combined_count += 1

        self.connection.commit()
        return f"Defragmentation complete. Combined {combined_count} blocks."

    def close(self):
        """Ensure the connection is closed when the object is deleted."""
        self._disconnect()

    def __del__(self):
        self._disconnect()
