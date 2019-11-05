import torch
import gym


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


def UpdateDiscriminator():
	"""Algorithm 2"""

	tasks_batch = []
	# Get a context for every task.  Corresponds to the for-loop in Algo2
	contexts = [sample_context(task) for task in tasks_batch] 

	# Sample M transitions per task.  Not sure how to do that yet.
	transitions_expert = []
	transitions_replay_buffers = []

	# The 2 variables below should be tensors
	L_disc = -1 # Discriminator objective
	L_GP = -1 # Regularization term

	# Need to look at what are psi and phi.  They're probably standard stuff in
	# RL.
	lambda_GP = 10

	# These 5 should be tensors
	grad_psi_L_disc, grad_psi_L_GP, grad_phi_L_disc = -1, -1, -1 
	psi, phi = -1, -1
	# Learning rate
	alpha_psi, alpha_phi = -1, -1

	psi -= alpha_psi * (grad_psi_L_disc + lambda_GP * grad_psi_L_GP)
	phi -= alpha_phi * grad_phi_L_disc


def UpdatePolicy():
	"""Algorithm 3"""

	tasks_batch = []
	# Get a context for every task
	contexts = [sample_context(task) for task in tasks_batch] 

	# Sample M transitions (s, a, s', terminal) per task from the task replay buffers
	transitions = []  

	for trans in transitions:
		r = -1 # The log formula
		# Add/append the r to something

	# Still don't get the last line in Algo3

# HELPERS -----------------------------------------------
def get_env(task):
	pass

def sample_context(task):
	pass