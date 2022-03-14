from testCases import *

def points( index ) :
		
	#returns approriate grade points based on the test index
    x = 5
    if( index == 0 ) :
        return 2 * x 
    elif( index == 1 ) : 
        return 2 * x
    elif( index == 2 ) :
        return 1 * x 
    elif( index == 3 ) :
        return 1 * x
    elif( index == 4 ) :
        return 2 * x
    elif( index == 5 ) :
        return 1 * x
    elif( index == 6 ) :
        return 1 * x
    elif( index == 7 ) :
        return 1 * x
    else :
        return 0
        
def test() :
    
    test = []
    test.append( evaluateQuestion( q1() ) )
    test.append( evaluateQuestion( q2() ) )
    test.append( evaluateQuestion( q3() ) )
    test.append( evaluateQuestion( q4() ) )
    test.append( evaluateQuestion( q5() ) )
    test.append( evaluateQuestion( q6() ) )
    test.append( evaluateQuestion( q7() ) )
    test.append( evaluateQuestion( q8() ) )
    
    return test

#this method computes students grade for this lab...
def gradeAssignment() :

    flag = True
    totalPoints = 0
    earnedPoints = 0
    
    i = 0
    
    print("\n//..............Running testcases for the operations.............//")
    myTest = test() #invoking the test(...) method
    while( i < len( myTest ) ) :
    
        myPoints = round( points( i ), 2 )
        totalPoints += myPoints
        if( myTest[i] == True ) :
            print(f"Test {i}, Q{i+1} passed. [Alloted point(s): {myPoints}]")
            earnedPoints += points( i )
        else :
            print(f"Test {i}, Q{i+1} failed. [Alloted point(s): {myPoints}]")
            flag = False
            
        i += 1
    
    if( flag ) :
        print("All tests are successful.")
    else :
        print("Not all tests are successful.")
    
    print(f"Total points earned in this assignment: {round(earnedPoints, 2)} (out of) {totalPoints} points")
    print("//.............................End...............................//")