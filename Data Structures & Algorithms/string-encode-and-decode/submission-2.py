class Solution:
    def encode(self, arr: List[str]) -> str:
        output = ""
        for item in arr:
            count = len(item)
            output += f"{count}#{item}"
        return output

    def decode(self, encoded_str: str) -> List[str]:
        curr_ind = 0
        res = []
        while curr_ind < len(encoded_str):

            # Get the char count of the item
            count = ""
            while encoded_str[curr_ind] != "#":
                count += encoded_str[curr_ind]
                curr_ind += 1
            count = int(count)

            # offseting # delimeter
            curr_ind += 1
            # Extract item
            item = ""
            for _ in range(count):
                item += encoded_str[curr_ind]
                curr_ind += 1

            res.append(item)
        return res
