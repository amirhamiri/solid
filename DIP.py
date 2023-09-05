# Dependency Inversion Principle

from abc import ABC, abstractmethod



# low level class
# high level class
# abstract class


# low level class
class DiskStorage:
    def save(self, data):
        print(f"Saving data to disk: {data}")

# High level class
class DataStorer:
    def __init__(self):
        self.storage = FiskStorage()

    def store(self, data):
        self.storage.save(data)


data_storer = DataStorer()
data_storer.store("Disk storage data") 







# ----------------------------------------------------------------------------

# low level class
# high level class
# abstract class



# abstract class
class Storage(ABC):
    @abstractmethod
    def save(self, data):
        pass

# low level class
class DiskStorage(Storage):
    def save(self, data):
        print(f"Saving data to disk: {data}")

# low level class
class CloudStorage(Storage):
    def save(self, data):
        print(f"Saving data to cloud: {data}")



# high level class
class DataStorer:
    def __init__(self, storage: Storage):
        self.storage = storage

    def store(self, data):
        self.storage.save(data)


disk_storage = DiskStorage()

data_storer1 = DataStorer(disk_storage)
data_storer1.store("Disk storage data") 

