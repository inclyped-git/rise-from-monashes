import unittest

class TestAllFunctions(unittest.TestCase):
    
    def test_funds_string(self):
        self.assertEqual(get_funds_string([4,5,19]), "4 Dorabies, 5 Doubloons and 19 Dusts")
        self.assertEqual(get_funds_string([3,0,2]), "3 Dorabies, 0 Doubloons and 2 Dusts")
        self.assertEqual(get_funds_string([1,2,3]), "1 Dorabie, 2 Doubloons and 3 Dusts")
        self.assertEqual(get_funds_string([5,6,88]), "5 Dorabies, 6 Doubloons and 88 Dusts")
        self.assertEqual(get_funds_string([4,1,77]), "4 Dorabies, 1 Doubloon and 77 Dusts")
    
    def test_conversion(self):
        self.assertEqual(beryl_dollar_conversion(540,20,5), [5, 2, 0])
        self.assertEqual(beryl_dollar_conversion(123,32,15), [0, 3, 27])
        self.assertEqual(beryl_dollar_conversion(111,10,5), [2, 1, 1])
        self.assertEqual(beryl_dollar_conversion(387,28,6), [2, 1, 23])
        self.assertEqual(beryl_dollar_conversion(15543,255,11), [5, 5, 243])
        
    def test_indicator(self):
        self.assertEqual(beryl_dollar_indicator(152, [0,3,5], 10, 5), [2, 3, 7])
        self.assertEqual(beryl_dollar_indicator(-22, [0,3,5], 10, 5), [0, 0, 0])
        self.assertEqual(beryl_dollar_indicator(542, [5,10,40], 30, 10), [11, 5, 12])
        self.assertEqual(beryl_dollar_indicator(-32, [10,20,33], 12, 5), [11, 0, 9])
        self.assertEqual(beryl_dollar_indicator(-89, [1,6,78], 10, 5), [0,0,0])
         

def get_funds_string(listOfBerylDollars: list[int]) -> str:
    """
    Returns the number of Dorabies, Doubloons, and Dusts the user has, from a given list of dollars in a string format.
    
    @param list[int] listOfBerylDollars: List of dollars representing respective Dorabies, Doubloons, and Dusts.
    @return: Representable string that represents Dorabies, Doubloons, and Dusts that the user has.
    """
    # extracting dorabies, doubloons, and dusts and storing them in appropriate variables.
    numOfDorabies = listOfBerylDollars[0] 
    numOfDoubloons = listOfBerylDollars[1]
    numOfDusts = listOfBerylDollars[2] 

    # manipulates the output string depending on the number of dollar units the user has. 
    hasMultipleDorabies = "Dorabies" if ( numOfDorabies > 1 or numOfDorabies == 0) else "Dorabie"
    hasMultipleDoubloons = "Doubloons" if ( numOfDoubloons > 1 or numOfDoubloons == 0) else "Doubloon"
    hasMultipleDusts = "Dusts"  if ( numOfDusts > 1 or numOfDusts == 0) else "Dust"

    # returning the final output of the dollar units.
    return ("{0} {1}, {2} {3} and {4} {5}".format(numOfDorabies, hasMultipleDorabies, numOfDoubloons, hasMultipleDoubloons, numOfDusts, hasMultipleDusts))
    
    
def beryl_dollar_conversion(amountOfDusts: int, dustToDoubloon_rate: int, doubloonToDorabies_rate: int) -> list[int]:
    """
    Returns a list of converted Dorabies, Doubloons, and Dusts from a given number of Dusts
    
    @param int amountOfDusts: Takes in the number of Dusts the user has.
    @param int dustToDoubloon_rate: The rate of conversion from Dusts to Doubloons.
    @param int doubloonToDorabies_rate: The rate of conversion from Doubloons to Dorabies.
    @return: A list of converted Dorabies, Doubloons, and Dusts.
    """
    dustToDorabie_rate = (dustToDoubloon_rate * doubloonToDorabies_rate) # getting the dust to dorabie rate for direct conversion of dust to dorabies.

    # converting dusts to dorabies and remaining dusts.
    convertedDorabies = int ( amountOfDusts / dustToDorabie_rate )
    remainingDusts = amountOfDusts - ( convertedDorabies * dustToDorabie_rate )

    # converting remaining dusts to doubloons and final dusts.
    convertedDoubloons = int ( remainingDusts / (dustToDoubloon_rate) )
    convertedDusts = remainingDusts - ( convertedDoubloons * dustToDoubloon_rate )

    # returning a list of converted dollar units.
    return [convertedDorabies, convertedDoubloons, convertedDusts]
    

