## python-瓷砖铺贴图生成

最近家里装修，选了一款花砖，有9种样式，最终拼成地面的铺贴图，比如
![image](https://github.com/travisjiang/floor_finish/blob/master/output/1503541533.jpg?raw=true)

为此写一个程序随机生成铺贴图案，选一个相对美观的用上：

	* 地面大小为5*11
	* 每款转的数量有限，总和有64
	* 随机选择55块，随机的摆放位置，生成铺贴图


有时候随机的效果不够好，也可以固定部分砖，形成特定图案，其他位置随机
![image](https://github.com/travisjiang/floor_finish/blob/master/output/1503541579.jpg?raw=true)

使用：python floor_join.py
如果要使用特定花纹：修改floor_join.py中的mat或者choose

