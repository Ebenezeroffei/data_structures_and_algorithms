def depth_first_search(matrix):
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