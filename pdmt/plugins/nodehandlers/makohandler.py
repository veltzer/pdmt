import pdmt.api
import pdmt.plugins.nodetypes.makofilenode
import pdmt.plugins.nodetypes.makotfilenode
import pdmt.config
import os.path # for join, basename

class NodeHandler(pdmt.api.NodeHandler):
	def respond(self,mgr,node,eventtype):
		if eventtype!='nodepostadd':
			return
		if not isinstance(node,pdmt.plugins.nodetypes.makofilenode.NodeType):
			return
		name=node.name[:node.name.rfind(pdmt.config.ns_makohandler.p_sourcefilesuffix)]
		newname=os.path.join(pdmt.config.ns_makohandler.p_targetdir,os.path.basename(name))
		#newname=node.name[:node.name.rfind(pdmt.config.ns_makohandler.p_sourcefilesuffix)]
		newnode=pdmt.plugins.nodetypes.makotfilenode.NodeType(name=newname)
		mgr.addNode(newnode)
		mgr.addEdge((newnode,node))
