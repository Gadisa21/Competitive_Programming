class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited=set()
        que=deque()
        que.append(0)
        visited.add(0)

        while que:
            node=que.popleft()
            for neighbour in rooms[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    que.append(neighbour)
            
        return len(rooms)==len(visited)

        
        