# def sum(a,b):
#     print(a+b)
# sum(10,20)

a=[1,2,3,4,5,6,7,8,9,10,11,12,3,14]
def count(a):
    dict={
    "odd":0,
    "even":0
}
    for i in range(1,len(a)):
        if a[i]%2==0:
            dict["odd"]+=1
        else:
            dict["even"]+=1
    
    print(dict)
count(a)
