from threading import Timer

import data


# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.
    #DONE
# Part 2
   # The function for Part 2 should be within the class in data.py.
   #DONE
# Part 3
def time_add(time1,time2):
    total_time = data.Time(0,0,0)
    total_time.second += time1.second + time2.second
    if total_time.second >=60:
        total_time.minute+=1
        total_time.second -= 60
    else:
        total_time.second = time1.second + time2.second
    total_time.minute += time1.minute +time2.minute
    if total_time.minute >=60:
        total_time.hour+=1
        total_time.minute -= 60
    else:
        total_time.minute = time1.minute + time2.minute
  #  mod_sec = seconds % 60
   # mod_min = minutes % 60
    total_time.hour += (time1.hour+time2.hour)
    return total_time
# Part 4
def is_descending(input_list:list[float])->bool:
    for i in range(1, len(input_list)):
        if input_list[i] >= input_list[i - 1]:
            return False
    return True

# Part 5
def largest_between(nums, lower, upper):
    # Check if the range is empty or out of bounds
    if lower > upper or not (0 <= lower < len(nums)) or not (0 <= upper < len(nums)):
        return None

    lower = max(0, lower)
    upper = min(len(nums) - 1, upper)


    max_index = lower
    for i in range(lower, upper + 1):
        if nums[i] > nums[max_index]:
            max_index = i

    return max_index
# Part 6
def furthest_from_origin(points):
    # Return None if the list is empty
    if not points:
        return None

    max_index = 0
    max_distance = points[0].x**2 + points[0].y**2

    for i in range(1, len(points)):
        distance = points[i].x**2 + points[i].y**2
        if distance > max_distance:
            max_distance = distance
            max_index = i

    return max_index
