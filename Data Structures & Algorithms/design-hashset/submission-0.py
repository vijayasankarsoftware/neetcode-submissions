class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(10)]

    def add(self, key: int) -> None:
        bucket_id = hash(key) % 10

        bucket = self.buckets[bucket_id]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket_id = hash(key) % 10

        bucket = self.buckets[bucket_id]

        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket.pop(i)
                break

    def contains(self, key: int) -> bool:
        bucket_id = hash(key) % 10

        bucket = self.buckets[bucket_id]

        for k in bucket:
            if k == key:
                return True

        return False