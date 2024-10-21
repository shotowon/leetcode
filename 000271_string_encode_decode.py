from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0] + '\0'

        return '\0'.join(strs)

    def decode(self, s: str) -> List[str]:
        return [] if s == '' else [s[:len(s) - 1]] if s.endswith('\0') else s.split('\0')
