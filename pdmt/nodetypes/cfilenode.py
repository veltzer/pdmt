import pdmt.nodetypes.sourcefilenode
import pdmt.types

"""
This node represents C source code
"""

class CFileNode(pdmt.nodetypes.sourcefilenode.SourceFileNode):
	def __init__(self,fname):
		super(CFileNode,self).__init__(fname,pdmt.types.t_c)
