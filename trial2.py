import gym
import random
import numpy as np
from keras.models     import Sequential
from keras.layers     import Dense
from keras.optimizers import Adam

env = gym.make('CartPole-v1')
env.reset()
goal_steps = 500
score_requirement = 60
initial_games = 10000

def model_data_preparation():
    # Collect data and scores
    training_data = []
    accepted_scores = []

    # Play a bunch of times
    for game_index in range(initial_games):

        # Initialize stuff
        score = 0
        game_memory = []
        previous_observation = []

        # Take 500 steps to complete each game
        for step_index in range(goal_steps):
            action = random.randrange(0, 2) # Randomly go left or right
            observation, reward, done, info = env.step(action)
            
            if len(previous_observation) > 0:
                game_memory.append([previous_observation, action])
                
            previous_observation = observation
            score += reward
            if done:
                break
            
        # If successful, append to training_data
        if score >= score_requirement:
            accepted_scores.append(score)
            for data in game_memory:
                if data[1] == 1:
                    output = [0, 1] # right
                elif data[1] == 0:
                    output = [1, 0] # left

                # data[0] is prev_observation
                training_data.append([data[0], output])
        
        env.reset() # start playing new game

    print(accepted_scores)
    
    return training_data

def build_model(input_size, output_size):
    model = Sequential()
    model.add(Dense(128, input_dim=input_size, activation='relu'))
    model.add(Dense(52, activation='relu'))
    model.add(Dense(output_size, activation='linear'))
    model.compile(loss='mse', optimizer=Adam())

    return model

def train_model(training_data):
    X = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0])) # observations. 1 row per observation.
    y = np.array([i[1] for i in training_data]).reshape(-1, len(training_data[0][1])) # actions. 1 row per action.
    model = build_model(input_size=len(X[0]), output_size=len(y[0]))
    model.fit(X, y, epochs=10)

    return model


if __name__ == '__main__':
    # Get data and train model
    training_data = model_data_preparation()
    trained_model = train_model(training_data)

    # To accumulate scores and choices
    scores, choices = [], []

    for each_game in range(100):
        score = 0
        prev_obs = []
        
        # Play this game for 500 steps
        for step_index in range(goal_steps):
            env.render()

            if len(prev_obs) == 0:
                 # For first step, take random action
                action = random.randrange(0, 2)
            else:
                # As from 2nd step, ask model which action we should take
                # Put prev_obs in row form and predict
                pred = trained_model.predict(prev_obs.reshape(-1, len(prev_obs))) 
                # pred is a matrix with a single row. Check out that single row.
                action = np.argmax(pred[0])

            choices.append(action)
            new_observation, reward, done, info = env.step(action)
            prev_obs = new_observation

            score += reward
            if done:
                break

        # Make a new game
        env.reset()
        scores.append(score)
        print("Finished game", each_game)

    print(scores)
    print('Average score:', sum(scores)/len(scores))
    print('choice 1:{}  choice 0:{}'.format(choices.count(1)/len(choices),choices.count(0)/len(choices)))
