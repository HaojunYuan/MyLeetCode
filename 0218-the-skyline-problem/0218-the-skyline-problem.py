class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return
        elif len(buildings) == 1:
            return self.processSingleBuilding(buildings[0])
        else:
            l,r = 0, len(buildings)-1
            res = self.process(l,r,buildings)
            return res
        
    def processSingleBuilding(self, building):
        left = building[0]
        right = building[1]
        height = building[2]
            
        return [[left, height],[right, 0]]
    
    def process(self, l, r, buildings):
        # process buildings
        if l>=r:
            return self.processSingleBuilding(buildings[l])
        mid = l+(r-l)//2
        left = self.process(l, mid, buildings)
        right = self.process(mid+1, r, buildings)
        res = self.merge(left, right)
        return res
    
    def merge(self, left, right):
        # left one has smaller x index
        # right one has smaller x index
        # has same x indices
        h1, h2 = 0, 0
        i,j = 0, 0
        res = []
        while i<len(left) and j<len(right):
            temp = [0,0]
            if left[i][0]<right[j][0]:
                x, height = left[i]
                temp[0]=x
                temp[1]=height
                if height<h2:
                    temp[1]=h2
                h1 = height
                i+=1
            elif left[i][0]>right[j][0]:
                x, height = right[j]
                temp[0]=x
                temp[1]=height
                if height<h1:
                    temp[1]=h1
                h2 = height
                j+=1
            else:
                temp[0]=left[i][0]
                temp[1]=max(left[i][1],right[j][1])
                h1 = left[i][1]
                h2 = right[j][1]
                i+=1
                j+=1
            res.append(temp)
        while i<len(left):
            res.append(left[i])
            i+=1
        while j<len(right):
            res.append(right[j])
            j+=1
        # Remove duplicates in the res
        k = 0
        while k<len(res):
            while k+1 < len(res):
                if res[k][1]==res[k+1][1]:
                    res.pop(k+1)
                else:
                    break
            k+=1
        return res
        