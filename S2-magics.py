from typing import Any


class Student:
    def __init__(self, name: str, marks: [int | float]) -> None:
        self.name = name
        self.marks = marks

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        data = self.marks[self.index]

        self.index += 1
        if self.index >= len(self.marks):
            raise StopIteration

        return data

    def __getitem__(self, item) -> Any:
        print("item:", item)

        # if isinstance(item, str) and item.startswith('n'):
        #     return self.name[int(item.strip()[1:])]
        # elif isinstance(item, str) and item.startswith('m'):
        #     return self.marks[int(item.strip()[1:])]

        return self.marks[item]

    def __contains__(self, item) -> bool:
        return item in self.marks


ali = Student('Alireza Arvani', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# print(ali["n0"])
# print(ali["m0"])

# for i, v in enumerate(ali):
#     print(f"-- {ali[i]}")

# numbers = [10, 5, 3, 2, 34, 8, 3, 1]

print(60 in ali)
print(list(ali))
