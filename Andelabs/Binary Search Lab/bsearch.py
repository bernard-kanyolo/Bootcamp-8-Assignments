class BinarySearch(list):

    def __init__(self, a, b):
        super(BinarySearch, self).__init__(range(b, a * b + b, b))
        # self = range(b, a * b + b, b)
        self.length = a

    def search(self, value):
        result = {"count": 0, "index": -1}

        start = 0
        end = self.length - 1

        while start <= end:
            """iterate until start >= end"""
            result["count"] = result.get("count") + 1

            middle = (start + end) / 2
            if value == self[middle]:
                result["index"] = middle
                break
            elif value > self[middle]:
                start = middle + 1
            else:  # value < self[middle]
                end = middle - 1

        return result

"""one_to_twenty = BinarySearch(20, 1)
two_to_forty = BinarySearch(20, 2)
ten_to_thousand = BinarySearch(100, 10)

print {index: num for index, num in enumerate(two_to_forty)}

print two_to_forty.search(40)
print ten_to_thousand
print ten_to_thousand.search(880)
"""