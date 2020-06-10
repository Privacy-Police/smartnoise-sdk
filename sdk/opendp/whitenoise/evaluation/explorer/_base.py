from opendp.whitenoise.evaluation.metrics._metrics import Metrics
from opendp.whitenoise.evaluation.params._halton_params import HaltonParams

class ExplorerInterface:
	"""
	DP evaluator can be invoked with various evaluation parameters
	For example, for a SQL analysis, we can pass various datasets and 
	queries to see if the evaluator metrics are successful. This interface
	helps provide capability to do brute force generation of neighboring 
	datasets.
	"""
	def evaluate_powerset(self, dataset : object) -> Metrics:
		"""
		Explores powerset of a given dataset
		"""
		pass
		
	def generate_halton(self, halton_params : HaltonParams) -> [object]:
		"""
		Generate new datasets using halton sequence. Calls the powerset explore
		"""
		pass