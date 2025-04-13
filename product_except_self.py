n = len(nums)
        answer = [1] * n
        
        # Compute prefix products (left to right)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Compute suffix products (right to left) and multiply into answer
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

        