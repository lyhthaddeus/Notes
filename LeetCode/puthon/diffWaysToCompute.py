class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}

        def calculate(expression):
            if expression in memo:
                return memo[expression]

            results = []

            for i in range(len(expression)):
                char = expression[i]
                if char in "+-*":
                    left = calculate(expression[:i])
                    right = calculate(expression[i + 1:])
                    
                    for l in left:
                        for r in right:
                            if char == "+":
                                results.append(l + r)
                            if char == "-":
                                results.append(l - r)
                            if char == "*":
                                results.append(l * r)

            if not results:
                results.append(int(expression))

            memo[expression] = results

            return results


        return calculate(expression)
