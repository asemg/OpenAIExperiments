import gym
import sys

env = gym.make(sys.argv[1])
env.reset()

while True:
    env.render()
    env.step(env.action_space.sample()) # 