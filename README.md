

# RightSignature API written in Python
## by Anton Kaiser

#### pip install RightSignature

Get the API-Key from [here](https://rightsignature.com/oauth_clients) called "Secure Token"



Initialize
```
from rightsignature import *
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
RightSignature = RightSignature.CRightSignature(API_KEY)
if not RightSignature.isLoggedIn():
	print("Wrong API Key!")
	exit(0)
```

Get the Document Array
```
for document in RightSignature.getDocuments(): // get the Array
	document = RightSignature.getDocument(document.getGuid()) // get the full Object
```

download a signed  PDF
```
RightSignature.downloadSignedPDF(document,"./" + document.getGuid() + '.pdf')
```

Classes/Objects
```
CRightSignature:
getDocuments(date="alltime", debug=False) - Returns a CDocument Array - the CDocument is not full filled!
	date: 'today', 'thisweek', 'thismonth', 'alltime'
			or a date in the format 'yyyy-mm-dd'
	debug: Print debug logs
	hint: the script loads all pages!
getDocumentsRange(dateStart="2019-01-25", dateEnd="2019-05-25", debug=False) - Returns a CDocument Array - the CDocument is not full filled!
	dateStart/dateEnd: in the format 'yyyy-mm-dd'
	debug: Print debug logs
	hint: the script loads all pages!
getDocument(documentGUID) - Returns a full CDocument
downloadSignedPDF(CDocument, location, debug=False) - Returns a void
	debug: prints a message when a download failed
	hint: when a download fails, the script will redownload the file
isLoggedIn() - Returns a boolean
```

```
CDocument:
getAuditTrails() - Returns a CAudiot Array
getCallbackLocation() - Returns a String
getCompletedAt() - Returns a String
getContentType() - Returns a String
getCreatedAt() - Returns a String
getExpiresOn() - Returns a String
getFormFields() - Returns a CField Array
getGuid() - Returns a String
isTrashed() = Returns a boolean
getLargeUrl() - Returns a String
getLastActivityAt() - Returns a String
getMergeState() - Returns a String
getMessage() - Returns a String
getOriginalFilename() - Returns a String
getOriginalUrl() - Returns a String
getPages() - Returns a CPage Array
getPdfUrl() - Returns a String
getProcessingState() - Returns a String
getRecipients() - Returns a CRecipient Array
getSignedPdfChecksum() - Returns a String
getSignedPdfUrl() - Returns a String
getSize() - Returns a String
getState() - Returns a String
getSubject() - Returns a String
getTags() - Returns a String
getThumbnailUrl() - Returns a String
```

```
CAudit:
getKeyword() - Returns a String
getMessage() - Returns a String
getTimestamp() - Returns a String
```
```
CRecipient:
getCompletedAt() - Returns a String
getDocumentRoleID() - Returns a String
getEmail() - Returns a String
isSender() - Returns a String
getMustSign() - Returns a String
getName() - Returns a String
getRoleID() - Returns a String
getState() - Returns a String
getViewedAt() - Returns a String
```


```
CPage:
getOriginalTemplateFilename() - Returns a String
getOriginalTemplateGUID() - Returns a String
getPageNumber() - Returns a String
```


```
CField:
getID() - Returns a String
getName() - Returns a String
getPage() - Returns a String
getRoleID() - Returns a String
getValue() - Returns a String
```

Example:
```
for document in RightSignature.getDocuments():
	document = RightSignature.getDocument(document.getGuid())
	print("")
	print("=====================================================")
	print("===========" + document.getGuid() + " | " + document.getState() + "===========")
	print("=====================================================")
	name = document.getOriginalFilename().replace(".pdf","").replace("-","_")
	if len(document.getFormFields()) > 0:
		print("Document is ready!")
		print("Downloading...")
		RightSignature.downloadSignedPDF(document,"./" + document.getGuid() + '.pdf')
	else:
		print("Still on " + document.getState())
		print("User opened the document last time at the: " + document.getLastActivityAt())
	print("=====================================================")


```