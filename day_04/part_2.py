""" Solution for Advent of Code 2024, Day 4, Part 2 """

def find_xmax_xs(input):

    count = 0

    input_list = input.split("\n")
    input_grid = [list(line) for line in input_list]

    for i, line in enumerate(input_grid):
        for j, letter in enumerate(line):
            if i == len(input_grid) - 2:
                return count
            else:
                if j <= len(line) - 3:
                    # find forward x_mas x 
                    # find top of the x and middle of the x
                    if (letter == 'M' or letter == 'S') and (input_grid[i][j+2] == "S" or input_grid[i][j+2] == "M") and (input_grid[i+1][j+1] == "A"):
                            # find bottom left of the x
                            if (letter == "M" and input_grid[i+2][j+2] == "S") or (letter == "S" and input_grid[i+2][j+2] == "M"):
                                #find bottom right of the x
                                if (input_grid[i][j+2] == "M" and input_grid[i+2][j] == "S") or (input_grid[i][j+2] == "S" and input_grid[i+2][j] == "M"):
                                    count += 1
   

if __name__ == "__main__":

    with open('day_04/input.txt') as file:
        input = file.read()
    
    print(find_xmax_xs(input))