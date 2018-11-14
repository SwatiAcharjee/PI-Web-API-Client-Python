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


class PINotificationRuleTemplate(object):
	swagger_types = {
		'web_id': 'str',
		'id': 'str',
		'name': 'str',
		'description': 'str',
		'path': 'str',
		'category_names': 'list[str]',
		'criteria': 'str',
		'multi_trigger_event_option': 'str',
		'nonrepetition_interval': 'str',
		'resend_interval': 'str',
		'status': 'str',
		'template_name': 'str',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'web_id': 'WebId',
		'id': 'Id',
		'name': 'Name',
		'description': 'Description',
		'path': 'Path',
		'category_names': 'CategoryNames',
		'criteria': 'Criteria',
		'multi_trigger_event_option': 'MultiTriggerEventOption',
		'nonrepetition_interval': 'NonrepetitionInterval',
		'resend_interval': 'ResendInterval',
		'status': 'Status',
		'template_name': 'TemplateName',
		'web_exception': 'WebException',
	}
	def __init__(self, web_id=None, id=None, name=None, description=None, path=None, category_names=None, criteria=None, multi_trigger_event_option=None, nonrepetition_interval=None, resend_interval=None, status=None, template_name=None, web_exception=None):

		self._web_id = None
		self._id = None
		self._name = None
		self._description = None
		self._path = None
		self._category_names = None
		self._criteria = None
		self._multi_trigger_event_option = None
		self._nonrepetition_interval = None
		self._resend_interval = None
		self._status = None
		self._template_name = None
		self._web_exception = None

		if web_id is not None:
			self.web_id = web_id
		if id is not None:
			self.id = id
		if name is not None:
			self.name = name
		if description is not None:
			self.description = description
		if path is not None:
			self.path = path
		if category_names is not None:
			self.category_names = category_names
		if criteria is not None:
			self.criteria = criteria
		if multi_trigger_event_option is not None:
			self.multi_trigger_event_option = multi_trigger_event_option
		if nonrepetition_interval is not None:
			self.nonrepetition_interval = nonrepetition_interval
		if resend_interval is not None:
			self.resend_interval = resend_interval
		if status is not None:
			self.status = status
		if template_name is not None:
			self.template_name = template_name
		if web_exception is not None:
			self.web_exception = web_exception

	@property
	def web_id(self):
		return self._web_id

	@web_id.setter
	def web_id(self, web_id):
		self._web_id = web_id

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def description(self):
		return self._description

	@description.setter
	def description(self, description):
		self._description = description

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, path):
		self._path = path

	@property
	def category_names(self):
		return self._category_names

	@category_names.setter
	def category_names(self, category_names):
		self._category_names = category_names

	@property
	def criteria(self):
		return self._criteria

	@criteria.setter
	def criteria(self, criteria):
		self._criteria = criteria

	@property
	def multi_trigger_event_option(self):
		return self._multi_trigger_event_option

	@multi_trigger_event_option.setter
	def multi_trigger_event_option(self, multi_trigger_event_option):
		self._multi_trigger_event_option = multi_trigger_event_option

	@property
	def nonrepetition_interval(self):
		return self._nonrepetition_interval

	@nonrepetition_interval.setter
	def nonrepetition_interval(self, nonrepetition_interval):
		self._nonrepetition_interval = nonrepetition_interval

	@property
	def resend_interval(self):
		return self._resend_interval

	@resend_interval.setter
	def resend_interval(self, resend_interval):
		self._resend_interval = resend_interval

	@property
	def status(self):
		return self._status

	@status.setter
	def status(self, status):
		self._status = status

	@property
	def template_name(self):
		return self._template_name

	@template_name.setter
	def template_name(self, template_name):
		self._template_name = template_name

	@property
	def web_exception(self):
		return self._web_exception

	@web_exception.setter
	def web_exception(self, web_exception):
		self._web_exception = web_exception

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
		if not isinstance(other, PINotificationRuleTemplate):
			return False
		return self.__dict__ == other.__dict__

