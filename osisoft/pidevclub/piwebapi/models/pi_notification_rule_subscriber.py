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


class PINotificationRuleSubscriber(object):
	swagger_types = {
		'web_id': 'str',
		'id': 'str',
		'name': 'str',
		'description': 'str',
		'path': 'str',
		'config_string': 'str',
		'contact_template_name': 'str',
		'contact_type': 'str',
		'delivery_format_name': 'str',
		'plug_in_name': 'str',
		'escalation_timeout': 'str',
		'maximum_retries': 'int',
		'notify_option': 'str',
		'retry_interval': 'str',
		'web_exception': 'PIWebException',
	}

	attribute_map = {
		'web_id': 'WebId',
		'id': 'Id',
		'name': 'Name',
		'description': 'Description',
		'path': 'Path',
		'config_string': 'ConfigString',
		'contact_template_name': 'ContactTemplateName',
		'contact_type': 'ContactType',
		'delivery_format_name': 'DeliveryFormatName',
		'plug_in_name': 'PlugInName',
		'escalation_timeout': 'EscalationTimeout',
		'maximum_retries': 'MaximumRetries',
		'notify_option': 'NotifyOption',
		'retry_interval': 'RetryInterval',
		'web_exception': 'WebException',
	}
	def __init__(self, web_id=None, id=None, name=None, description=None, path=None, config_string=None, contact_template_name=None, contact_type=None, delivery_format_name=None, plug_in_name=None, escalation_timeout=None, maximum_retries=None, notify_option=None, retry_interval=None, web_exception=None):

		self._web_id = None
		self._id = None
		self._name = None
		self._description = None
		self._path = None
		self._config_string = None
		self._contact_template_name = None
		self._contact_type = None
		self._delivery_format_name = None
		self._plug_in_name = None
		self._escalation_timeout = None
		self._maximum_retries = None
		self._notify_option = None
		self._retry_interval = None
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
		if config_string is not None:
			self.config_string = config_string
		if contact_template_name is not None:
			self.contact_template_name = contact_template_name
		if contact_type is not None:
			self.contact_type = contact_type
		if delivery_format_name is not None:
			self.delivery_format_name = delivery_format_name
		if plug_in_name is not None:
			self.plug_in_name = plug_in_name
		if escalation_timeout is not None:
			self.escalation_timeout = escalation_timeout
		if maximum_retries is not None:
			self.maximum_retries = maximum_retries
		if notify_option is not None:
			self.notify_option = notify_option
		if retry_interval is not None:
			self.retry_interval = retry_interval
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
	def config_string(self):
		return self._config_string

	@config_string.setter
	def config_string(self, config_string):
		self._config_string = config_string

	@property
	def contact_template_name(self):
		return self._contact_template_name

	@contact_template_name.setter
	def contact_template_name(self, contact_template_name):
		self._contact_template_name = contact_template_name

	@property
	def contact_type(self):
		return self._contact_type

	@contact_type.setter
	def contact_type(self, contact_type):
		self._contact_type = contact_type

	@property
	def delivery_format_name(self):
		return self._delivery_format_name

	@delivery_format_name.setter
	def delivery_format_name(self, delivery_format_name):
		self._delivery_format_name = delivery_format_name

	@property
	def plug_in_name(self):
		return self._plug_in_name

	@plug_in_name.setter
	def plug_in_name(self, plug_in_name):
		self._plug_in_name = plug_in_name

	@property
	def escalation_timeout(self):
		return self._escalation_timeout

	@escalation_timeout.setter
	def escalation_timeout(self, escalation_timeout):
		self._escalation_timeout = escalation_timeout

	@property
	def maximum_retries(self):
		return self._maximum_retries

	@maximum_retries.setter
	def maximum_retries(self, maximum_retries):
		self._maximum_retries = maximum_retries

	@property
	def notify_option(self):
		return self._notify_option

	@notify_option.setter
	def notify_option(self, notify_option):
		self._notify_option = notify_option

	@property
	def retry_interval(self):
		return self._retry_interval

	@retry_interval.setter
	def retry_interval(self, retry_interval):
		self._retry_interval = retry_interval

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
		if not isinstance(other, PINotificationRuleSubscriber):
			return False
		return self.__dict__ == other.__dict__

