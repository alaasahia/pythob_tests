def get_even_nums(nums_list: list[int]) -> list:
    even_nums: list[int] = []
    for num in nums_list:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums
