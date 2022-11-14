"""
    Problem: Find the region with the biggest number of cells.
"""

"""
    Edge Cases:
    1. A single row  has two or more filled cells not connected to each other
    2. An adjacent filled cell is connected to a filled cell on top of it
"""

"""
    Solution 
    1. Create a variable max_cell_region which will contain the number of cells in the biggest region
    2. Create a variable called region_cell_count which will store the number of cells in a region
    3. Create a variable called discovered_region_cells which is a list which stores the position of the ells in the region
    4. Loop through the row and column of the matrix
    5. If we discover a region we add the position of the first cell of the region to the discovered_region_cells and loop through it 
    6. As we are looping through the dicovered_region_cells we will look for neighbours which are filled cells
    7. When we discover them we will add them to the discovered_region_cells and continue looping over the discovere_region_cells till we are done with it.
    8. We will be increasing the region_cell_count as we discover new filled cells in the region
    9. After looping through the discovered_region_cells we will compare the region_cell_count to the max_cell_region to get the maximum number which will be assigned to max_cels
"""

def connectedCells(matrix):
    max_cell_region = region_cell_count = 0
    discovered_region_cells = []

    # Go through every element
    for row_index in range(len(matrix)):
        for col_index, col in enumerate(matrix[row_index]):
            # Found a filled cell
            if col == 1:
                # Append its location 
                discovered_region_cells.append((row_index,col_index))
                # Go through the discovered region and find its neigbours 
                current_discovered_region_cell_index = 0

                while current_discovered_region_cell_index < len(discovered_region_cells):
                    region_cell_count += 1 # Increase
                    # Location of the cell
                    current_discovered_region_cell_location_row, current_discovered_region_cell_location_col = discovered_region_cells[current_discovered_region_cell_index]
                    # Mark the cell as visited
                    matrix[current_discovered_region_cell_location_row][current_discovered_region_cell_location_col] = 0

                    # Go throug it's neighbours
                    for r in range(current_discovered_region_cell_location_row - 1,current_discovered_region_cell_location_row + 2):
                        for c in range(current_discovered_region_cell_location_col - 1, current_discovered_region_cell_location_col + 2):

                            # Check if the element index exists
                            try:
                                # Invalid element index
                                if r < 0 or c < 0: raise IndexError
                                # Found a filled cell
                                if matrix[r][c] == 1:
                                    # Filled cell index hasn't been registered
                                    if (r,c) not in discovered_region_cells:
                                        discovered_region_cells.append((r,c))
                            except IndexError:
                                pass 
                    # Go to the next filled index in the region
                    current_discovered_region_cell_index += 1
                # Check if region has the highest calls
                max_cell_region =  max(region_cell_count,max_cell_region)
                # Reset values
                discovered_region_cells.clear()
                region_cell_count = 0

    return max_cell_region



# Test Cases
test = [
    {
        'input':{
            'matrix':[
                [1, 1, 1, 0], 
                [0, 1, 1, 0], 
                [0, 0, 1, 0], 
                [1, 0, 0, 0]
            ]
        },
        'output': 6,
    },
    {
        'input':{
            'matrix':[
                [1, 1, 1, 0,0,1,1], 
                [0, 1, 1, 0,1,0,1], 
                [0, 0, 1, 0,0,1,1], 
                [1, 0, 0, 0,1,1,1],
            ]
        },
        'output': 9,
    }
]


if __name__ == "__main__":
    for index,ele in enumerate(test):
        test_case_output = test[index]['output']
        output = connectedCells(ele['input']['matrix'])
        print(
            f"Test Case {index + 1} Passed"
            if test_case_output == output
            else f"Test Case {index + 1} Failed"
        )