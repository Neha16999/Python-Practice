def sort(nums):
    for i in range(len(nums)-1):
        minpos=i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                nums[j], nums[minpos] = nums[minpos],nums[j]    


nums=[8,9,7,16,5,84,75,64,24,12,11,6]
sort(nums)

print(nums)