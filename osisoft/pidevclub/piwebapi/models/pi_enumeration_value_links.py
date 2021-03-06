# coding: utf-8

"""
	Copyright 2018 OSIsoft, LLC
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
	
	  <http://www.apache.org/licenses/LICENSE-2.0>
	
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
"""
from pprint import pformat
from six import iteritems


class PIEnumerationValueLinks(object):
	swagger_types = {
		'enumeration_set': 'str',
		'parent': 'str',
	}

	attribute_map = {
		'enumeration_set': 'EnumerationSet',
		'parent': 'Parent',
	}
	def __init__(self, enumeration_set=None, parent=None):

		self._enumeration_set = None
		self._parent = None

		if enumeration_set is not None:
			self.enumeration_set = enumeration_set
		if parent is not None:
			self.parent = parent

	@property
	def enumeration_set(self):
		return self._enumeration_set

	@enumeration_set.setter
	def enumeration_set(self, enumeration_set):
		self._enumeration_set = enumeration_set

	@property
	def parent(self):
		return self._parent

	@parent.setter
	def parent(self, parent):
		self._parent = parent

	def to_dict(self):
		result = {}
		for attr, _ in iteritems(self.swagger_types):
			value = getattr(self, attr)
			if isinstance(value, list):
				result[attr] = list(map(
					lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
					value
				))
			elif hasattr(value, "to_dict"):
				result[attr] = value.to_dict()
			elif isinstance(value, dict):
				result[attr] = dict(map(
					lambda item: (item[0], item[1].to_dict())
					if hasattr(item[1], "to_dict") else item,
					value.items()
				))
			else:
				result[attr] = value
		return result

	def to_str(self):
		return pformat(self.to_dict())

	def __repr__(self):
		return self.to_str()

	def __ne__(self, other):
		return not self == other

	def __eq__(self, other):
		if not isinstance(other, PIEnumerationValueLinks):
			return False
		return self.__dict__ == other.__dict__

