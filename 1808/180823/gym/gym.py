import gym

env = gym.make('MountainCar-v0')

observation = env.reset()

action = 0
observation, reward, done, info = env.step(action)


print(observation)

env.render()
print(ervation_space.low)
print(env.observation_space.high)


