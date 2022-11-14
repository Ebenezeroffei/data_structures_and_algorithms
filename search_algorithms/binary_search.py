def binary_search(lst,ele):
    high,low, mid = len(lst) - 1,0,len(lst) // 2
    mid_ele = lst[mid]

    
    # One element
    if len(lst) == 1 and lst[0] == ele:
        return 1
        # Loop
    elif len(lst) > 1:
        while True:
            if lst[high] == ele or lst[low] == ele or mid_ele == ele:
                return 1
            # Go to the left
            elif mid_ele < ele:
                high, low = mid - 1, low + 1
                mid = low + ((high - low) // 2)
                mid_ele = lst[mid]
            else:
                high,low = high - 1 ,mid + 1
                mid = low + ((high - low) // 2)
                mid_ele = lst[mid]
    # Element not in list
    else:
        return -1
        
        