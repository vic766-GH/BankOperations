APILAYER_ERROR_CODE = {
    400:{"STATUS_CODE":"Bad Request",
         "EXPLANATION":"The request was unacceptable,often due to missing a required parameter."},
    401: {"STATUS_CODE" : "Unauthorized",
          "EXPLANATION":"No valid API key provided."},
    404: {"STATUS_CODE" : "Not Found",
          "EXPLANATION":"The requested resource doesn't exist."},
    429: {"STATUS_CODE" : "Too many requests",
          "EXPLANATION":"API request limit exceeded. See section Rate Limiting for more info."},
    500: {"STATUS_CODE" : "Server Error",
          "EXPLANATION":"We have failed to process your request. (You can contact us anytime)"}
}
