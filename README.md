# RightSignature API written in Python
## by Anton Kaiser

###### pip install RightSignature


Initialize
```
from RightSignature import *
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
RightSignature = RightSignature.CRightSignature(API_KEY)
if not RightSignature.isLoggedIn():
	print("Wrong API Key!")
	exit(0)
```
