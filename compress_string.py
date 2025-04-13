class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0  # Pointer to write the compressed result
        read = 0    # Pointer to read the original array
        
        while read < n:
            char = chars[read]
            count = 1
            
            # Count consecutive occurrences of `char`
            while read + 1 < n and chars[read + 1] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
            read += 1
        
        return write