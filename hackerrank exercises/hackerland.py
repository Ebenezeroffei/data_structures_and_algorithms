from math import ceil
from time import sleep

arr1 = [1,2,3,5,9]
# arr1 = [9,5,4,2,6,15,12]
k = 1

def hackerlandRadioTransmitters(x, k):
    modified_arr = range(min(x),max(x) + (k * 2 + 2))
    start = 0
    step = (k * 2) + 1
    end = start + step - 1
    mid_transmitter_index = start + int((end - start) / 2)
    mid_transmitter = modified_arr[mid_transmitter_index]
    transmitter_end = start - 1
    no_of_transmitters = 0

    while start <= max(x):
        if mid_transmitter in x:
            start = end + 1
            end = start + step - 1
            mid_transmitter_index = start + int((end - start) / 2)
            mid_transmitter = modified_arr[mid_transmitter_index]
            transmitter_end =  start - 1
            no_of_transmitters += 1
        else:
            if mid_transmitter_index - 1 > transmitter_end:
                start -= 1
                end -= 1
                mid_transmitter_index -= 1
            else:
                start += 1
                end += 1
                mid_transmitter_index += 1
                transmitter_end += 1

            mid_transmitter = modified_arr[mid_transmitter_index]
    return no_of_transmitters

    # Write your code here

hackerlandRadioTransmitters(arr1,k)