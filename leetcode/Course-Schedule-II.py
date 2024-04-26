class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph=defaultdict(list)
        in_degree=defaultdict(int)

        for c,p in prerequisites:
            graph[p].append(c)
            in_degree[c]+=1
        
        que=deque()
        
        for i in range(numCourses):
            if in_degree[i]==0:
                que.append(i)
        
        ans=[]
        while que:
            course=que.popleft()

            for num in graph[course]:
                in_degree[num]-=1
                if in_degree[num]==0:
                    que.append(num)
            ans.append(course)
        return ans if len(ans)==numCourses else []
        