def beryl_dollar_indicator(dollarIndicator: int, startingFundsList: list[int], dustsToDoubloons_rate: int, doubloonsToDorabies_rate: int) -> list[int]:
    """
    Returns a list of Dorabies, Doubloons, and Dusts remaining after encountering with the Dollar Indicator.
    
    @param int dollarIndicator: The Dollar Indicator
    @param list[int] startingFundsList: The starting Dorabies, Doubloons, Dusts before encountering with the Dollar Indicator.
    @param int dustToDoubloon_rate: The rate of conversion from Dusts to Doubloons.
    @param int doubloonToDorabies_rate: The rate of conversion from Doubloons to Dorabies.
    @return: A list of final Dorabies, Doubloons, Dusts after encountering the Dollar Indicator.
    """
    
    # converting dollarIndicator into dusts
    totalDusts = 0
    if (dollarIndicator> 0): # if dollar indicator is positive.
        
        # first digit of the indicator is the dorabie amount added to the initial dorabie amount.
        convertedDorabies = int( dollarIndicator / 100 )
        remainingDollarIndicator = dollarIndicator - ( convertedDorabies * 100 ) # remaining dollar indicators is calculated.
        
        # second digit of the indicator is the doubloon amount added to the initial doubloon amount.
        convertedDoubloons = int ( remainingDollarIndicator / 10 )
        remainingDollarIndicator = remainingDollarIndicator - convertedDoubloons * 10 # remaining dollar indidcators is calculated.

        totalDusts = remainingDollarIndicator + ( convertedDoubloons * dustsToDoubloons_rate ) + ( convertedDorabies * ( dustsToDoubloons_rate * doubloonsToDorabies_rate ) ) # convert all of the converted units back to dusts.

    else: # if dollar indicator is negative.
        
        # first digit of the indicator is the dorabie amount going to be subtracted from the starting dorabie amount.
        convertedDorabies = int ( dollarIndicator / 10 )
        remainingDollarIndicator = dollarIndicator - ( convertedDorabies * 10 ) # remaining dollar indicators is calculated.
        
        totalDusts = ( remainingDollarIndicator * dustsToDoubloons_rate ) + ( convertedDorabies * (dustsToDoubloons_rate * doubloonsToDorabies_rate) ) # convert all of the converted units back to dusts.
        
    # getting the starting dorabie, doubloon, and dust amounts from the list startingFundsList[]
    startingDorabies = startingFundsList[0]
    startingDoubloons = startingFundsList[1]
    startingDusts = startingFundsList[2]

    # converting starting dorabies, doubloons, dusts all to dusts.
    startingTotalDusts = startingDorabies * (dustsToDoubloons_rate * doubloonsToDorabies_rate)
    startingTotalDusts += startingDoubloons * (dustsToDoubloons_rate)
    startingTotalDusts += startingDusts

    # adding the starting dust amount with the dusts converted from the dollar indicator.
    finalTotalDusts = startingTotalDusts + totalDusts

    # converting the final dusts back to dorabies, doubloons, and remaining dusts
    # if dorabies, doubloons and dusts are less than 0, it is automatically defined to 0.
    finalDorabies = int ( finalTotalDusts / (dustsToDoubloons_rate * doubloonsToDorabies_rate) ) if int ( finalTotalDusts / (dustsToDoubloons_rate * doubloonsToDorabies_rate) ) > 0 else 0
    remainingFinalDusts = finalTotalDusts - ( finalDorabies *  (dustsToDoubloons_rate * doubloonsToDorabies_rate) ) # remaning dusts after dorabie conversion

    finalDoubloons = int ( remainingFinalDusts / (dustsToDoubloons_rate) ) if int ( remainingFinalDusts / (dustsToDoubloons_rate) ) > 0 else 0
    
    finalDusts = remainingFinalDusts - ( finalDoubloons * dustsToDoubloons_rate ) # remaning dusts after doubloon conversion
    finalDusts = finalDusts if finalDusts > 0 else 0
    
    return [finalDorabies, finalDoubloons, finalDusts]

#for debugging purpose only, please delete during final submission
if __name__ == "__main__":
    unittest.main()