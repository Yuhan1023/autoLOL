import cv2,json
from picProcessor import picProcessor
from agent import agent

p = agent(test=True)
if __name__ == '__main__':
	# if len(sys.argv) == 1:
	# 	gameIndex = 9
	# else:
	# 	gameIndex = sys.argv[1]
	#
	# path = r'E:\develop\autoLOL\ans/game{}/'.format(gameIndex)
	#
	# if not os.path.exists(path):
	# 	print('not exist')
	# 	exit(1)
	#
	# with open(path + 'infor.txt', "r") as f:  # 设置文件对象
	# 	inforStr = f.read()  # 可以是随便对文件的操作
	#
	# ss = inforStr.split('*fenge*')
	# print(ss)
	# for s in ss:
	# 	if s is not '':
	# 		dic = json.loads(s)
	# 		if dic['params']['HP'] > 10:
	# 			print(dic['file'],dic['params']['HP'])
	# 			img =cv2.imread(path + '{}.png'.format(dic['file']))
	# 			print(img.shape)
	# 			p.get_pic(img)

	# for i in range(10):
	# index = i * 50 + 13

	img = cv2.imread(r'D:\develop\autoLOL\ans\game1\10.png')
	p.pic_processor.get_pic(img, test=True)
