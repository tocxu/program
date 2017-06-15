def almostIncreasingSequence(sequence):
    for j in range(0, (len(sequence) - 1)):
        if (sequence[j] >= sequence[j + 1]) &(j < (len(sequence) - 2)):
            if (sequence[j] <= sequence[j + 2]):
                del sequence[j + 1]
                print sequence
                break
            else:
                del sequence[j]
                print sequence
                break
        elif(sequence[j] >= sequence[j + 1])&(j==(len(sequence)-2)):
            del sequence[j+1]
            print sequence
            break
        elif (sequence[j] >= sequence[j + 1]):
            del sequence[j]
            print sequence
            break
    for i in range(0, (len(sequence) - 1)):
        if (sequence[i] >= sequence[i + 1]):
            return False
    return True

if __name__ == '__main__':
    sequence = [3, 5, 67, 98, 3]
    if almostIncreasingSequence(sequence)== True:
        print ("True")
    else: print ("False")
