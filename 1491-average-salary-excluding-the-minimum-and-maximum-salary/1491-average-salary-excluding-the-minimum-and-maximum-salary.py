class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.remove(min(salary))
        salary.remove(max(salary))
    
        return sum(salary) /len(salary)