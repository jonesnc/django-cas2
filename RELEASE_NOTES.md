Release Notes
-------------

## Version 2.0.3-KTH-11

* Incorporated support for single sign out. 
* Project has since then moved to other repository and all pull requests 
  seem to be thrown away, so the project seems officially a dead end 
  for other purposes than the ones intended by the maintainer.
* Heavily refactorized.
  * Removed support for CAS 1.0.
  * Removed support for old Python versions.
  * Removed lots of other dead code.
  * Improved XML handling.
  * Added logging.
  * Lots of clean ups.
* Add setting CAS_SINGLE_SIGN_OUT True/False to allow for turning 
  off single sign out support, default True.
* Add setting CAS_ALLOWED_PROXIES [list of URLS] to support basic 
  filtering of allowed proxy servers, not tested.
* Add setting CAS_AUTO_CREATE_USERS True/False to control behavior
  where backend auto creates users that are logged in, default False.

## Version 2.0.3-KTH-10
 
* Added support for CAS proxy authentication.
* Removed messaging.