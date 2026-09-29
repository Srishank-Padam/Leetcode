class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mp = {}

        # Convert knowledge into a dictionary
        for key, value in knowledge:
            mp[key] = value

        result = []
        i = 0

        while i < len(s):

            if s[i] == '(':
                j = i + 1

                # Find closing bracket
                while s[j] != ')':
                    j += 1

                # Extract key
                key = s[i + 1:j]

                # Add value or ?
                if key in mp:
                    result.append(mp[key])
                else:
                    result.append('?')

                # Move past ')'
                i = j + 1

            else:
                result.append(s[i])
                i += 1

        return ''.join(result)