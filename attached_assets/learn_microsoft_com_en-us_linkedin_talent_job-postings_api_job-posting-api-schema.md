URL: https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema
---
[Skip to main content](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#main)

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

[Download Microsoft Edge](https://go.microsoft.com/fwlink/p/?LinkID=2092881) [More info about Internet Explorer and Microsoft Edge](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge)

Table of contentsExit focus mode

[Read in English](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema "Read in English")Save

- Add to Collections
- Add to plan

[Edit This Document](https://github.com/MicrosoftDocs/linkedin-api-docs/blob/live/linkedin-api-docs/talent/job-postings/api/job-posting-api-schema.md "Edit This Document")

Table of contents [Read in English](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema "Read in English")Add to CollectionsAdd to plan[Edit](https://github.com/MicrosoftDocs/linkedin-api-docs/blob/live/linkedin-api-docs/talent/job-postings/api/job-posting-api-schema.md "Edit This Document")

* * *

#### Share via

[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fjob-posting-api-schema%3FWT.mc_id%3Dfacebook) [x.com](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fjob-posting-api-schema%3FWT.mc_id%3Dtwitter&text=Today%20I%20completed%20%22Job%20Posting%20Schema%20-%20LinkedIn%20%7C%20Microsoft%20Learn%22!%20I%27m%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!&tw_p=tweetbutton&url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fjob-posting-api-schema%3FWT.mc_id%3Dtwitter) [LinkedIn](https://www.linkedin.com/feed/?shareActive=true&text=Today%20I%20completed%20%22Job%20Posting%20Schema%20-%20LinkedIn%20%7C%20Microsoft%20Learn%22!%20I%27m%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fjob-posting-api-schema%3FWT.mc_id%3Dlinkedin) [Email](mailto:?subject=%5BShared%20Article%5D%20Job%20Posting%20Schema%20-%20LinkedIn%20%7C%20Microsoft%20Learn&body=Today%20I%20completed%20%22Job%20Posting%20Schema%20-%20LinkedIn%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fjob-posting-api-schema%3FWT.mc_id%3Demail)

* * *

Print

Table of contents

# Job Posting Schema

- Article
- 02/04/2025
- 9 contributors

Feedback

This document lists and describes the job fields supported by the Job Posting API.

[Section titled: Foundation Schema](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#foundation-schema)

## Foundation Schema

The schema below includes attributes required for posting jobs on LinkedIn. The foundation schema represents the core schema that has to be implemented irrespective of integration type. The partner needs to implement the Foundation schema and can also build any extension schema(s) which are defined in the topics below.

Expand table

| Field | Description | Type | Required |
| --- | --- | --- | --- |
| integrationContext | Represents the unique identifier of the company page on LinkedIn for which this job is posted. Must be in the format urn:li:organization:{ [company\_id](https://www.linkedin.com/help/linkedin/answer/a415420)} for example, `urn:li:organization:1234`. If the company is a LinkedIn customer with access to the [onboarding widget](https://learn.microsoft.com/en-us/linkedin/talent/apply-connect/customer-configuration), then this field must be used to identify the company, else use companyName field | URN | `integrationContext` is a recommended field and must be provided to ensure job postings get associated with correct company page. Provide companyName field value only if you cannot provide value for this field. However, this does not guarantee a 100% accurate match with LinkedIn company page |
| companyApplyUrl | URL for applicants to apply for the jobs | String | Yes |
| externalJobPostingId | Represents unique job id within the partner system. Do not send an empty or null string for this field. The maximum allowed length is 200 characters | String | Yes |
| jobPostingOperationType | Represents the operation on the job posting. Available operation options are: CREATE, UPDATE, RENEW, CLOSE | String | Yes |
| title | Represents the title of the job posting that will be published. Character limit: 200 | String | Yes |
| description | Represents the job description including the job basic information, responsibility and so on. Character limit: 100 ~ 25,000, limited set of [HTML tags](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#html-tags) accepted, non-support HTML tags will be ignored. | String | Yes |
| listedAt | Represents initial date the job posting was added into the application tracking system. The date is epoch timestamp in milliseconds (UTC) and should not be a future time | Integer | Yes |
| location | Represents the geographic location of the job position to hire. Please use one of the below recommended formats: <br>- "CITY, STATE, COUNTRY" <br>- "CITY, STATE"<br>- "CITY, PROVINCE"<br>- "CITY, COUNTRY" <br>- "POSTALCODE, COUNTRYCODE" <br>- "COUNTRY" (accepted only for Remote jobs) <br>- "COUNTRY CLUSTER" (accepted only for Remote jobs) <br> To know more about <br>- COUNTRY CLUSTER, refer to our [Help Article](https://www.linkedin.com/help/linkedin/answer/a524054). <br>- Best practices to use location field, refer to our [Help Article](https://www.linkedin.com/help/recruiter/answer/a478845?trk=partner-documentation). If your application is unable to match one of the suggested formats please provide the raw location details. | String | Yes |
| alternateLocations | Represents alternate locations for a job with multiple locations. This field takes the locations as input (including the one set in the `location` field). This field is null if the job has only one location. Maximum up to seven alternate locations are allowed. <br>- US locations - City <br>- Non-US locations - City, Country/Region (for example, “London, United Kingdom”) <br>_NOTE:_ Alternate locations are not supported for RSC and CRM Connect | String Array | Optional |
| categories | Represents job functions specific to this job (for example, Accounting, Marketing, Sales). Category names are predefined by LinkedIn and can be retrieved from [Job Functions](https://learn.microsoft.com/en-us/linkedin/shared/references/reference-tables/job-function-codes) reference table. You can provide upto 3 values. <br>- If predefined LinkedIn values are provided, they are displayed on the LinkedIn Job Posting <br>- If none of the values match our predefined LinkedIn values, we recommend partner to still provide raw values for offline processing. However, they may not be displayed on LinkedIn Job Posting. <br>- If no value is provided, then LinkedIn will infer a value by referencing other fields of the Job Posting | String Array | Yes, if available on career site. |
| skillsDescription | Represents description of desired skills and experiences of the job position. The maximum allowed length is 4000 characters. Limited set of HTML tags accepted (details below) | String | No |
| companyJobCode | Represents job posting id within the company’s system for reference. Should be used only when the unique ID for a job in your system is different from the unique ID of the job as in the customer's platform where the job originated. Do not send an empty or null string for this field | String | Yes, if available on career site. |
| workplaceTypes | Represents the workplace nature of the job. Available options are <br>- `On-site`<br>- `Hybrid`<br>- `Remote`<br> Remote value should be provided when employee is allowed to work remotely. Hybrid should be provided if the employee is expected to work some days from home and some days from the designated office. `On-Site` should be used when it is mandatory for employee to work only from the designated office. <br>- `Remote` jobs require either Country only, City and Country, or Country Cluster.<br>- For `On-site` and `Hybrid` jobs, `location` field should be in either of the following formats "CITY, STATE, COUNTRY", "CITY,STATE", "CITY, PROVINCE", "CITY, COUNTRY" or "POSTALCODE, COUNTRYCODE" <br>- It is recommended to default set the value of this field as `On-site`, if an employer is unsure about the workplace type of a particular job | Array of String. Currently accepts single element array with one of the following values `On-site`, `Hybrid`, `Remote` | Yes, if available on career site. |
| industries | Represents industries of this job or company. Array element must be quoted and in URN format: "urn:li:industry:{industry\_id}". Industry IDs are predefined by LinkedIn and can be retrieved from [Industry Codes](https://learn.microsoft.com/en-us/linkedin/shared/references/reference-tables/industry-codes) reference table.<br> Each company page on LinkedIn is linked to one or multiple industry codes. When posting a job on that company page, the job will default to the industry code(s) defined for the company. Providing an industry code in this field will override the industry code(s) defined on the company page for the job posting. The API will return an error if no industry code exists on the company page and one is not provided in the API request. | Array of Industry URN | No |
| employmentStatus | Represents employment status of the job position. Available options are: `FULL_TIME`, `PART_TIME`, `CONTRACT`, `INTERNSHIP`, `TEMPORARY`, `VOLUNTEER`. If predefined LinkedIn values are provided, they are displayed on the LinkedIn job posting. If a non-standard value is provided, LinkedIn attempts to standardize and match it to the closest pre-defined value. If no values are provided, LinkedIn standardizes to the closest matched value based on other fields in the job posting | String | Yes, if available on career site. |
| experienceLevel | Represents experience level of the job position to hire. Available options are: `ENTRY_LEVEL`, `MID_SENIOR_LEVEL`, `DIRECTOR`, `EXECUTIVE`, `INTERNSHIP`, `ASSOCIATE`, `NOT_APPLICABLE`. If predefined LinkedIn values are provided, they are displayed on the LinkedIn job posting. If a non-standard value is provided, LinkedIn attempts to standardize and match it to the closest pre-defined value. If no values are provided, LinkedIn standardizes to the closest matched value based on other fields in the job posting | String | Yes, if available on customer career sites. |
| trackingPixelUrl | URL for the tracking pixel to be embedded on the job description. To know more refer to [Help Article](https://www.linkedin.com/help/linkedin/answer/a412139) | String | No |
| companyName | The company name for which this job posting is created for. This field should be used in lieu of integrationContext only if the customer does not have contract with LinkedIn and cannot access the [Customer Onboarding Widget](https://learn.microsoft.com/en-us/linkedin/talent/apply-connect/customer-configuration) | String | Yes, if `integrationContext` or `companyPageUrl` is not available, and only if none of them is available. |
| companyPageUrl | The URL of the customer’s LinkedIn Company Page they would like their jobs posted to (e.g. [https://www.linkedin.com/company/{company\_page}/](https://www.linkedin.com/company/%7Bcompany_page%7D/)) | String | Yes, if `integrationContext` or `companyName` is unavailable. |
| compensation | Compensation provided by the job poster. | [PosterProvidedCompensation](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#poster-provided-compensation-schema) | No |
| expireAt | The date when a job should expire and no longer be available to users. This date should be greater than the current date. If this field is not provided, the default expiration is 180 days for basic and 30 days for premium jobs. For `PREMIUM` jobs, the expiration date must be within the range of 1 to 90 days, for invalid date API will return an "Invalid ExpirationDate" error. | Epoch in Milliseconds (UTC) | No |
| listingType | Represents the type of the job posting. Value of `PREMIUM` should be provided only if integration is build for [Premium Job Posting Extension schema](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#promoted-jobs-extension-schema). For everything else, value of this field should be `BASIC`. Default value is `BASIC`. | String | No |

[Section titled: Poster Provided Compensation Schema](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#poster-provided-compensation-schema)

## Poster Provided Compensation Schema

Expand table

| Field | Description | Type | Required |
| --- | --- | --- | --- |
| compensations | Compensation detail | Array of [compensation](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#compensation-schema) | Yes |

[Section titled: Compensation Schema](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#compensation-schema)

## Compensation Schema

Expand table

| Field | Description | Type | Required |
| --- | --- | --- | --- |
| amount | The amount of compensation. | [MoneyAmount](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#money-amount-schema) | No |
| value | The compensation amount, which may be either "range" or "exactAmount" | [MoneyAmountRange](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#money-amount-range-schema) | Yes |
| period | Period in which the amount of compensation is paid. Valid value is `YEARLY`, `MONTHLY`, `SEMIMONTHLY`, `BIWEEKLY`, `WEEKLY`, `DAILY`, `HOURLY` | String | Yes |
| type | Type of compensation, valid value are `BASE_SALARY`, `TIPS`, `COMMISSION`, `PROFIT_SHARING`, `STOCK_OPTIONS`, `STOCK`, `BONUS`, `SIGN_ON_BONUS`, `OVER_TIME`, `OTHER` | String | Yes |

[Section titled: Money Amount Schema](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#money-amount-schema)

## Money Amount Schema

Expand table

| Field | Description | Type | Required |
| --- | --- | --- | --- |
| currencyCode | ISO [currency code](https://learn.microsoft.com/en-us/linkedin/shared/references/reference-tables/currency-codes). | String | Yes |
| amount | The amount of money as a real number string | String | Yes |

[Section titled: Money Amount Range Schema](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#money-amount-range-schema)

## Money Amount Range Schema

Expand table

| Field | Description | Type | Required |
| --- | --- | --- | --- |
| start | Represents the inclusive (greater than or equal to) value in which to start the range. This field is optional. An unset field indicates an open range; for example, if end is 5, it means everything less than or equal to 5. | [MoneyAmount](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#money-amount-schema) | Yes |
| end | Represents the inclusive (less than or equal to) value in which to end the range. This field is optional. An unset field indicates an open range; for example if start is 2 it means everything greater than or equal to 2. | [MoneyAmount](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#money-amount-schema) | Yes |

[Section titled: Sample Request for compensation](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#sample-request-for-compensation)

## Sample Request for compensation

```lang-json
"compensation":{
    "compensations":[\
        {\
            "period":"YEARLY",\
            "type":"BASE_SALARY",\
            "value": {\
                "range": {\
                    "start":{"amount":"1234", "currencyCode":"USD"},\
                    "end":{"amount":"4567", "currencyCode":"USD"}\
                }\
            }\
        }\
    ]
}

```

```lang-json
"compensation":{
    "compensations":[\
        {\
            "period":"YEARLY",\
            "type":"BASE_SALARY",\
            "value": {\
                "exactAmount": {"amount":"4000", "currencyCode":"USD"}\
            }\
        }\
    ]
}

```

[Section titled: Promoted Jobs Extension Schema](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#promoted-jobs-extension-schema)

## Promoted Jobs Extension Schema

Includes additional attributes required or optional for [jobs promotion](https://learn.microsoft.com/en-us/linkedin/talent/premium-job-posting).

Expand table

| Field | Description | Type | Required |
| --- | --- | --- | --- |
| contract | Represents the contract this job posting is published to, which is signed by the customer with LinkedIn to use LinkedIn Recruiter services. Must be in the format urn:li:contract:{ [contractId](https://www.linkedin.com/help/recruiter/answer/a412381/finding-your-recruiter-contract-id?lang=en)} | Contract URN | Yes |
| posterEmail | Represents valid email address of the poster who will publish the job. Must be the primary email address of the seat holder as defined in the customer's contract. If not provided, the `defaultJobPoster` configured by the customer is used | String | No |
| showPosterInfo | Represents whether LinkedIn would display the poster information on job description page. The default value is false (No). For Basic jobs this only works if `posterEmail` is provided and can be associated to a contract seat holder | Boolean | No |

Note

It is mandatory to provide the value of `listingType` field as PREMIUM.

[Section titled: Recruiter System Connect and CRM Connect Extension Schema](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#recruiter-system-connect-and-crm-connect-extension-schema)

## Recruiter System Connect and CRM Connect Extension Schema

Includes additional attributes required or optional for [Recruiter System Connect (RSC)](https://learn.microsoft.com/en-us/linkedin/talent/recruiter-system-connect/recruiter-system-connect) and CRM Connect.

Expand table

| Field | Description | Type | Required |
| --- | --- | --- | --- |
| accessRestricted | Flag indicating whether the job is visible in the Recruiter UI and 1-Click Export dropdown list. For any ATS that does not have the ATS Integration Configuration set to "JOB\_POSTING\_VIEWERS" or "APPLICATION\_VIEWERS":<br>If accessRestricted is set to true, only recruiters in an ACL group tied to the job will see the job in the 1-Click Export dropdown list and be able to view associated associated applications in the LinkedIn Recruiter UI (In-ATS Indicator and ATS Tab). <br>If accessRestricted is set to false, jobs and applications will be visible for all recruiters in 1 Click Export dropdown list and the Recruiter UI respectively. <br> For an ATS which has ATS integration configuration "JOB\_POSTING\_VIEWER" setting as "ALL\_PRODUCT\_USERS", jobs will be visible for all recruiters in 1 Click Export dropdown list and in the LinkedIn Recruiter UI. <br> For an ATS which has ATS IntegrationConfiguration "APPLICATION\_VIEWER" setting "ALL\_PRODUCT\_USERS", associated applications with jobs will be visible for all recruiters in the LinkedIn Recruiter UI. | Boolean | No |
| availability | Valid values are `PUBLIC` or `PRIVATE_TO_ATS_INTEGRATION`. Must be `PUBLIC` for Apply Connect and Premium jobs | String | Yes |
| requisitionOwnerEmail | Email of the requisition owner | String | No |
| requisitionOwnerLastName | Last name of the requisition owner | String | No |
| requisitionOwnerFirstName | First name of the requisition owner | String | No |

Note

For Partner ATS who have also integrated for [Recruiter System Connect](https://learn.microsoft.com/en-us/linkedin/talent/recruiter-system-connect), it is a requirement that they make it optional for customers to choose whether to sync jobs as Private(PRIVATE\_TO\_ATS\_INTEGRATION) or Public.

[Section titled: Apply Connect Extension Schema](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#apply-connect-extension-schema)

## Apply Connect Extension Schema

Includes additional attributes required or optional for [Apply Connect](https://learn.microsoft.com/en-us/linkedin/talent/apply-connect)

Expand table

| Field | Description | Type | Required |
| --- | --- | --- | --- |
| onsiteApplyConfiguration | Information required to configure job applications to be collected on LinkedIn | [Onsite ApplyConfiguration](https://learn.microsoft.com/en-us/linkedin/talent/apply-connect/onsite-apply-config-schema) | Yes |

[Section titled: HTML Tags](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/job-posting-api-schema#html-tags)

## HTML Tags

The following HTML tags are supported for `description` and `skillsDescription` fields. Other HTML tags will be stripped out, and their contents will be displayed as plain text.

Expand table

| HTML Tag | Description |
| --- | --- |
| `<b>, <strong>` | Bold / strong |
| `<u>` | Underline |
| `<i>` | Italic |
| `<br>` | Line break |
| `<p>` | Paragraph |
| `<ul>` | Unordered list |
| `<li>` | List element |

* * *

## Feedback

Was this page helpful?

YesNo

[Provide product feedback](https://linkedin.zendesk.com/hc/en-us)

## Additional resources

* * *

Training


Learning path


[Implement finance and operations apps - Training](https://learn.microsoft.com/en-us/training/paths/implement-finance-operations/?source=recommendations)

Plan and design your project methodology to successfully implement finance and operations apps with FastTrack services, data management and more.