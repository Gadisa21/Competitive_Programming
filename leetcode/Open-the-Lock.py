class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1
        que=deque()
        visited=set(deadends)
        visited.add("0000")
        que.append(["0000",0])

        def keys(locks):
            result=[]
            for i in range(4):
                digit=str((int(lock[i])+1)%10)
                result.append(lock[:i]+digit+lock[i+1:])
                digit=str((int(lock[i])-1+10)%10)
                result.append(lock[:i]+digit+lock[i+1:])
            return result
        while que:
            lock,turn=que.popleft()
            if lock==target:
                return turn

            for key in keys(lock):
                if key not in visited:
                    visited.add(key)
                    que.append([key,turn+1])
        return -1

                


        