# NotificationRuleTemplateApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get**](NotificationRuleTemplateApi.md#get) | **GET** /notificationruletemplates/{webId} | Get the specified notification rule template.
[**get_notification_rule_template_subscribers**](NotificationRuleTemplateApi.md#getnotificationruletemplatesubscribers) | **GET** /notificationruletemplates/{webId}/notificationrulesubscribers | Retrieve notification rule template subscribers.
[**get_notification_rule_templates_query**](NotificationRuleTemplateApi.md#getnotificationruletemplatesquery) | **GET** /notificationruletemplates/search | Retrieve Notification rule templates based on the specified conditions. Returns Notification rule templates using the specified search query string.


# **get**
> get('web_id', 'selected_fields', 'web_id_type')

Get the specified notification rule template.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the notification rule template.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **web_id_type** | **str**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item "WebIDType".. | [optional]


### Return type

[**PINotificationRuleTemplate**](../models/PINotificationRuleTemplate.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_notification_rule_template_subscribers**
> get_notification_rule_template_subscribers('web_id', 'selected_fields', 'web_id_type')

Retrieve notification rule template subscribers.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the resource to use as the root of the search.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **web_id_type** | **str**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item "WebIDType".. | [optional]


### Return type

[**PIItemsNotificationRuleSubscriber**](../models/PIItemsNotificationRuleSubscriber.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_notification_rule_templates_query**
> get_notification_rule_templates_query('database_web_id', 'max_count', 'query', 'selected_fields', 'start_index', 'web_id_type')

Retrieve Notification rule templates based on the specified conditions. Returns Notification rule templates using the specified search query string.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **database_web_id** | **str**| The ID of the asset database to use as the root of the query.. | [optional]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **query** | **str**| The query string is a list of filters used to perform an AFSearch for the Notification rule templates in the asset database. An example would be: "query=NotificationRuleTemplate:{ Name:='MyNotificationRuleTemplate' } Type:=Int32".. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]
 **web_id_type** | **str**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item "WebIDType".. | [optional]


### Return type

[**PIItemsNotificationRuleTemplate**](../models/PIItemsNotificationRuleTemplate.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
