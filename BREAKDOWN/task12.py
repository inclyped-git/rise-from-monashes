mimport unittest

class TestFunctions(unittest.TestCase):
    
    def testNavMaze(self):
        self.assertEqual(navigating_maze([(3,2), (3,3), (3,4)], [235, -12, -89], [50, 10, 2], 20, 10), ((3, 4), [43,2,7]))
        self.assertEqual(navigating_maze([(2, 2), (2, 3), (2, 4), (2, 5)], [112, -46, -76, -11], [8, 2, 3], 20, 10), ((2,4),[0,0,0]))
        self.assertEqual(navigating_maze([(2, 2), (2, 3), (2, 4), (2, 5)], [-12, 345, 123, 100], [0, 0, 3], 5, 8), (None, [0,0,3]))




BERYL_MAZE = [
  [300, -13, 189, -15, -12, 203, -23, 587, -78, 321, -46],
  [300, -11, -13, -24, 365, 198, -34, -21, 789, -81, -53],
  [300, -12, 112, -46, -76, -11, -23, -59, 321, 204, -32],
  [300, -23, 235, -12, -89, -62, -34, 212, -56, -67, -89],
  [300, 376, -23, -77, 227, -99, 134, 289, -12, 476, -51]
]

def check_valid_maze_location(desiredPosition: tuple[int]) -> bool:
    """
    Returns whether the entered location is within the range or not.
    
    @param tuple(int) currentPosition: The current row and column index the character is on.
    @return: A boolean value indicating if the location is within the BERYL_MAZE range or not.
    """
    if (desiredPosition[0] < 0 or desiredPosition[1] < 0 or desiredPosition[0] >= len(BERYL_MAZE) or desiredPosition[1] >= len(BERYL_MAZE[0])):
        return False
    return True

def visualise_maze(nestedList: list[list[int]], characterName: str, desiredPosition: tuple[int]) -> str:
    """
    
    """
    finalString = ""
    
    for i in range(len(nestedList)):
        for j in range(len(nestedList[0])):
            if desiredPosition[0] == i and desiredPosition[1] == j:
                finalString += "<" + characterName.upper()[0] + ">   "
            else:
                finalString += str(nestedList[i][j]) + "   "
        if (i < len(nestedList)-1):
            finalString += "\n"
    
    print(finalString)
    

def deploy_drone(nestedList: list[list[int]], location : tuple[int], direction: str, dollarIndicator: int) -> str:
    """
    """
    # storing coordinates and dollar indicators 
    row = int(location[0])
    column = int(location[1])
    
    coordinates = []; indicators = []
    foundDigit = False # sentinel
    
    if direction == "right":
        for index in range(column + 1, len(nestedList[row])):
            if str(dollarIndicator) not in str(nestedList[row][index]):
                coordinates.append( (row,index) )
                indicators.append( nestedList[row][index] )
            else:
                coordinates.append( (row, index) )
                indicators.append( nestedList[row][index] )
                foundDigit = True
                print(f"Found digit at location { (row, index)}!\n")
                return coordinates, indicators
        if not foundDigit:
            print(f"Entered restricted area!\n")
            return [],[]
    
    elif direction == "up":
        for index in range(row-1, -1,-1):  # looping through eachd row of the same column, upwards.
            if str(dollarIndicator) not in str(nestedList[index][column]):
                coordinates.append( (index, column) )
                indicators.append( nestedList[index][column] )
            
            else:
                coordinates.append( (index, column) )
                indicators.append( nestedList[index][column] )
                foundDigit = True
                print(f"Found digit at location { (index, column)}!\n")
                return coordinates, indicators

        if not foundDigit:
            print(f"Entered restricted area!\n")
            return [],[]
        

    elif direction == "down":
        for index in range(row+1, len(nestedList)):  # looping through each row of the same column, downwards.
            if str(dollarIndicator) not in str(nestedList[index][column]):
                coordinates.append( (index, column) )
                indicators.append( nestedList[index][column] )
            
            else:
                coordinates.append( (index, column) )
                indicators.append( nestedList[index][column] )
                foundDigit = True
                print(f"Found digit at location { (index, column)}!\n")
                return coordinates, indicators
  
        if not foundDigit:
            print(f"Entered restricted area!\n")
            return [],[]
        


def navigating_maze(visitedList: list[tuple[int]], dollarIndicatorList: list[int], funds, dustsToDoubloons, doubloonsToDorabies):
    
    """
    self.assertEqual(navigating_maze([(3,2), (3,3), (3,4)], [235, -12, -89], [50, 10, 2], 20, 10), ((3, 4), [43,2,7]))
    self.assertEqual(navigating_maze([(2, 2), (2, 3), (2, 4), (2, 5)], [112, -46, -76, -11], [8, 2, 3], 20, 10), ((2,4),[0,0,0]))
    self.assertEqual(navigating_maze([(2, 2), (2, 3), (2, 4), (2, 5)], [-12, 345, 123, 100], [0, 0, 3], 5, 8), (None, [0,0,3]))
    """
    def convertDollarIndicatorToDust(indicator):
        if indicator > 0:
            convertedDorabies = int(indicator / 100)
            remainingIndicator = indicator - convertedDorabies * 100
            
            convertedDoubloons = int(remainingIndicator / 10)
            remainingIndicator = remainingIndicator - convertedDoubloons * 10
            
            return remainingIndicator + convertedDoubloons * dustsToDoubloons + convertedDorabies * dustsToDorabies

        elif indicator < 0:
            indicator = -1 * indicator
            convertedDorabies = int ( indicator / 10 )
            remainingIndicator = indicator - convertedDorabies * 10
            
            return -1 * ( convertedDorabies * dustsToDorabies + remainingIndicator * dustsToDoubloons )
        
        return 0

    canExitLoop = False
    index = 0
    currentCoordinate = None
    
    finalDorabies = funds[0] 
    finalDoubloons = funds[1]
    finalDusts = funds[2]
    
    dustsToDorabies = dustsToDoubloons * doubloonsToDorabies
    
    totalDusts = finalDorabies * dustsToDorabies + finalDoubloons * dustsToDoubloons + finalDusts
    
    while index < len(visitedList):
        currentIndicator = dollarIndicatorList[index]
        
        totalDusts += convertDollarIndicatorToDust(currentIndicator)
        
        if totalDusts < 0 and index == 0:
            break
        
        finalDorabies = int( totalDusts / dustsToDorabies ) if int( totalDusts / dustsToDorabies ) > 0 else 0
        remainingDusts = totalDusts - finalDorabies * dustsToDorabies
            
        finalDoubloons = int( remainingDusts / dustsToDoubloons ) if  int( remainingDusts / dustsToDoubloons ) > 0 else 0
        remainingDusts = remainingDusts - finalDoubloons * dustsToDoubloons
            
        finalDusts = remainingDusts if remainingDusts > 0 else 0
        currentCoordinate = visitedList[index]
        
        if totalDusts < 0:
            break
        
        index += 1
    return currentCoordinate, [finalDorabies, finalDoubloons, finalDusts]
        
if __name__ == "__main__":
    #visualise_maze(BERYL_MAZE, "DORAEMON", (4,9))
    #print(deploy_drone(BERYL_MAZE, (1,2), "up", 3))
    
    """
    visited_position_list, dollar_indicator_list = deploy_drone(BERYL_MAZE, (0,0), "up", 9)
    print(visited_position_list)

    
    print(dollar_indicator_list)
    """
    unittest.main()
    #print(navigating_maze([(3,2), (3,3), (3,4)], [235, -12, -89], [50, 10, 2], 20, 10))
        