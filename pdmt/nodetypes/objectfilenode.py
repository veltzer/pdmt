import pdmt.nodetypes.buildfilenode
import pdmt.nodetypes.cfilenode
import pdmt.utils.subproc
import pdmt.types

class NodeType(pdmt.nodetypes.buildfilenode.NodeType):
	def __init__(self,p_fname):
		super().__init__(p_fname,pdmt.types.t_object)
	def build(self):
		args=[]
		args.append('gcc')
		args.append('-c')
		args.append('-o')
		args.append(self.m_fname)
		for node in self.getSourcesOfType(pdmt.nodetypes.cfilenode.NodeType):
			args.append(node.m_fname)
		pdmt.utils.subproc.check_call(args)
