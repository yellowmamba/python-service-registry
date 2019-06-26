class GlobalRegistry:

	registry = {}

	@classmethod
	def register(cls, name="default", func=None):
		cls.registry[name] = func

	@classmethod
	def list(cls):
		return cls.registry

	@classmethod
	def dispatch(cls, name="default"):
		return cls.registry[name]