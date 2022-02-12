# class Student:

#   def __init__(self,name):
#     self.name=name

#   def calculate_avg(self,date):
#     sum=0

#     for num in date:
#       sum+=num
    
#     avg=sum/len(date)
#     return avg

#   def judge(self,avg):

#     if(avg>=60):
#       result='passed'
#     else:
#         result='failed'
#     return result

# a001=Student('sato')
# date=[70,65,50,10,30]
# avg=a001.calculate_avg(date)
# result=a001.judge(avg)

# print(avg)
# print(a001.name+' '+result)

# count=1
# x=1
# while x>=1:
#     x=int(input())
#     if x==0:
#       break
#     print('Case '+str(count)+': '+str(x))
#     count+=1
  
# while True:
#     x,y=map(int,input().split())
#     if x==0 and y==0:
#       break
#     if x>y:
#       print(y,x)
#     else:
#       print(x,y)

a,b=map(int,input().split())
d=a/b
r=a%b
f=a/b
print(str(d)+str(r)+str('{}'.format(f)))