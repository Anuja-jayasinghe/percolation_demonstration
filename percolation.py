# import modules
import sys
import percolation_fun.perc_functions


if __name__ == "__main__":
    # Check command line arguments for grid dimensions
    if len(sys.argv) == 1:
        #if dimensions not provided apply default dimensions 5x5
        rows, cols = 5, 5
    elif len(sys.argv) == 2 and "x" in sys.argv[1]:
        try:
            # extract dimensions from the argument by spitting the string 
            rows, cols = map(int, sys.argv[1].split("x"))
            if rows < 3 or cols < 3 or rows > 9 or cols > 9:
                # check if the dimensions are between the limits
                print("dimensions must be between 3x3 and 9x9")
                exit()
        except ValueError:
            # if the dimension are in a wrong format display error message
            print("Invalid dimensions provided. Please provide dimensions in the format 'NxM'.")
            sys.exit(1)
    else:
        print("Invalid command line arguments. Please provide dimensions in the format 'NxM'.")
        sys.exit(1)
        
    # Generate the grid
    grid = percolation_fun.perc_functions.generate_grid(rows, cols)
    
    # Display grid and check percolation status
    gridTable, percolationStatus = percolation_fun.perc_functions.display_and_check(grid)
    
    # Write grid table and percolation status to a text file
    percolation_fun.perc_functions.write_to_txt_file_and_terminal(gridTable, percolationStatus)
    
    # Generate HTML content
    htmlFileContent = percolation_fun.perc_functions.generate_html_content(gridTable,percolationStatus)
    
    # Write HTML content to a file
    percolation_fun.perc_functions.write_to_html_file(htmlFileContent)