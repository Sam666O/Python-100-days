"""
Python 3.9 стартовая программа на Python по изучению обучения с подкреплением - Reinforcement Learning
Название файла 00. start.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2021-12-19

воспользуемся одной из тестовых игр OpenAI, в частности, со средой «MountainCar-v0»
"""
import gym  # библиотека OpenAI с простыми играми

env = gym.make("MountainCar-v0")  # обращаемся к виртуальной среде (инициализировать среду)
env.reset()  # В случае с этим тренажерным залом наблюдения возвращаются из сбросов и шагов.

print(env.action_space.n)  # Для различных сред мы можем запросить у них, сколько действий / ходов возможно?
# В этом случае мы можем передать «3» действия. Это означает, что когда мы шагаем по среде, мы можем передавать 0,
# 1 или 2 в качестве нашего «действия» для каждого шага. Каждый раз, когда мы это делаем, среда будет возвращать нам
# новое состояние, награду, независимо от того, завершена / завершена среда, а затем любую дополнительную информацию,
# которая может быть у некоторых env.
# 0 означает толчок влево, 1 - оставаться на месте, а 2 - толкать вправо.


print(env.reset())  # Вы получите что-то вроде того [-0.4826636 0. ], что является начальным состоянием наблюдения.

done = False
while not done:
    action = 2  # always go right! 0 означает толчок влево, 1 - оставаться на месте, а 2 - толкать вправо.
    env.step(action)
    env.render()

# Как видите, несмотря на то, что эту машину постоянно просят ехать направо, мы видим, что у нее просто нет сил,
# чтобы это сделать. Вместо этого нам нужно на самом деле набрать обороты, чтобы достичь этого флага. Для этого нам
# нужно двигаться взад и вперед, чтобы набрать обороты. Мы могли бы запрограммировать функцию, которая будет
# выполнять эту задачу за нас, или мы можем использовать Q-обучение для ее решения!

