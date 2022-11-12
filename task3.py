# three variables are initialized based on the total events in the triathlon that a participant execute.

# the variable swimming_duration is initialized to time used in swimming per minutes, and casted to an integer
swimming_duration = int(input(" enter the time (minutes) used in swimming.  "))

# the swimming_duration variable is printed
print(swimming_duration)


# the variable cycling_duration is initialized to time used in swimming per minutes, and casted to an integer
cycling_duration = int(input("enter time (minutes)  used in cycling.    "))

# the cycling_duration variable is printed
print(cycling_duration)

# the variable running_duration is initialized to time used in running per minutes, and casted to an integer
running_duration = int(input("enter the time used in running.   "))

# the running_duration variable is printed
print(running_duration)

# the sum of the total_time_to_complete_triathlon is set to the total duration of three events
total_time_to_complete_triathlon = swimming_duration + cycling_duration + running_duration

# comparing the total time with respect to each time interval for a given reward

# comparing total time to the interval of  qualifying time
if total_time_to_complete_triathlon <= 100:
    # print the corresponding award the provincial colour
    print("provincial colour")

# comparing the total time to the interval of  5 minutes of qualifying time
elif 100 < total_time_to_complete_triathlon <= 105:
    # print the corresponding award the provincial half colour
    print("provincial half colours")

# comparing the total time to the interval of 10 minutes of qualifying time
elif 105 < total_time_to_complete_triathlon <= 110:
    # print the corresponding award the provincial scroll
    print("provincial scroll")

# otherwise print no award
else:
    print("no award")

