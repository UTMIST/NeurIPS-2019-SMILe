import torch
import gym
from utils import get_env, sample_context
from Algo2 import UpdateDiscriminator
from Algo3 import UpdatePolicy

def SMILe():
	"""Algorithm 1"""
	meta_policy = -1 # Not sure what kind of object this is
	meta_discriminator = -1 # Same
	context_encoder = -1 # Don't know how to encode yet
	meta_training_tasks = []

	expert_demonstrations = [] # Get them from Soft-Actor-Critic
	task_replay_buffers = []

	j = -1
	# Populate buffers with initial rollouts
	for task in meta_training_tasks:
		for _ in range(j):
			env = get_env(task)
			context = sample_context(task)
			# Do rollout
			# Add rollout to replay buffer

	# Train loop
	converged = False
	m, d = -1, -1
	while not converged:
		for _ in range(m):
			task = -1 # Just use a torch method to uniformly sample from meta_training_tasks
			env = get_env(task)
			context = sample_context(task)
			# Do rollout
			# Add rollout to replay buffer

		for _ in range(d):
			UpdateDiscriminator()
			UpdatePolicy()

		# Need to figure out this condition
		if True:
			converged = True
