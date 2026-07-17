class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def can_place(distance):
            count=1
            last_pos = position[0]

            for current_pos in position[1:]:
                if current_pos - last_pos >= distance:
                    count+=1
                    last_pos = current_pos

                    if count==m:
                        return True
            return False
        low=1
        high=position[-1] - position[0]
        answer=0

        while low<= high:
            mid = low+(high-low)//2

            if can_place(mid):
                answer=mid
                low=mid+1
            else:
                high=mid-1
        return answer
