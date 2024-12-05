class delist(list):
    def __getitem__(self, index):
        if isinstance(index, slice):
            return delist(super().__getitem__(index))
        return super().__getitem__(index % len(self))
    
    def __contains__(self, key: object) -> bool:
        if isinstance(key, list):
            for i in range(len(self) - len(key) + 1):
                if self[i:i + len(key)] == key:
                    return True
            return False
        return super().__contains__(key)