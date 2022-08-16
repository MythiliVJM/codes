class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		 res=[]     #created new list
         for i in range(0,n):
             if i+1==arr[i]:  #here index is start from 1 so i+1 equals to arr[i]
                  res.append(arr[i])
         return res




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1
