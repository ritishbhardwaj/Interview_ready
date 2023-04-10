
class Solution:
    def customSort(self, phy, chem, math, N):
        
        student_marks=[]
        for i in range(N):
            student_marks.append((phy[i],chem[i],math[i]))
        # print(student_marks)
        student_marks.sort(key = lambda x:(x[0],-x[1],x[2]))
        # print(student_marks)
        for i in range(N):
            phy[i]=student_marks[i][0]
            chem[i]=student_marks[i][1]
            math[i]=student_marks[i][2]

        return phy, chem , math



obj=Solution()
N = 10
phy= [4, 1, 10, 4, 4, 4, 1, 10, 1, 10]
chem= [5, 2, 9, 6, 3, 10, 2, 9, 14, 10]
math= [12, 3, 6, 5, 2, 10, 16, 32, 10, 4]

print(obj.customSort(phy,chem,math,N))