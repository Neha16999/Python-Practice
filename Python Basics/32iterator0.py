nums=[5,8,9,7]

it=iter(nums)  #crating iterator it using iter fuction

print(it.__next__())

print(next(it))

#another way of iteration
for i in nums:
    print(i)
