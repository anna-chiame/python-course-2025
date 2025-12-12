class HashTable:
    """
    Simple hash table implementation using separate chaining.

    Supports:
    - Insertion: table[key] = value
    - Access: table[key]
    - Membership test: key in table
    - Length: len(table)
    """

    def __init__(self, size=10):
        # Number of buckets
        self.size = size
        # Buckets: list of lists
        self.table = [[] for _ in range(self.size)]
        # Counter for number of stored keys
        self.count = 0

    def _hash(self, key):
        """
        Compute hash index for a key.
        """
        return hash(key) % self.size

    def __setitem__(self, key, value):
        """
        Insert or update a key-value pair.
        """
        index = self._hash(key)
        bucket = self.table[index]

        # Check if key already exists -> update
        for i in range(len(bucket)):
            k, v = bucket[i]
            if k == key:
                bucket[i] = (key, value)
                return

        # Key not found -> insert new
        bucket.append((key, value))
        self.count += 1

    def __getitem__(self, key):
        """
        Retrieve value by key.
        """
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key {key!r} not found")

    def __contains__(self, key):
        """
        Check if a key exists in the hash table.

        Used by: `key in table`
        """
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return True

        return False

    def __len__(self):
        """
        Return the number of keys stored in the hash table.

        Used by: `len(table)`
        """
        return self.count

    # --- Example usage  ---
ht = HashTable()

ht["a"] = 10
ht["b"] = 20
ht["a"] = 99

print("a" in ht)  # True
print("c" in ht)  # False
print(len(ht))  # 2
print(ht["a"])  # 99