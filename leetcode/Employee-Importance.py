"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph=defaultdict(list)

        for employee_info in employees:
            graph[employee_info.id].append(employee_info.importance)
            graph[employee_info.id].append(employee_info.subordinates)
       

        def dfs(id,total):

            total+=graph[id][0]
 
            for neighbour in graph[id][-1]:
                
                total=dfs(neighbour,total)
            return total
        return dfs(id,0)


            

        