class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, M, L, R):
            l_sub_arr = arr[L:M+1]
            r_sub_arr = arr[M+1:R+1]
            
            i, j, k = L, 0, 0

            # handle out of bounds
            while( j < len(l_sub_arr) and k < len(r_sub_arr)):
                if l_sub_arr[j] <= r_sub_arr[k]:
                    arr[i] = l_sub_arr[j]
                    j+=1
                else:
                    arr[i] = r_sub_arr[k]
                    k+=1
                i+=1
            # add rest of remaining l_sub_arr
            while j < len(l_sub_arr):
                arr[i] = l_sub_arr[j]
                j += 1
                i+=1
            while k < len(r_sub_arr):
                arr[i] = r_sub_arr[k]
                k+=1
                i+=1 

        def merge_sort(arr, l, r):
            if l == r:
                return arr
            m = (l + r) // 2
            merge_sort(arr, l, m)
            merge_sort(arr, m + 1, r)
            merge(arr, m, l, r)
            
        merge_sort(nums, 0, len(nums) - 1)
        return nums
