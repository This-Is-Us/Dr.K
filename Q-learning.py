#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random

# Build Q-table
q = np.zeros((6, 6))
q = np.matrix(q)

# Build R-table
r = np.array([[-1, -1, -1, -1, 0, -1], [-1, -1, -1, 0, -1, 100], [-1, -1, -1, 0, -1, -1], [-1, 0, 0, -1, 0, -1],
              [0, -1, -1, 0, -1, 100], [-1, 0, -1, -1, 0, 100]])
r = np.matrix(r)

# Discount factor
gamma = 0.8

# Training
for i in range(1000):
    # For each training episode, randomly select a state
    state = random.randint(0, 5)
    while state != 5:
        # Select the action of a non-negative value in the R-table
        r_pos_action = []
        for action in range(6):
            if r[state, action] >= 0:
                r_pos_action.append(action)
        next_state = r_pos_action[random.randint(0, len(r_pos_action) - 1)]
        q[state, next_state] = r[state, next_state] + gamma * q[next_state].max()
        state = next_state

print('Finally, the content of Q-table is:\n')
print(q)

# verification
for i in range(10):
    print("\n{}-th verification:".format(i + 1))
    state = random.randint(0, 5)
    print('The robot is at {}'.format(state))
    count = 0
    while state != 5:
        if count > 20:
            print('fail')
            break
        # Choose the largest q_max
        q_max = q[state].max()

        q_max_action = []
        for action in range(6):
            if q[state, action] == q_max:
                q_max_action.append(action)

        next_state = q_max_action[random.randint(0, len(q_max_action) - 1)]
        print("the robot goes to " + str(next_state) + '.')
        state = next_state
        count += 1


# In[ ]:




