class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''new_Arr=[]
        for i in range(1,len(arr)):
            new_Arr.append(max(arr[i:]))
        new_Arr.append(-1)
        return new_Arr'''
        for i in range(len(arr)):
            if arr[i+1:]!=[]:
                arr[i]=max(arr[i+1:])
            else:
                arr[i]=-1
        return arr
