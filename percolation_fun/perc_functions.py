# import modules

import random
import datetime
from prettytable import PrettyTable

# Define the functions 
def generate_grid(rows, cols):
    "Function to generate a 2D grid with random values"
    grid = []
    # declaring variables to adjust the possibility of the random empty and filled cells
    selections = [0, 1]
    probabilities = [0.3, 0.7]# 30% chance of "0" and 70% chance of "1"
    for _ in range(rows):
        row = []
        for _ in range(cols):
            # Randomly choose between None and a random two-digit integer
            selectedValue = random.choices(selections, probabilities)[0]
            if selectedValue == 1:
                row.append(random.randint(10, 99)) # random selection is equal to 1 fill that cell with two digit integer
            else:
                row.append(None)
        # Insert created row to the grid
        grid.append(row)
    return grid

def display_and_check(grid):
    "Function to display grid and check percolation status"
    table = PrettyTable() # Create grid using PrettyTable 
    percolationStatus = []
    co = []
    for col in range(len(grid[0])):
        column = []
        for row in range(len(grid)):
            if grid[row][col] == None:
                grid[row][col]= " "
                column.append(grid[row][col])
                continue
            column.append(grid[row][col])
        if " " not in column:
            #check percolation by matching the lengths of the grid and column
            percolation = "OK"
        else:
            percolation = "NO"
        # Append percolation status to the end of the column
        column.append(percolation)
        # Add the column to the prettytable with the header
        table.add_column(f"C {col+1}", column)
        # Add the percolation status of the coloum to the list
        percolationStatus.append(percolation)
        co.append(column)
    return table, percolationStatus



def write_to_txt_file_and_terminal(gridTable, percolationStatus):
    "Function to write grid table and percolation status to a text file"
    now = datetime.datetime.now() 
    # Create the file name as year_month_day_4digit random number.txt
    fileName = f"{now.year}_{now.month:02d}_{now.day:02d}_{random.randint(1000, 9999)}.txt"
    # creating a txt file
    with open(fileName, "w") as file:
        # write table and percolation status to the text file
        file.write("Grid table and percolation status:\n\n")
        file.write(str(gridTable) + "\n\n")
        for i, status in enumerate(percolationStatus):
            statusMessage = "Possible" if status == "OK" else "Not possible"
            file.write(f"Percolation for Column {i+1} is: {statusMessage}\n")
    # Print percolation table and percolation status to the terminal
    print("Grid table and percolation status:")
    print(gridTable)
    for i, status in enumerate(percolationStatus):
        statusMessage = "Possible" if status == "OK" else "Not possible"
        print(f"Percolation for Column {i+1} is: {statusMessage}")
    print("\n")
    print(f"Text file created and saved as: {fileName}") # print the file name the of the text file generated
        
