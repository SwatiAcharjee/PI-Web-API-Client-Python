# NotificationContactTemplateApi

Method | HTTP request | Description
------------ | ------------- | -------------
[**get**](NotificationContactTemplateApi.md#get) | **GET** /notificationcontacttemplates/{webId} | Retrieve a notification contact template.


# **get**
> get('web_id', 'selected_fields', 'web_id_type')

Retrieve a notification contact template.

### Parameters

Name | Type | Description | Notes
------------- | ------------- | ------------- | -------------
 **web_id** | **str**| The ID of the notification contact template.. | [required]
 **selected_fields** | **str**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.. | [optional]
 **web_id_type** | **str**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item "WebIDType".. | [optional]


### Return type

[**PINotificationContactTemplate**](../models/PINotificationContactTemplate.md)

[[Back to top]](#) [[Back to API list]](../../DOCUMENTATION.md#documentation-for-api-endpoints) [[Back to Model list]](../../DOCUMENTATION.md#documentation-for-models) [[Back to DOCUMENTATION]](../../DOCUMENTATION.md)
