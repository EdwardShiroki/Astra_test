from pprint import pprint


def longest_increasing_streak(nums: list[int]) -> dict:
    """Return the first longest contiguous strictly increasing streak."""
    if len(nums) < 2:
        return {"length": 0, "streak": []}

    best_start = 0
    best_length = 0
    current_start = 0
    current_length = 1

    for index in range(1, len(nums)):
        if nums[index] > nums[index - 1]:
            current_length += 1
        else:
            if current_length > best_length and current_length >= 2:
                best_start = current_start
                best_length = current_length

            current_start = index
            current_length = 1

    if current_length > best_length and current_length >= 2:
        best_start = current_start
        best_length = current_length

    if best_length == 0:
        return {"length": 0, "streak": []}

    return {
        "length": best_length,
        "streak": nums[best_start:best_start + best_length],
    }


if __name__ == "__main__":
    example_nums = [1, 3, 2, 5, 8, 4, 7]
    equal_best_nums = [1, 2, 0, 3]
    decreasing_nums = [9, 7, 7, 2]

    assert longest_increasing_streak(example_nums) == {
        "length": 3,
        "streak": [2, 5, 8],
    }

    assert longest_increasing_streak(equal_best_nums) == {
        "length": 2,
        "streak": [1, 2],
    }

    assert longest_increasing_streak(decreasing_nums) == {
        "length": 0,
        "streak": [],
    }

    print("Example numbers:")
    pprint(longest_increasing_streak(example_nums), sort_dicts=False)

    print("\nEqual best streaks, first returned:")
    pprint(longest_increasing_streak(equal_best_nums), sort_dicts=False)

    print("\nNo increasing streak:")
    pprint(longest_increasing_streak(decreasing_nums), sort_dicts=False)
