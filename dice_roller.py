def main():
  print('You rolled a die')

if __name__== "__main__":
  main()


list = [18,5,7,6,9,2,4,1,0,15,59,55,100,11,32,100,69,81]

def sort(list):
    for i in range(len(list)):
        minpos = i
        for j in range(i, len(list)):
            if list[j] > list[minpos]:
                minpos = j
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp
        print(list)  # To see every swap

sort(list)
print("Sorting by Selection Sort:", list)
