class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

def getImportance(employees, id):
    '''
    方法：DFS  前序遍历
         每个员工看成是一个节点
         其下属看成一个N叉树
    '''
    emap = {e.id: e for e in employees}
    ###递归本层级子员工
    def dfs(eid):
        employee = emap[eid]
        return (employee.importance + sum(dfs(eid) for eid in employee.subordinates))
    return dfs(id)

def getImportance1(employees, id):
    '''
    方法：BFS 层序遍历
    '''
    emap = {e.id: e for e in employees}
    res = 0
    queue = [id]
    while queue:
        ###本层级员工重要性计算
        res += sum(emap[iid].importance for iid in queue)
        ###下一层级员工id统计
        queue = [sub for iid in queue for sub in emap[iid].subordinates]
    return res

if __name__ == '__main__':
    nums = [[1,2,[2]], [2,3,[]]]
    employees = [Employee(x[0],x[1],x[2]) for x in nums]
    print(getImportance1(employees, 2))


