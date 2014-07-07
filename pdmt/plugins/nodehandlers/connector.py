import pdmt.api # for NodeHandler, Event.nodepostadd
import re # for compile

"""
This is a node connector. It listens for Event.nodepostadd events
and connects nodes that match a regualr expression to the node
given to it at construction.

TODO: It should also listen for the removal of the node given to it
and remove itself when it is removed.
"""
class NodeHandler(pdmt.api.NodeHandler):
	def __init__(self,cnode=None,type=None,regexp=None):
		self.cnode=cnode
		self.type=type
		self.regexp=regexp
		if self.regexp is not None:
			self.regexp=re.compile(self.regexp)
	def respond(self,mgr,node,eventtype):
		if eventtype!=pdmt.api.Event.nodepostadd:
			return
		if self.type is not None and not isinstance(node,self.type):
			return
		if self.regexp is not None and not self.regexp.match(node.name):
			return
		mgr.addEdge((self.cnode,node))
