__author__ = 'shihchosen'
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist 只是对统一对象指派的另一个名字

del shoplist[0] # 我买了第一项商品， 因此我把它从清单上移除

print('shoplist is', shoplist)
print('mylist is', mylist)
#注意shoplist和mylist两者print的结果是相同的＃
#删除的这个 apple去让我们确信两者指向同一个对象#
print('Copy by making a full slice')
mylist = shoplist[:] # 引用所有的选项形成一个拷贝

del shoplist[0] # 移除第一个项目
print('shoplist is', shoplist)
print('mylist is', mylist)
#注意此时两个列表的输出是不同的