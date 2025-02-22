URL: https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#sample-request-for-basic-jobs
---
[Skip to main content](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#main)

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

[Download Microsoft Edge](https://go.microsoft.com/fwlink/p/?LinkID=2092881) [More info about Internet Explorer and Microsoft Edge](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge)

Table of contentsExit focus mode

[Read in English](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#sample-request-for-basic-jobs "Read in English")Save

- Add to Collections
- Add to plan

[Edit This Document](https://github.com/MicrosoftDocs/linkedin-api-docs/blob/live/linkedin-api-docs/talent/job-postings/api/create-jobs.md "Edit This Document")

Table of contents [Read in English](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#sample-request-for-basic-jobs "Read in English")Add to CollectionsAdd to plan[Edit](https://github.com/MicrosoftDocs/linkedin-api-docs/blob/live/linkedin-api-docs/talent/job-postings/api/create-jobs.md "Edit This Document")

* * *

#### Share via

[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fcreate-jobs%3FWT.mc_id%3Dfacebook) [x.com](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fcreate-jobs%3FWT.mc_id%3Dtwitter&text=Today%20I%20completed%20%22Create%20Jobs%20-%20LinkedIn%20%7C%20Microsoft%20Learn%22!%20I%27m%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!&tw_p=tweetbutton&url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fcreate-jobs%3FWT.mc_id%3Dtwitter) [LinkedIn](https://www.linkedin.com/feed/?shareActive=true&text=Today%20I%20completed%20%22Create%20Jobs%20-%20LinkedIn%20%7C%20Microsoft%20Learn%22!%20I%27m%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fcreate-jobs%3FWT.mc_id%3Dlinkedin) [Email](mailto:?subject=%5BShared%20Article%5D%20Create%20Jobs%20-%20LinkedIn%20%7C%20Microsoft%20Learn&body=Today%20I%20completed%20%22Create%20Jobs%20-%20LinkedIn%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fcreate-jobs%3FWT.mc_id%3Demail)

* * *

Print

Table of contents

# Create Jobs

- Article
- 02/04/2025
- 3 contributors

Feedback

To create a job, post the job by providing unique `externalJobPostingId` value and set the `jobPostingOperationType` as `CREATE`.

[Section titled: API Overview](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#api-overview)

## API Overview

Use the `/simpleJobPosting` API to create, update, renew and close jobs on LinkedIn. This wiki describes how to create jobs. To know more about this API, refer to [API Overview](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/sync-job-postings).

[Section titled: API Endpoint](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#api-endpoint)

### API Endpoint

Use the following endpoint to submit a task to create, close, update, or renew one or more jobs asynchronously:

```lang-https
POST https://api.linkedin.com/v2/simpleJobPostings

```

[Section titled: API Authorization](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#api-authorization)

### API Authorization

All requests below require access tokens obtained via the [OAuth2.0 Client Credentials flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow).

Important

We strongly recommend to use same access token for all concurrent and consecutive calls. An access token has a lifespan of 30 mins. Only on expiry of the existing token, new token should be generated.

Note

- Ensure that requests do not include duplicate updates to the same `externalJobPostingId`
- The maximum number of jobs which can be submitted during one batch call is 100. If you would like to submit more than 100 jobs at a time, please group your jobs in to collections of 100 and make multiple batch calls in sequential order

[Section titled: Sample Request for Basic Jobs](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#sample-request-for-basic-jobs)

## Sample Request for Basic Jobs

In order to publish a job as a free job, you need to provide `listingType` field value as `BASIC`.

**API Header**:

The header for making the request is `X-Restli-Method: batch_create`.

```lang-https
Authorization: Bearer {token}
x-restli-method: batch_create

```

**Sample Request Body**:

```lang-json
{
 "elements": [{\
   "integrationContext": "urn:li:organization:2414183",\
   "companyApplyUrl": "http://linkedin.com",\
   "description": "We are looking for a passionate Software Engineer to design, develop and install software solutions. Software Engineer responsibilities include gathering user requirements, defining system functionality and writing code in various languages. Our ideal candidates are familiar with the software development life cycle (SDLC) from preliminary system analysis to tests and deployment.",\
   "employmentStatus": "PART_TIME",\
   "externalJobPostingId": "1234",\
   "listedAt": 1440716666,\
   "jobPostingOperationType": "CREATE",\
   "title": "Software Engineer",\
   "location": "India",\
   "workplaceTypes": [\
    "remote"\
   ]\
  },\
  {\
   "integrationContext": "urn:li:organization:2414183",\
   "companyApplyUrl": "http://linkedin.com",\
   "description": "We are looking for a passionate Software Engineer to design, develop and install software solutions. Software Engineer responsibilities include gathering user requirements, defining system functionality and writing code in various languages. Our ideal candidates are familiar with the software development life cycle (SDLC) from preliminary system analysis to tests and deployment.",\
   "employmentStatus": "PART_TIME",\
   "externalJobPostingId": "1234",\
   "listedAt": 1440716666,\
   "jobPostingOperationType": "CREATE",\
   "title": "Software Engineer",\
   "location": "San Francisco, CA",\
   "workplaceTypes": [\
    "hybrid"\
   ]\
  },\
  {\
   "integrationContext": "urn:li:organization:2414183",\
   "companyApplyUrl": "http://linkedin.com",\
   "description": "We are looking for a passionate Senior Software Engineer to design, develop and install software solutions. Software Engineer responsibilities include gathering user requirements, defining system functionality and writing code in various languages. Our ideal candidates are familiar with the software development life cycle (SDLC) from preliminary system analysis to tests and deployment.",\
   "employmentStatus": "PART_TIME",\
   "externalJobPostingId": "789",\
   "listedAt": 1440716666,\
   "jobPostingOperationType": "CREATE",\
   "title": "Senior Software Engineer",\
   "location": "San Francisco, CA"\
  }\
 ]
}

```

Note

The first element in the above request body is an example of posting a remote job on LinkedIn (workplaceTypes is `remote`, note that the `location` field has only `COUNTRY` value) and the second element is an example of posting a hybrid job (workplaceTypes is `hybrid`). In the third element, since no value for `workplaceTypes` field is provided, the job will get posted as an `On-site` job.

[Section titled: Sample Request for Promoted Jobs](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#sample-request-for-promoted-jobs)

## Sample Request for Promoted Jobs

In order to post a job as promoted, you need to provide `listingType` field value as `PREMIUM`.

Note

Only selective partners have the permission to post promoted jobs. If your developer application does not support posting promoted jobs, reach out to LinkedIn's business development point of contact (if interested).

[Section titled: API Header](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#api-header)

### API Header

```lang-http
Authorization: Bearer {access token}
X-restli-method: batch_create

```

[Section titled: Sample Request Body](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#sample-request-body)

### Sample Request Body

```lang-json
{
   "elements":[\
      {\
         "externalJobPostingId":"PremiumJobPostingG1TC1",\
         "listingType":"PREMIUM",\
         "title":"Premium Job Posting G1 TC1",\
         "description":"<b>Objective of the Position</b><br/> <ul> <li>To develop digital content plan, manage and monitor different content executions for social and online platforms to maximize the communication effectiveness and impact</li> <li>To manage, monitor and keep optimizing the performance of social platforms of MB and AMG</li> <li>To monitor and manage internet word of mouth to keep the health of brand and product image</li></ul>",\
         "contract":"urn:li:contract:{your_contract_id}",\
         "integrationContext":"urn:li:organization:{your_organization_id_01}",\
         "companyApplyUrl": "http://linkedin.com/jobpostingG1TC1",\
         "location":"San Francisco, CA",\
         "listedAt":1513756352000,\
         "jobPostingOperationType":"CREATE"\
      },\
      {\
         "externalJobPostingId":"PremiumJobPostingG1TC2",\
         "listingType":"PREMIUM",\
         "title":"Premium Job Posting G1 TC2",\
         "description":"<b>G1 TC2: Objective of the Position</b><br/> <ul> <li>To develop digital content plan, manage and monitor different content executions for social and online platforms to maximize the communication effectiveness and impact</li> <li>To manage, monitor and keep optimizing the performance of social platforms of MB and AMG</li> <li>To monitor and manage internet word of mouth to keep the health of brand and product image</li></ul>",\
         "contract":"urn:li:contract:{your_contract_id}",\
         "industries":["urn:li:industry:4", "urn:li:industry:99"],\
         "integrationContext":"urn:li:organization:{your_organization_id_02}",\
         "companyApplyUrl": "http://linkedin.com/jobpostingG1TC2",\
         "location":"San Francisco, CA",\
         "listedAt":1513756352000,\
         "jobPostingOperationType":"CREATE",\
         "posterEmail":"stub@your_poster_email_address"\
      }\
   ]
}

```

Note

- Ensure that requests do not include duplicate updates to the same `externalJobPostingId`
- To post promoted jobs it is mandatory to provide contract information. If the `posterEmail` field is not provided the job is be posted on behalf of the default job poster email configured by recruiter customers

[Section titled: Sample Request for Internal Only Jobs](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#sample-request-for-internal-only-jobs)

## Sample Request for Internal Only Jobs

In order to post a job as internal only, you need to provide `availability` field value as `INTERNAL`.

Note

Only selective partners have the permission to post promoted jobs. If your developer application does not support posting promoted jobs, reach out to LinkedIn's business development point of contact (if interested).

[Section titled: API Header](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#api-header-1)

### API Header

```lang-http
Authorization: Bearer {access token}
X-restli-method: batch_create

```

[Section titled: Sample Request Body](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#sample-request-body-1)

### Sample Request Body

```lang-json
{
   "elements":[\
      {\
         "externalJobPostingId":"PremiumJobPostingG1TC1",\
         "listingType":"BASIC",\
         "title":"Job Posting G1 TC1",\
         "description":"<b>Objective of the Position</b><br/> <ul> <li>To develop digital content plan, manage and monitor different content executions for social and online platforms to maximize the communication effectiveness and impact</li> <li>To manage, monitor and keep optimizing the performance of social platforms of MB and AMG</li> <li>To monitor and manage internet word of mouth to keep the health of brand and product image</li></ul>",\
         "contract":"urn:li:contract:{your_contract_id}",\
         "integrationContext":"urn:li:organization:{your_organization_id}",\
         "companyApplyUrl": "http://linkedin.com/jobpostingG1TC1",\
         "location":"San Francisco, CA",\
         "listedAt":1513756352000,\
         "jobPostingOperationType":"CREATE",\
         "availability": "INTERNAL"\
      }\
   ]
}

```

Note

- Ensure that requests do not include duplicate updates to the same `externalJobPostingId`
- To post internal jobs it is mandatory to provide contract information.

[Section titled: Sample Response Body](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#sample-response-body)

### Sample Response Body

Below are the response body examples for success and error scenarios:

**Sample Response Body for Success**

A successful request returns a `200 OK` response code, and you will find the `simpleJobPostingTaskIDs` in the response body.

```lang-json
{
    "elements": [\
        {\
            "id": "urn:li:simpleJobPostingTask:03ff7ca6-dedf-4d92-b856-10669f8fe5ef",\
            "status": 202\
        },\
        {\
            "id": "urn:li:simpleJobPostingTask:01c922a8-96cd-4c32-8cc1-40eea169fe01",\
            "status": 202\
        }\
    ]
}

```

**Sample Response Body for Error**

In case of an error, the request will return a `200 OK` response code and the error message is within the response body.

```lang-json
{
 "elements": [{\
  "error": {\
   "message": "ERROR :: /title :: field is required but not found and has no default value\n",\
   "status": 422\
  },\
  "status": 422\
 }]
}

```

Note

- Be sure to check the response for error statuses corresponding to individual entities you submit
- The Task ids returned in the above response are valid for 24 hours
- [Check the Job Operation Task Status](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-taskstatus) to find the status of the job posting via above task ids
- The value of `integrationContext` field is obtained from customer onboarding widget. To know more, refer to [Apply Connect's Customer OnBoarding](https://learn.microsoft.com/en-us/linkedin/talent/apply-connect/customer-configuration) or [Recruiter System Connect's Customer OnBoarding](https://learn.microsoft.com/en-us/linkedin/talent/recruiter-system-connect/rsc-customer-configuration#2-display-the-ats-integration-configuration-plugin). If this value is not present please provide the company information via `companyName` field

[Section titled: How to Test](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#how-to-test)

## How to Test

To test and view the public jobs that were successfully posted, use your `integrationContextid` to view the job here: `https://www.linkedin.com/jobs/search/?f_C={id}&locationType=Y`. For jobs posted with an availability set to `PRIVATE_TO_ATS_INTEGRATION`, login to your [Recruiter platform](https://www.linkedin.com/talent/login) with development contract and use the [One-Click Export](https://learn.microsoft.com/en-us/linkedin/talent/recruiter-system-connect/recruiter-system-connect) feature.

[Section titled: API Error Details](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/create-jobs#api-error-details)

## API Error Details

Click to view a list of possible API error codes that can display while creating a job.

One of the following responses is returned, that contains a JSON object with a status and a message about the error for Post on /simpleJobPostings.

Expand table

| HTTP CODE | RESPONSE STATUS | ERROR MESSAGE | DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- | --- |
| 200 | 422 | ERROR :: /{mandatory key} :: field is required but not found and has no default value | Required field is missing in the request body | Refer to the schema documentation and ensure all the required fields are present in the request body |
| 200 | 422 | ERROR :: /{attribute\_name} :: {value} cannot be coerced to Long\\n", (Why is \\n coming in error message) | When value of the attribute does not match the datatype it accepts. For example, `title` accepts String but we have provided numerical value | Ensure that the value provided for attribute should match the datatype it accepts. Please refer to schema documentation for data types of the attributes |
| 200 | 422 | ERROR :: / `jobPostingOperationType` :: "UPDATED" is not an enum symbol\\n | Wrong value provided for the field `jobPostingOperationType` | The value should either be one of `CREATE`, `UPDATE` or `CLOSE` |
| 200 | 400 | The `workplaceTypes` field cannot have more than one value provided. Provided values \[..\] | `workplaceTypes` field accepts an array of only one element, but the request contains more than one elements for `workplaceTypes` field | Ensure that `workplaceTypes` field is an array with only one element (one of the following: `On-Site`, `Hybrid`, `Remote`) |
| 400 | 400 | Invalid company apply url for job with externalPartnerId {externalJobPostingId}, taskUrn urn:li:simpleJobPostingTask:{taskID} | The URL specified for the job posting is in an invalid format | Ensure the url specified is in a valid url |
| 400 | 400 | Either `context` or `company` or `companyPageUrl` or `companyName` must be provided | Integration context company field is missing | All jobs are associated with company page. You can provide this value with either of the schema fields listed in the error messages |
| 401 | 401 | Invalid access token | Access token is tampered | Regenerate a new access token |
| 401 | 401 | The token used in the request has expired | The access token used in Authorization header is a valid token but it has expired | Regenerate a new access token |
| 402 | 402 | Insufficient job slots for contract = urn:li:contract:{contract\_id} for purchase flow | All job slots associated with the supplied contract are used | Please ask the customer to reach out to LinkedIn's customer support to purchase more Job Slots with LinkedIn or Close some existing Premium Job Postings to free up Job Slots. To know more refer to LinkedIn [help center article](https://www.linkedin.com/help/linkedin/answer/a417111?lang=en). If this issue is occurring frequently in your development environment please create a ticket on Zendesk Platform |
| 402 | 402 | Insufficient lifetime budget for contract: urn:li:contract:{contract\_id} | For FP4P jobs PAYMENTS\_INSUFFICIENT\_FUNDS contract has exhausted allocated budget for premium job posting. Contract monthly limits can be setup within LinkedIn Recruiter | Please validate contract limit per month or sufficient balance before posting a premium job |
| 403 | 403 | Caller is not authorized to access the jobs for contract: urn:li:contract:{contract\_id} | The application used for posting premium job does not belong to the Job posting contract | 1\. Ensure that you are using the correct contract details provided in the Premium Job Posting onboarding email <br> 2\. Ensure that you are using the correct application credentials |
| 403 | 403 | Not enough permissions to access: POST /simpleJobPostings | The application does not have enough permissions to use /simpleJobPostings API | Ensure that the header x-restli-method with value batch\_create is present |
| 403 | 403 | Unpermitted fields present in REQUEST\_BODY: Data Processing Exception while processing fields \[/elements\] | Value for Request Header: `x-restli-method: batch_create` is not provided | Ensure that value for Request Header: `x-restli-method: batch_create` is provided |
| 403 | 403 | Caller is not authorized to access the fp4p contract | Customer is unable to post premium jobs after widget opt-in | Pay for performance contract customers need to enable toggle for posting of promoted jobs with a LinkedIn recommended budget using the [Job Posting API](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/overview) (Partner Integrations) |
| 403 | 403 | Not enough permissions to access: POST (Name) | Access token is generated from the application which does not have permission to access this resource | Use Partner application for creating child application, all other resources should be requested using child applications |
| 404 | 404 | Resource (Name) does not exist | API URL format is incorrect | Please verify the URL format from documentation and sample code |
| 409 | 409 | Cannot close job which is already closed or does not exist | The request payload is trying to close a job which either does not exist or is already closed | Ensure that the `jobPostingOperationType` value is `CREATE` while creating new job postings |
| 422 | 422 | ERROR :: / `employmentStatus` :: {value} is not an enum symbol | Wrong value provided for the field `employmentStatus` | The value should either be one of `FULL_TIME`, `PART_TIME`, `CONTRACT`, `INTERNSHIP`, `TEMPORARY`, `VOLUNTEER` or `OTHER` |
| 422 | 422 | ERROR :: / `experienceLevel` :: {value} is not an enum symbol | Wrong value provided for the field `experienceLevel` | The value should either be one of `ENTRY_LEVEL`, `MID_SENIOR_LEVEL`, `DIRECTOR`, `EXECUTIVE`, `INTERNSHIP`, `ASSOCIATE` or `NOT_APPLICABLE` |
| 422 | 422 | ERROR :: / `state` :: {value} is not an enum symbol | Wrong value provided for the field `state` | The value should either be one of `LISTED` or `CLOSED` |
| 422 | 422 | ERROR :: /{field} :: enum type is not backed by a String | Field expects an enum value in the form of String but the value passed is not a string. For example, `state` : 123 | Ensure the Enum value provided is in a String |
| 422 | 422 | The job contains more than seven locations. Please ensure maximum seven locations per job | More than seven locations are passed in the `alternateLocations` field | You can add upto seven locations in a single API call |
| 500 | 500 | Internal Server Error | When incorrect attribute type is given. For example, Integer instead of String | Please check if `externalJobPostingId` datatype is string in request body |
| 504 | 504 | Gateway Timeout | Invalid API request | Please recheck all header's and API payload |

* * *

## Feedback

Was this page helpful?

YesNo

[Provide product feedback](https://linkedin.zendesk.com/hc/en-us)

## Additional resources