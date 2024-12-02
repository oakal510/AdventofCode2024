""" Solution for Advent of Code 2024, Day 2, Part 2 """

def reformat(report):
    report_values = report.split()
    report_values = [int(value) for value in report_values]
    return report_values


def is_safe(report_values):
    
    increasing = False
    decreasing = False
    
    for i, value in enumerate(report_values):

        if i == 0:
            if value < report_values[i+1]:
                increasing = True
            elif value > report_values[i+1]:
                decreasing = True
            else:
                 return 0

        if i+1 < len(report_values):
            if abs(value - report_values[i+1]) > 3:
                return 0
            if i != 0:
                if increasing:
                    if is_increasing(value, report_values[i+1]):
                        continue
                    else:
                        return 0
                elif decreasing:
                    if is_decreasing(value, report_values[i+1]):
                        continue
                    else:
                        return 0
    
    return 1


def is_increasing(value, next_value):
    if value < next_value:
        return True
    else:
        return False
    

def is_decreasing(value, next_value):
    if value > next_value:
        return True
    else:
        return False


if __name__ == "__main__":

    count = 0
    
    with open('day_02/input.txt') as file:
        
        for line in file:
            report = reformat(line)
            
            if is_safe(report) == 1:
                count += 1
            else: 
                for i, item in enumerate(report):
                    test_report = report.copy()
                    test_report.pop(i)
                    if is_safe(test_report) == 1:
                        count += 1
                        break
                    else:
                        continue

    print(count)