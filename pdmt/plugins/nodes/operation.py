import pdmt.api # for NodeType

'''
This node represents an operation.
An operation is something that needs to run but does not depend on anything
'''

class NodeType(pdmt.api.NodeType):
	def __init__(self, name=None, description=None):
		super().__init__(name=name, proto='op')
		self.description=description
	def needbuild(self,todo):
		return True
	def canBuild(self):
		return True
	def canClean(self):
		return False
	def clean(self):
		pass
