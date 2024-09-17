def diamond(row):
    for i in range(1,row+1,1):
        print(" "*(row-i)+"*"*(2*i-1))
        if(i == row):
            for j in range(row-1,0,-1):
                print(" "*(row-j)+"*"*(2*j-1))


row = int(input("Enter number of rows you want in diamond \n"))
print(diamond(row))
