'''
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.


'''

# Analyze the unusual data from the engineers. How many reports are safe?



file = open('input/Day2.txt', 'r')

inputFile = file.read()

reports = inputFile.split('\n')

safeReports = 0

def lvldiff(x,y):
    if x > y:
        return x - y
    return y-x

# def check(report, decreasing):
#     for index, lvl in enumerate(report[:-1]):
#         if report[index] - report[index+1] <0:
#             dec = False
#         else:
#             dec = True

#         if dec != decreasing:
#             return False

#         if 1 <= lvldiff(report[index], report[index+1]) <= 3 :
#            continue
#         else:
#             return False
#     return True


# for item in reports:
#     report = item.split()
#     for index, delta in enumerate(report):
#         report[index] = int(delta)
#     if report[0] - report[1] <0:
#         decreasing = False
#     else:
#         decreasing = True
#     if check(report, decreasing) == True:
#         safeReports += 1
            
# print(safeReports)


# Answer: 411

'''
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
'''




def check(report, dampcount):
    index = 0
    
    # Handle the case where the first two levels are the same
    if len(report) > 1 and report[0] == report[1]:
        dampcount += 1
        if dampcount > 1:
            return False
        
        # Try removing the first or second level and check recursively
        for i in [0, 1]:
            temp_report = report[:]
            temp_report.pop(i)
            if check(temp_report, dampcount):
                return True
        return False

    # Determine the initial decreasing trend
    decreasing = len(report) > 1 and report[0] > report[1]

    while index < len(report) - 1:
        dec = report[index] > report[index + 1]

        # Check if the trend changes
        if dec != decreasing:
            dampcount += 1
            if dampcount > 1:
                return False

            # Try removing the current or adjacent levels and check recursively
            for i in [index, index - 1, index + 1]:
                if 0 <= i < len(report):  # Ensure index is valid
                    temp_report = report[:]
                    temp_report.pop(i)
                    if check(temp_report, dampcount):
                        return True
            return False

        # Check if the difference between levels is valid
        if 1 <= abs(report[index] - report[index + 1]) <= 3:
            index += 1  # Move to the next index
        else:
            dampcount += 1
            if dampcount > 1:
                return False

            # Try removing the current or adjacent levels and check recursively
            for i in [index, index - 1, index + 1]:
                if 0 <= i < len(report):  # Ensure index is valid
                    temp_report = report[:]
                    temp_report.pop(i)
                    if check(temp_report, dampcount):
                        return True
            return False

    return True


# Main loop to process reports
for item in reports:
    report = [int(delta) for delta in item.split()]  # Convert report to integers

    if check(report, dampcount=0):  # Check the report
        safeReports += 1

print(safeReports)


# answer : 465