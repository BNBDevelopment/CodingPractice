from typing import List


class Count_Good_Triplets_1534:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        if len(arr) > 2:
            for i in range(0, len(arr)-2):
                #print("arr[i]: " + str(arr[i]))
                for j in range(i+1, len(arr)-1):
                    #print("arr[j]: " + str(arr[j]))
                    if abs(arr[i] - arr[j]) <= a:
                        for k in range(j+1, len(arr)):
                            #print("arr[k]: " + str(arr[k]))
                            if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                                #print("Winner!" + "arr[i]: " + str(arr[i]) + " arr[j]: " + str(arr[j]) + " arr[k]: " + str(arr[k]))
                                count += 1
        return count


class Find_the_Winner_of_an_Array_Game_1535:
    def getWinner(self, arr: List[int], k: int) -> int:

        testIndex = 0
        wincount = 0
        # print("New arr: " + str(arr))
        if k > len(arr):
            return max(arr)
        while testIndex < len(arr):
            if arr[testIndex] > arr[testIndex + 1]:
                # print("testIndex WINS: " + str(arr[testIndex]) + " vs " + str(arr[testIndex+1]))
                # print("list(arr[:testIndex+1]): " + str(list(arr[:testIndex+1])))
                # print("list(arr[testIndex+2:]: " + str(list(arr[testIndex+2:])))
                # print("list(arr[testIndex+1]: " + str([arr[testIndex+1]]))
                arr = arr[:testIndex + 1] + arr[testIndex + 2:] + [arr[testIndex + 1]]
                wincount += 1
                if wincount == k:
                    return arr[testIndex]
            else:
                # print("testIndex LOSES: " + str(arr[testIndex]) + " vs " + str(arr[testIndex+1]))
                arr = arr[:testIndex] + arr[testIndex + 1:] + [arr[testIndex]]
                # testIndex += 1
                wincount = 1
                if wincount == k:
                    return arr[testIndex]
        # print("New arr: " + str(arr))

