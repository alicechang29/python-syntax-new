def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits

    """

    # YOUR CODE HERE - if number is inside nums, if the num is greater than or equal to 15 and less than 30, print
    for num in nums:
        if num >= lowest and num <= highest:
            print(num)


in_range([10, 20, 30, 40, 50], 15, 30)
