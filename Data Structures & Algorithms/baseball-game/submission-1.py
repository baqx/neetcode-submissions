class Solution:
    def calPoints(self, operations: List[str]) -> int:
        outputs = []
        for op in operations:
            try:
                outputs.append(int(op))
            except ValueError:
                if op == '+':
                    outputs.append(outputs[-1] + outputs[-2])
                elif op == "D":
                    outputs.append(outputs[-1] * 2)
                elif op == "C":
                    if outputs:
                        outputs.pop()
        return sum(outputs)
