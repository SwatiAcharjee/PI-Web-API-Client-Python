# NotificationRuleApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_notification_rules**](NotificationRuleApi.md#getnotificationrules) | **GET** /notificationrules/{webId} | Retrieve a notification rule.
[**get_notification_rule_subscribers**](NotificationRuleApi.md#getnotificationrulesubscribers) | **GET** /notificationrules/{webId}/notificationrulesubscribers | Retrieve notification rule subscribers.
[**get_notification_rules_query**](NotificationRuleApi.md#getnotificationrulesquery) | **GET** /notificationrules/search | Retrieve notification rules based on the specified conditions. Returns notification rules using the specified search query string.


# **get_notification_rules**
> get_notification_rules('web_id', 'selected_fields', 'web_id_type')

Retrieve a notification rule.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the resource to use as the root of the search.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **web_id_type** | **str**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item "WebIDType".. | [optional]


### Return type

[**PINotificationRule**](../models/PINotificationRule.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_notification_rule_subscribers**
> get_notification_rule_subscribers('web_id', 'selected_fields', 'web_id_type')

Retrieve notification rule subscribers.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the resource to use as the root of the search.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **web_id_type** | **str**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item "WebIDType".. | [optional]


### Return type

[**PIItemsNotificationRuleSubscriber**](../models/PIItemsNotificationRuleSubscriber.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_notification_rules_query**
> get_notification_rules_query('database_web_id', 'max_count', 'query', 'selected_fields', 'start_index', 'web_id_type')

Retrieve notification rules based on the specified conditions. Returns notification rules using the specified search query string.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **database_web_id** | **str**| The ID of the asset database to use as the root of the query.. | [optional]
 **max_count** | **int**| The maximum number of objects to be returned per call (page size). The default is 1000.. | [optional]
 **query** | **str**| The query string is a list of filters used to perform an AFSearch for the Notification rules in the asset database. An example would be: "query=Name:=MyNotificationRule* Template:=NoteRuleTemplate*".. | [optional]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **start_index** | **int**| The starting index (zero based) of the items to be returned. The default is 0.. | [optional]
 **web_id_type** | **str**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item "WebIDType".. | [optional]


### Return type

[**PIItemsNotificationRule**](../models/PIItemsNotificationRule.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
