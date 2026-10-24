class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == '+':
                value1 = record.pop()
                value2 = record.pop()
                record.append(value2)
                record.append(value1)
                record.append(value1 + value2)
            elif operations[i] == 'D':
                value = record.pop()
                record.append(value)
                record.append(value * 2)
            elif operations[i] == 'C':
                record.pop()
            else:
                record.append(int(operations[i]))
        return sum(record)