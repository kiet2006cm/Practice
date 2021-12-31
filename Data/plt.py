import matplotlib.pyplot as mpl
import numpy as np
cos=lambda x: np.cos(x)
tan=lambda x: np.tan(x)
sin=lambda x: np.sin(x)
rng= np.random.RandomState(0)
x = rng.randn(100)
y= rng.randn(100)
# mpl.plot(x,y, color="green", linestyle="dashed", label='con lãi')
# mpl.plot(y,x, linestyle='dashed', label='con giun pha ke')
size=80*rng.randn(100)
color=rng.randn(100)
# dothihinhtron=mpl.scatter(x,y,s=size,c=color,cmap='viridis',alpha=0.3) #hình tròn
# alpha : độ trong suốt
# mpl.colorbar(dothihinhtron)

# mpl.title('Xàm loz tí')
# mpl.xlabel('X')
# mpl.ylabel('Y')

# mpl.axis([x,y,x2,y2]) hạn tầm nhìn #'tight': khít vào hình #'equal': trục xy = nhau
# mpl.xlim([start, stop]) giới hạn tầm nhìn
# mpl.ylim([start, stop]) tương tự 

menu={
    'Fried_Chicken': 32,
    'Pizza': 220,
    'Potato': 20,
    'Hambuger': 45
}

# mpl.bar(menu.keys(),menu.values()) 
#biểu đồ cột            # mpl.barh(): cũng i chang nhưng nó nằm ngang
#                                     phải chuyển thành list mới dùng được

# mpl.title('Menu')
# mpl.xlabel('Món ăn')
# mpl.ylabel('Giá (VNĐ)')

Student_Height= np.random.normal(170,10,100)
#                             khoảng,độ lệch chuẩn, size

# mpl.hist(Student_Height) #tuần suất sang cột
# biểu độ dạng gì đó giống kiểu tháp tuổi

fig, ((ax1,ax2),(ax3,ax4)) = mpl.subplots(
    nrows=2,
    ncols=2,
    figsize=(10,5)
)
ax1.hist(Student_Height)
ax2.bar(menu.keys(),menu.values())
ax3.plot(x,cos(x),y,cos(y))
ax4=ax4.scatter(cos(Student_Height),Student_Height,s=size,c=color,cmap='viridis',alpha=0.3)
mpl.colorbar(ax4)

# mpl.legend() #giúp show cái biến label tron plot
mpl.show()