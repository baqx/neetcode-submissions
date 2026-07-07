class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        i = 0
        

        while i < len(arr) - 1:
            j = len(arr) - 1
            
        
            max_on_right = arr[i + 1] 
            
            
            while j >= i + 1:
                if arr[j] > max_on_right:
                    max_on_right = arr[j]
                j -= 1
            
            
            arr[i] = max_on_right 
            i += 1
            
        
        arr[len(arr)-1] = -1
        
        return arr