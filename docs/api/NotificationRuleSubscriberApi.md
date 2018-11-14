# NotificationRuleSubscriberApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get_notification_rule_subscriber_by_path**](NotificationRuleSubscriberApi.md#getnotificationrulesubscriberbypath) | **GET** /notificationrulesubscribers | Retrieve a notification rule subscriber by path.
[**get_notification_rule_subscriber**](NotificationRuleSubscriberApi.md#getnotificationrulesubscriber) | **GET** /notificationrulesubscribers/{webId} | Retrieve a notification rule subscriber.
[**get_notification_rule_subscribers**](NotificationRuleSubscriberApi.md#getnotificationrulesubscribers) | **GET** /notificationrulesubscribers/{webId}/notificationrulesubscribers | Retrieve notification rule subscriber subscribers.


# **get_notification_rule_subscriber_by_path**
> get_notification_rule_subscriber_by_path('path', 'selected_fields', 'web_id_type')

Retrieve a notification rule subscriber by path.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path to the notification rule subscriber.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **web_id_type** | **str**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item "WebIDType".. | [optional]


### Return type

[**PINotificationRuleSubscriber**](../models/PINotificationRuleSubscriber.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_notification_rule_subscriber**
> get_notification_rule_subscriber('web_id', 'selected_fields', 'web_id_type')

Retrieve a notification rule subscriber.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the resource to use as the root of the search.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **web_id_type** | **str**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item "WebIDType".. | [optional]


### Return type

[**PINotificationRuleSubscriber**](../models/PINotificationRuleSubscriber.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)

# **get_notification_rule_subscribers**
> get_notification_rule_subscribers('web_id', 'selected_fields', 'web_id_type')

Retrieve notification rule subscriber subscribers.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the resource to use as the root of the search.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **web_id_type** | **str**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item "WebIDType".. | [optional]


### Return type

[**PIItemsNotificationRuleSubscriber**](../models/PIItemsNotificationRuleSubscriber.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
