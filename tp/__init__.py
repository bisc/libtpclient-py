__import__('pkg_resources').declare_namespace(__name__)
try:
	import modulefinder
	for p in __path__:
		modulefinder.AddPackagePath(__name__, p)
except Exception, e:
	import warnings
	warnings.warn(e, RuntimeWarning)
