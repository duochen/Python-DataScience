def example1():
    while True:
       try:
            x = int( input( "enter a number: " ) )
            y = int( input( "enter another number: " ) )
            print( x, '/', y, '=', x/y )
            break
       except ZeroDivisionError:
            print( "Can't divide by 0!" )
       except ValueError:
            print( "That doesn't look like a number!" )
       except:
            print( "something unexpected happend!" )
            
def example2( L ):
    print( "\n\nExample 2" )
    print( "L          = ", L )
    sum = 0
    sumOfPairs = []
    for i in range( len( L ) ):
            try:
                sumOfPairs.append( L[i]+L[i+1] )
            except IndexError:
                continue
            except TypeError:
                continue
    
    print( "sumOfPairs = ", sumOfPairs )

def printUpperFile( fileName ):
    try:
       file = open( fileName, "r" )
    except FileNotFoundError:
       print( "***Error*** File", fileName, "not found!" )
       return False
    
    for line in file:
        print( line.upper() )
    file.close()
    return True
    
def main():
    example1()
    
    L = [ 10, 3, 5, 6, 9, 3 ]
    example2( L )

    L = [ 10, 3, "NA", 6, 9, 3 ]
    example2( L )
    
    open( "doesNotExistYest.txt", "w" ).close()

    printUpperFile( "misspelled.txt" )


main()
