from abc import abstractmethod
import re
from unicodedata import normalize

from google.appengine.ext.ndb.key import Key


class Service(object):
	def __init__(self):
		self._punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

	@abstractmethod
	def create(self, form):
		pass

	@abstractmethod
	def update(self, key, form):
		pass

	@abstractmethod
	def get(self, key):
		pass

	@abstractmethod
	def delete(self, key):
		pass

	@staticmethod
	def get_by_urlsafe_key(key):
		entity = Key(urlsafe=key)
		return entity.get()

	@staticmethod
	def to_key(urlsafe):
		return Key(urlsafe=urlsafe)

	@staticmethod
	def get_all(qry, **kwargs):
		if 'filter' in kwargs:
			for f in kwargs['filter']:
				qry = qry.filter(f)
		if 'sort' in kwargs:
			for s in kwargs['sort']:
				qry.order(s)
		return qry.fetch()

	def slugify(self, text, delim=u'-'):
		"""Generates an slightly worse ASCII-only slug."""
		result = []
		for word in self._punct_re.split(text.lower()):
			word = normalize('NFKD', word).encode('ascii', 'ignore')
			if word:
				result.append(word)
		return unicode(delim.join(result))
