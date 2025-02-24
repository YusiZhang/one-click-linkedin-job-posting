URL: https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-taskstatus
---
[Skip to main content](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-taskstatus#main)

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

[Download Microsoft Edge](https://go.microsoft.com/fwlink/p/?LinkID=2092881) [More info about Internet Explorer and Microsoft Edge](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge)

Table of contentsExit focus mode

[Read in English](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-taskstatus "Read in English")Save

- Add to Collections
- Add to plan

[Edit This Document](https://github.com/MicrosoftDocs/linkedin-api-docs/blob/live/linkedin-api-docs/talent/job-postings/api/check-job-taskstatus.md "Edit This Document")

Table of contents [Read in English](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-taskstatus "Read in English")Add to CollectionsAdd to plan[Edit](https://github.com/MicrosoftDocs/linkedin-api-docs/blob/live/linkedin-api-docs/talent/job-postings/api/check-job-taskstatus.md "Edit This Document")

* * *

#### Share via

[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fcheck-job-taskstatus%3FWT.mc_id%3Dfacebook) [x.com](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fcheck-job-taskstatus%3FWT.mc_id%3Dtwitter&text=Today%20I%20completed%20%22Job%20Operation%20Task%20Status%20-%20LinkedIn%20%7C%20Microsoft%20Learn%22!%20I%27m%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!&tw_p=tweetbutton&url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fcheck-job-taskstatus%3FWT.mc_id%3Dtwitter) [LinkedIn](https://www.linkedin.com/feed/?shareActive=true&text=Today%20I%20completed%20%22Job%20Operation%20Task%20Status%20-%20LinkedIn%20%7C%20Microsoft%20Learn%22!%20I%27m%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fcheck-job-taskstatus%3FWT.mc_id%3Dlinkedin) [Email](mailto:?subject=%5BShared%20Article%5D%20Job%20Operation%20Task%20Status%20-%20LinkedIn%20%7C%20Microsoft%20Learn&body=Today%20I%20completed%20%22Job%20Operation%20Task%20Status%20-%20LinkedIn%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Flinkedin%2Ftalent%2Fjob-postings%2Fapi%2Fcheck-job-taskstatus%3FWT.mc_id%3Demail)

* * *

Print

Table of contents

# Check Job Operation Task Status

- Article
- 02/04/2025
- 4 contributors

Feedback

After creating job postings, you can use the task ids from the response to track the status of the creation of the job postings. Typically the job creation process should take no longer than five minutes and it is suggested that you validate the completion of the job creation at least five minutes after your initial call to confirm there were no issues during job creation. The task IDs returned will have a lifespan of 30 days. Possible status values returned are: `IN_PROGRESS`, `SUCCEEDED` or `FAILED` and `PROCESSED`. Task Id is also returned after `UPDATE`, `RENEW` or `CLOSE` job operations.

Expand table

| STATUS | ERROR CODE | DESCRIPTION |
| --- | --- | --- |
| IN\_PROGRESS | Not Present | This is a temporary state and the job is still being evaluated |
| SUCCEEDED | Not Present | For a CREATE operation, API job was posted. <br>For UPDATE operation, update was successful and API job is posted on LinkedIn.<br> For CLOSE or RENEW operation, close or renew request was successful |
| FAILED | Present | For a CREATE operation, API job was not posted or did not pass validation. <br>For UPDATE operation, update was not successful. See task status on most recent CREATE operation to determine if the API job was posted on LinkedIn. <br>For CLOSE or RENEW operation, close or renew request was not successful |
| PROCESSED | Not Present | The API job has been processed successfully by LinkedIn |
| PROCESSED | Present | The API job has been processed by LinkedIn but also failed payload validation |

Note

The `PROCESSED` status indicates that customer's jobs are still being posted from an XML feed or career site. This status will appear during the stage when LinkedIn is evaluating the customer's job criteria to be migrated to API job postings.

[Section titled: Authentication](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-taskstatus#authentication)

## Authentication

All requests below require access tokens obtained via the [OAuth 2 Client Credentials flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow).

[Section titled: Throttle Limits](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-taskstatus#throttle-limits)

## Throttle Limits

Expand table

| Throttle Limits | Daily Call Limit (UTC) |
| --- | --- |
| Application maximum | 300,000 |

[Section titled: API Endpoint](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-taskstatus#api-endpoint)

## API Endpoint

```lang-https
GET https://api.linkedin.com/v2/simpleJobPostingTasks?ids={simpleJobPostingTaskUrn 1}&ids={simpleJobPostingTaskUrn 2}

```

[Section titled: Sample Response Body](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-taskstatus#sample-response-body)

## Sample Response Body

**Sample Response Body for Success**

```lang-json
{
    "errors": {},
    "results": {
        "urn:li:simpleJobPostingTask:07ae37ab-2216-4d0f-97a0-53a516681c8f": {
            "externalJobPostingId": "job-89a07328-89cc-4471-9b06-32d7b1f8f381",
            "id": "urn:li:simpleJobPostingTask:07ae37ab-2216-4d0f-97a0-53a516681c8f",
            "jobPosting": "urn:li:jobPosting:123456789",
            "status": "SUCCEEDED"
        },
        "urn:li:simpleJobPostingTask:edc75eb8-2c4f-4ac7-a64f-2ee583446f83": {
            "externalJobPostingId": "job-89a07328-89cc-4471-9b06-32d7b1f8f382",
            "id": "urn:li:simpleJobPostingTask:edc75eb8-2c4f-4ac7-a64f-2ee583446f83",
            "status": "IN_PROGRESS"
        }
    },
    "statuses": {}
}

```

[Section titled: SimpleJobPostingTask Field Schema](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-taskstatus#simplejobpostingtask-field-schema)

## SimpleJobPostingTask Field Schema

Expand table

| Field | Description | Format | Required |
| --- | --- | --- | --- |
| errorMessage | Description of an error resulting from a failed task. | String | Optional |
| externalJobPostingId | Unique job posting id within the partner's system. | String | Optional |
| id | Unique ID for a simple job posting task. | String | Required |
| jobPosting | Job posting resulting from a successful task. | String | Optional |
| location | The input location for a job using `alternateLocations` or customer based multiple location job rules. | String | Optional |
| status | Status of the task. List of possible statuses: `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, `PROCESSED`. | String | Required |

Note

If a job uses [`alternateLocations`](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-posting-status), a unique `simpleJobPostingTask` urn is returned as per `alternateLocations`

In the above example, observe that two results are returned with status values as `SUCCEEDED` and `IN_PROGRESS`. Status value of `SUCCEEDED` confirms that the job posting is live on LinkedIn.

**Sample Response Body for Error**

In case of an error, the request will return a `200 OK` response code and the error message is within the response body.

```lang-json
{
 "results": {
  "urn:li:simpleJobPostingTask:99da65f-d870-99f0-8734-8def50fb3765": {
   "errorMessage": "Job {partner=urn:li:jobPostingPartner:68204513, partnerJobCode=goldc04-03-12030896745} was dropped: true\n\nInvalid Field: /city; \nInvalid Field: /postalCode; \nInvalid Field: /state; \nInvalid Field: /geoLocation; ",
   "status": "FAILED",
   "id": "urn:li:simpleJobPostingTask:11da365f-d870-99f0-8734-8def50fb3765"
  }
 },
 "statuses": {},
 "errors": {}
}

```

Note

- Be sure to check the response for error statuses corresponding to individual entities you submitted. Ensure that the query string is limited to a maximum length of 4KB. Click [here](https://learn.microsoft.com/en-us/linkedin/shared/references/migrations/query-tunneling-migration#check-job-operation-task-status) for details and sample payload.

[Section titled: Error Codes](https://learn.microsoft.com/en-us/linkedin/talent/job-postings/api/check-job-taskstatus#error-codes)

## Error Codes

Refer below table to understand the HTTP response codes and corresponding error message. Below table should be followed for the purpose of troubleshooting.

One of the following responses is returned, that contains a JSON object with a status and a message about the error for Get on /simpleJobPostingsTasks.

Expand table

| HTTP CODE | RESPONSE STATUS | ERROR MESSAGE | DESCRIPTION | RESOLUTION |
| --- | --- | --- | --- | --- |
| 200 | Failed | Job processing failed due to a client-side error. Please check payload and integration setup. Error details: Trying to create a job with same partnerIdentifier already exists. It is duplicate creation request for a basic job or a non-draft premium job. Dropping the duplicate job posting creation request. LinkedIn job id: {job\_id}, externalJobPostingId: {jobPostingId} | There is already a premium job posted with same `externalJobPostingId` | Please ensure using unique `externalJobPostingId` in the Premium Job Posting API |
| 200 | Failed | Job {} was dropped: true Invalid Field: /description; Drop Message: The description length should be at least 100 characters | The description for the Job Posting should be more than 100 characters | Ensure the description of the job posing is more than 100 characters |
| 200 | Failed | Job processing failed due to a client-side error. Please check payload and integration setup. Error details: Operation type `RENEW` is not allowed for a non-existing job | The create/update job postings request has `operationType` as `RENEW` but the `externalJobPostingId` does not refer to any existing job postings | Please check to make sure the `externalJobPostingId` refers to an existing job posting |
| 200 | Failed | Job processing failed due to a client-side error. Please check payload and integration setup. Error details: Operation type `UPDATE` is not allowed for a non-existing job of partner urn urn:li:jobPostingPartner:{partner\_id}, partner job code ( `externalJobPostingId`) | Linkedin system is not able to find out the job to update with mentioned `externalJobPostingId` | LinkedIn uses `externalJobPostingId` to uniquely identify a premium job posted in its system. Please make sure the value of `externalJobPostingId` field in request body of UPDATE PREMIUM JOB api is used while posting premium job |
| 200 | Failed | The description length should be at least 100 characters | The value of description field in the response body of API to POST/UPDATE PREMIUM JOB should contain more than 100 characters | Provide description which contains more than 100 character in the `description` field in the response body of API to POST/UPDATE PREMIUM JOB |
| 200 | Failed | This job is blocked as its company is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_COMPANY\]. | The job payload has invalid company details | Please ensure right integrationContext or company |
| 200 | Failed | This job is blocked as its companyApplyUrl is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_COMPANY\_APPLY\_URL\]. | The companyApplyUrl is invalid URL | Please ensure valid URL format for companyApplyUrl |
| 200 | Failed | This job is blocked as its companyName is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_COMPANY\_NAME\]. | The companyName is invalid | Please ensure right company name for which this job posting is created |
| 200 | Failed | This job is blocked as its countryCode is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_COUNTRY\_CODE\]. | The location country/region is invalid | Please validate the country code in location field |
| 200 | Failed | This job is blocked as its description is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_DESCRIPTION\]. | The job description is invalid | Please validate right content, supported HTML tags and length for description |
| 200 | Failed | This job is blocked as its experience is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_EXPERIENCE\]. | The experienceLevel is invalid | Please ensure right enum for experienceLevel |
| 200 | Failed | This job is blocked as its geoLocation is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_GEO\_LOCATION\]. | The location is invalid | Please validate and update location field in supported formats |
| 200 | Failed | This job is blocked as its jobCategory is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_JOB\_CATEGORY\]. | The job categories is invalid | Please validate category names from predefined Job Functions reference table |
| 200 | Failed | This job is blocked as its jobType is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_JOB\_TYPE\]. | The employmentStatus is invalid | Please update right enum for employmentStatus |
| 200 | Failed | This job is blocked as its jobCode is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_ORIGINAL\_JOB\_CODE\]. | The companyJobCode is invalid | Please validate and update companyJobCode to valid string |
| 200 | Failed | This job is blocked as its sourceDomain is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_SOURCE\_DOMAIN\]. | The companyApplyUrl is invalid URL | Please ensure valid URL format for companyApplyUrl |
| 200 | Failed | This job is blocked as its sourceJobCode is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_SOURCE\_JOB\_CODE\]. | The companyJobCode is invalid | Please validate and update companyJobCode to valid string |
| 200 | Failed | This job is blocked as its sourceUrl is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_SOURCE\_URL\]. | The companyApplyUrl is invalid URL | Please ensure valid URL format for companyApplyUrl |
| 200 | Failed | This job is blocked as its standardizedLocation is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_STANDARDIZED\_LOCATION\]. | The location is invalid | Please validate and update location |
| 200 | Failed | This job is blocked as its title is marked invalid. Failure reason reference code: \[JOB\_FIELD\_PROCESSOR\_TITLE\]. | The job title is invalid | Please validate right content and length for title |
| 200 | Failed | We could not standardize your job's location. Please update the location in your ATS or careers site to post. | The location is not mapped | Please update location field with more accurate details |
| 200 | Failed | This job has an invalid location. Please update the location in your ATS or careers site to post. | The location is invalid | Please validate and update location field in supported formats |
| 200 | Failed | This job location cannot be standardized. Please refer to {:invalidLocationHelp,anchor,text#LinkedIn Help} for valid locations and workplace types for job posts. Click on \\u201CUpdate location\\u201D to select the job location, or update the location on the ATS to post. | The location is not mapped | Please update location field with more details |
| 200 | Failed | This job is missing location data. Click on Update location to select the job location, or update the location on the ATS to post. | The location is invalid | Please validate and update location |
| 200 | Failed | This job has an invalid Job URL. Please update the Job URL in your ATS or careers site to post. | The companyApplyUrl is invalid URL | Please ensure valid URL format for companyApplyUrl |
| 200 | Failed | This job post has an invalid job description. Please ensure a job description is present and between 100 - 25,000 characters. | The job description is invalid | Please validate right character length for description |
| 200 | Failed | This job post has an too many associated job functions. Please update the job functions listed in your ATS or careers site. | The industries are invalid | Please validate right enum for industries |
| 200 | Failed | This job post is missing industry codes. Please update the industry codes in your ATS or careers site to post. If the issue persists, please contact {:linkInfo,anchor,text#Customer Support} with this error code: \[MISSING\_INDUSTRY\_CODES\]." | The job industries is missing | Please update the payload to add right industries for hiring company |
| 200 | Failed | This job was blocked from ingestion due to missing job campaign. Please update your job payload to include a valid job campaign. If the issue persists, please contact Customer Support with this error code: \[MISSING\_JOB\_CAMPAIGN\]. | The partnerJobCampaignId is invalid | The partnerJobCampaignId is invalid |
| 200 | Failed | This job was blocked from ingestion due to missing source data. Please update your ingestion source as needed. If the issue persists, please contact {:linkInfo,anchor,text#Customer Support} with this error code: \[MISSING\_SOURCE\_DOMAIN\]. | The companyApplyUrl is invalid URL | Please ensure valid URL format for companyApplyUrl |
| 200 | Failed | This job could not be published because there is a {:duplicateJobPostingUrl,anchor,text#duplicate job} posted on LinkedIn. | The job is ingested already. You can use the "duplicateJobPostingUrl" to identify the duplicate job id. | Kindly retrieve or close existing job posting to proceed |
| 200 | Failed | This job is missing a connection to a LinkedIn company page. | The company page is restricted or invalid | Kindly request customer to reach out to linkedIn customer support team |
| 200 | Failed | The company page this job is linked to has blocked the posting. | The company admin has rejected this job post | Please validate company details or request company admin to access the job post |
| 200 | Failed | This job was not posted on LinkedIn due to employer not opted in. | The customer has specifically requested LinkedIn to stop the particular type of job ingestion with this source | Kindly request customer to reach out to linkedIn customer support team |
| 200 | Failed | This job was not posted on LinkedIn due to job source not opted in. | The company has specifically requested LinkedIn to stop the job ingestion with this source | Kindly request customer to reach out to linkedIn customer support team |
| 200 | Failed | This job was not posted on LinkedIn due to the a global block on job exports. | This job is restricted | Kindly request customer to reach out to linkedIn customer support team |
| 200 | Failed | This job was not posted on LinkedIn since it was deliberately marked as ignored by a field processor. | This job is restricted | Kindly request customer to reach out to linkedIn customer support team |
| 200 | Failed | This job was not posted on LinkedIn since its countryCode was not in the country/region allowlist. | The location country/region is blocked | We have restricted job postings for this location |
| 200 | Failed | This job was flagged by the jobs trust team as a low quality job. It was closed and will not be ingested again in the future. | The job details are not in accord with linkedIn job posting guidelines | Please create a new job with valid details |
| 200 | Failed | This job was determine to be spam. | The job details are not in accord with linkedIn job posting guidelines | Please create a new job with licit details |
| 200 | Failed | This job was dropped because of an unexpected error that occurred during job ingestion. This is meant to be a catch-all error. | The job is dropped due to server error | Please retry the job posting |
| 200 | Failed | This job was dropped due to validation error. | The job details are not in accord with linkedIn job posting guidelines | Please create a new job with valid details |
| 200 | Failed | This job was dropped due to poster specifically asking to not publish the job. | The posterEmail field is invalid | Please validate right permissions to post job |
| 200 | Failed | This job was manually taken down. | The job details are not in accord with linkedIn job posting guidelines | Please create a new job with licit details |
| 200 | Failed | This job was closed by original poster. | The job is closed by job admin | The reach out to job admin |
| 200 | Failed | This job has an invalid job campaign. | The partnerJobCampaignId is invalid | Please validate and update partnerJobCampaignId field |
| 200 | Failed | This job's budget has ran out. | The job budget has reached the limit | Please update the job posting credits for job |
| 200 | Failed | There is no job budget available for this job. | The contract budget has reached the limit | Please update the job posting credits for contract |
| 200 | Failed | The account level budget has ran out. | The account budget has reached the limit | Please update the recruiter account credits for contract |
| 200 | Failed | This job's affordable offer has reach end. | The job budget has reached the limit | Please update the job posting credits for job |
| 200 | Failed | This job's duration limit has been reach. | The job budget has reached the limit | Please update the job posting credits for job |
| 200 | Failed | This job's free trial budget has ran out | The job budget has reached the limit | Please update the job posting credits for job |
| 200 | Failed | A post payment failure is detected for this job. | The job budget has reached the limit | Please update the job posting credits for job |
| 200 | Failed | This job is suspended due to trust related restrictions. | The job details are not in accord with linkedIn job posting guidelines | Please create a new job with licit details |
| 400 | 400 | Batch key parameter value is invalid | The request parameter IDs does not contain valid job posting task urn | Please ensure that you are using valid task urn which is obtained in the response body of API calls to post, update or close Premium Jobs |
| 401 | 401 | Invalid access token | Access token is tampered | Regenerate a new access token |
| 401 | 401 | The token used in the request has expired | The access token used in Authorization header is a valid token but it has expired | Regenerate a new access token |

* * *

## Feedback

Was this page helpful?

YesNo

[Provide product feedback](https://linkedin.zendesk.com/hc/en-us)

## Additional resources