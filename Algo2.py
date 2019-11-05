from utils import sample_context

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