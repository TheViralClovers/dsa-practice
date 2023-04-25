class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        output = [intervals[0]] #new array to store the reuslt of all merges, intitialised to first element of the sorted interval array
        for start,end in intervals[1:]:
            lastEnd = output[-1][1] #stores the first element of the output array that contains the merged interval
            if start<=lastEnd: #check if interval is within
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])
        return output

            