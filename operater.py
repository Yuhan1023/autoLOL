# -*- coding: utf-8 -*-
import time
import json, os
import numpy as np
import random
from dm.MainCommucation import MainCommucation


class operater(MainCommucation):
	def __init__(self, id=1,test = False):
		self.id = id
		self.test = test
		self.commandCahe = {
			'time': 0,
			'commandList': []
		}
		if not test:
			super(operater, self).__init__()
			self.start()

	def randomChooseTargetAction(self:any,action:dict):
		'''
		根据softmax得出的值，随机选择一个动作
		:param action:动作字典，key为动作名 value为动作未指数前概率
		:return:动作名称
		'''
		keys = np.array(list(action.keys()))
		values = np.array(list(action.values()))
		values = np.e**values

		randomTarget = random.random()*np.sum(values)

		s = 0
		targetActionIndex = 0
		for i in range(len(values)):
			s += values[i]
			if randomTarget < s:
				targetActionIndex = i
				break
		targetAction = keys[targetActionIndex]
		return targetAction

	def goHome(self):
		'''
		返回泉水
		:return:无
		'''

		pass

	def actionExcute(self:any,action:dict,params:dict):
		'''
		根据字典随机选择动作并执行动作
		:param action:动作字典
		:param params:参数字典
		:return:
		'''
		targetAction = self.randomChooseTargetAction(action)

		if targetAction == 'go':
			targetPostion = params.get('go', None)
			if targetPostion is not None:
				self.MoveToPostion(targetPostion, True)
			targetAction = [1,0,0]
		elif targetAction == 'back':
			targetPostion = params.get('back', None)
			if targetPostion is not None:
				self.MoveToPostion(targetPostion, False)
			targetAction = [0, 1, 0]
		elif targetAction == 'standAndAttack':
			targetPostion = [590,358]
			self.MoveToPostion(targetPostion, True)
			targetAction = [0, 0, 1]
		else:
			print('未实现动作 待实现：{}'.format(targetAction))
			raise
		return targetAction


	def MoveToPostion(self, postionOnMap, attack=True):
		'''
		攻击移动前往坐标
		:param postionOnMap:
		:return:
		'''
		if attack:
			key = 'A'
			self.keyboardCommand(key, Down=True)
			self.mouseCommand(postionOnMap[0], postionOnMap[1], liftClick=True)
			self.keyboardCommand(key, Up=True)
		else:
			self.mouseCommand(postionOnMap[0], postionOnMap[1], rightClick=True)

	def keyboardCommand(self, keyChar, delay=100, Down=False, Up=False):
		mathodName = 'KeyPressChar'

		if Down:
			mathodName = 'KeyDownChar'
		if Up:
			mathodName = 'KeyUpChar'

		# print('keyboardCommand mathod:{} key:{} delay={}'.format(mathodName,keyChar,delay))
		command = {
			'name': mathodName,
			'key': keyChar,
			'delay': delay
		}
		self.excuteCommand(command)


	def mouseCommand(self, x=-1, y=-1, liftClick=False, rightClick=False, delay=100):
		'''
		:param x: -1==NoMove
		:param y: -1==NoMove
		:param liftClick:
		:param rightClick:
		:param delay:
		:return:
		'''
		# print('mouseCommand x:{} y:{} liftClick:{} rightClick:{} delay={}'.format(x,y,liftClick,rightClick,delay))
		if x != -1 and y != -1:
			mathodName = 'MoveTo'
			command = {
				'name': mathodName,
				'x': int(x),
				'y': int(y),
				'delay': delay
			}
			self.excuteCommand(command)

		mathodName = ''
		if liftClick:
			mathodName = 'LeftClick'
		if rightClick:
			mathodName = 'RightClick'
		if mathodName == '':
			return
		command = {
			'name': mathodName,
			'delay': delay
		}
		self.excuteCommand(command)

	def excuteCommand(self, commandDict):
		#print(commandDict)
		if self.test:
			return
		# 执行命令模块
		key = commandDict.get('key', '')
		x = commandDict.get('x', '')
		y = commandDict.get('y', '')
		delay = commandDict.get('delay', 100)
		name = commandDict.get('name', '')
		if name == '':
			return
		mathod = 'self.{}'.format(name)
		args = ''
		for arg in [key, x, y]:
			if arg != '':
				if args == '':
					args += '('
				else:
					args += ','
				args += '\'' + str(arg) + '\''
		if args == '':
			args = '()'
		else:
			args += ')'
		command = mathod + args
		try:
			print('excute command:{}'.format(command))
			eval(command)
			#time.sleep(delay / 1000)
		except Exception as e:
			print(e)
		finally:
			pass


if __name__ == "__main__":
	p = operater(1)
	p.keyboardCommand('a', Down=True)
	p.mouseCommand(619, 425, liftClick=True)
	p.keyboardCommand('a', Up=True)
	p.sendCommand()
