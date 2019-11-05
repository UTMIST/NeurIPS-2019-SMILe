from utils import sample_context


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

