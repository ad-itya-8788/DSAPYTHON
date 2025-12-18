def jump_game(arr):
    maxReach = 0

    for i in range(len(arr)):
        if i > maxReach:
            return False

        maxReach = max(maxReach, i + arr[i])

    return True


# Test
arr1 = [2, 3, 1, 1, 4]
arr2 = [3, 2, 1, 0, 4]

print(jump_game(arr1))  # True
print(jump_game(arr2))  # False
