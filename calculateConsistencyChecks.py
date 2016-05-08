from SudokuStarter import *
import os

resultsFile = open("results.txt", "w")
path = 'input_puzzles/more/'
# path = 'input_puzzles/easy'
typePuzzle = ['9x9', '16x16', '25x25']
backtrackingArgs =      {'forward_checking': False, 'MRV': False, 'Degree': False, 'LCV': False}
forwardCheckingArgs =   {'forward_checking': True,  'MRV': False, 'Degree': False, 'LCV': False}
MRVArgs =               {'forward_checking': True,  'MRV': True,  'Degree': False, 'LCV': False}
DegreeArgs =            {'forward_checking': True,  'MRV': False, 'Degree': True,  'LCV': False}
LCVArgs =               {'forward_checking': True,  'MRV': False, 'Degree': False, 'LCV': True}
listArgs = [backtrackingArgs, forwardCheckingArgs, MRVArgs, DegreeArgs, LCVArgs]
# listArgs = [MRVArgs, DegreeArgs, LCVArgs]

for pathPuzzle in typePuzzle:
    print 'Running ' + str(pathPuzzle) + ' puzzles '
    resultsFile.write('Running ' + str(pathPuzzle) + ' puzzles ' + '\n')
    for arguments in listArgs:
        print 'Arguments: ' + str(arguments)
        resultsFile.write('Running with arguments: ' + str(arguments) + '\n')
        numSuccesses = 0
        totalConsistencyChecks = 0
        for file in os.listdir(path+pathPuzzle):
            print 'File: ' + str(file)
            # resultsFile.write('File: ' + str(file) + '\n')
            tempBoard = init_board(path + pathPuzzle + '/' + file)
            vals = arguments.values()

            winBoard, numConsistencyChecks = solve(tempBoard, vals[0], vals[1], vals[2], vals[3])
            print 'Number of consistency checks: ' + str(numConsistencyChecks)
            resultsFile.write('Number of consistency_checks = ' + str(numConsistencyChecks) + '\n')

            if winBoard:
                totalConsistencyChecks += numConsistencyChecks
                numSuccesses += 1
            else:
                print 'File ' + str(file) + ' timed out '
                resultsFile.write('File ' + str(file) + ' timed out ' + '\n')
        print str(numSuccesses) + " boards succeeded, average number of consistency checks was: " + str(round(totalConsistencyChecks/numSuccesses, 5))
        resultsFile.write(str(numSuccesses) + " boards succeeded, average number of consistency checks was: " + str(round(totalConsistencyChecks/numSuccesses, 5)) + '\n')

resultsFile.close()