def generate_html_content(table, percolationStatus):
    "Function to generate HTML content for displaying grid and percolation status in a HTML file"
    htmlContent = f"""
    <html>
    <head>
        <title>Percolation Simulation</title>
        <style> 
            body {{
                background-color:black;
                background-image: linear-gradient(225deg, #FF3CAC 0%, #784BA0 50%, #2B86C5 100%);
                background-repeat: no-repeat;
                background-size: cover;
                background-attachment: fixed;
                background-position: center;
                color: white;
                font-family:'Times New Roman', Times, serif;
            }}

            h1{{
                text-align: center;
                font-size: 60px;     
            }}
            h2 {{
                font-size: 2em;
                position: fixed;
                top: 4em;
            }}
            ul {{
                list-style-type: none;
                font-size: 16px;
                position: fixed;
                top: 12em;
                padding-left: 9px;
                border: #551C7D solid;
                border-radius: 2em;
                padding: 25px;
                backdrop-filter: blur(30px);
            }}
            table {{
                background:transparent;
                border-radius: 1em;
                outline: 1px solid;
                outline-offset: -1px;
                overflow: hidden;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(15.2px);
                -webkit-backdrop-filter: blur(5.2px);
                
                border-collapse: collapse;
                width: 50%;
                height:50%;
                margin: auto;
            }}
            th, td {{
                border: 1px solid rgb(255, 255, 255);
                border-radius: 4px;
                padding: 8px;
                height: 40px;
                text-align: center;
            }}
            th {{
                background-color: #e17889;
                color:black;
            }}
           .highlight-no {{
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
                -webkit-backdrop-filter: blur(5.2px);
            }}
            .highlight-animation {{
                animation: highlight-colors 2s ease-in-out infinite;
            }}
            @keyframes highlight-colors {{
                0% {{
                    color: black;
                    background-color: palevioletred;
                }}
                            
                                
                100% {{
                        color: white;
                        webkit-backdrop-filter: blur(5.2px);
                }}
            }}
            @supports (background-image: url('https://source.unsplash.com/PvgqqicSLvA/')) {{
                body {{
                    background-image: url('https://source.unsplash.com/PvgqqicSLvA/');
                }}
                th{{
                    background-color: #E178C5;
                }}
            }}
        </style>
    </head>
    <body>
        <h1>Percolation Grid</h1>
        <table>
            <thead>
                <tr>
    """


    for i in range(len(table.field_names)):
        # Insert table headers to the html 
        htmlContent += f"<th>C {i + 1}</th>"
    htmlContent += "</tr></thead><tbody>"


    for row in range(len(table._rows)):
        # Insert table data to the html table
        htmlContent += "<tr>"
        for col in range(len(table._field_names)):
            cell_content = table._rows[row][col]
            if isinstance(cell_content, (int, float)) or cell_content == "OK":
                htmlContent += f"<td>{cell_content}</td>"
            else:
                # If cell is empty or contain string "NO" add class "highlight-no"
                htmlContent += f"<td class='highlight-no'>{cell_content}</td>"
        htmlContent += "</tr>"

    htmlContent += """
        </tbody>
        </table>
        <h2>Percolation Status</h2>
        <ul>
    """
    for i, status in enumerate(percolationStatus):
        # Insert percolation status of each row to a unordered list
        status_message = "Possible" if status == "OK" else "Not possible"
        htmlContent += f"<li>C {i + 1} :- Percolation {status_message}</li>"
    htmlContent += """
        </ul>
                <script>
            const rows = document.querySelectorAll('tbody tr');
            const columnsCount = document.querySelectorAll('tbody tr:first-child td').length;
            let rowIndex = 0;
            let columnIndex = 0;
        
            function animateCells() {
                let foundHighlightNo = false;
        
                // Iterate through each column first
                for (let c = 0; c < columnsCount; c++) {
                    foundHighlightNo = false;
                    // Iterate through each row in the column
                    for (let r = 0; r < rows.length; r++) {
                        const currentCell = rows[r].cells[c];
                        // Check if cell has highlight-no class
                        if (currentCell.classList.contains('highlight-no')) {
                            foundHighlightNo = true;
                        }
                        // If highlight-no found, apply it to rest of the cells in the column
                        if (foundHighlightNo && !currentCell.classList.contains('highlight-no')) {
                            currentCell.classList.add('highlight-no');
                        }
                    }
                }
        
                // Once highlighting is done, proceed with animation
                const currentRow = rows[rowIndex];
                const currentCell = currentRow.cells[columnIndex];
                if (!currentCell.classList.contains('highlight-no')) {
                    currentCell.classList.add('highlight-animation');
                }
        
                rowIndex++;
                if (rowIndex >= rows.length) {
                    rowIndex = 0;
                    columnIndex++;
                    if (columnIndex >= columnsCount) {
                        clearInterval(intervalId);
                    }
                }
            }
        
            const intervalId = setInterval(animateCells, 50);
        </script>
    </body>
    </html>
    """
    return htmlContent

def write_to_html_file(htmlContent):
    "Function to write HTML content to a file"
    now = datetime.datetime.now()
    # Create the file name as year_month_day_4digit random number.html
    fileName = f"{now.year}_{now.month:02d}_{now.day:02d}_{random.randint(1000, 9999)}.html"
    # creating a txt html
    with open(fileName, "w") as file:
        # write html content to the html file
        file.write(htmlContent)
        
    print(f"HTML file created and saved as: {fileName}\n") # print the file name the of the html file generated
