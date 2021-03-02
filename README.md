# Rest-API-Django-

## Simple API to register a User, check if credentials are correct, add or remove their favorite category.


Requirements:
1. First the email will be sent through the API
2. If it is a registered email id, then the response should be <br/>
{ <br/>
 user_id: <br/>
 login_type: signin <br/>
}<br/>
3. The userId and password will be sent to the same API
 If the credentials are correct, them the response should be<br/>
{<br/>
 message: " login successful "<br/>
}<br/>
 Else the response should be<br/>
{<br/>
message: "failed"<br/>
}<br/>
4. In the step 1, if the email id is not registered, then the response should be<br/>
{<br/>
 user_id: "not registered"<br/>
 login_type: "signup"<br/>
}<br/>
5. To register new user, the following details will be sent though the API
 Email address, Password, First Name, Last Name
 
----------------------------------------------------------------------------------------------------
1. User Details API:
* user_id will be sent.
* Should give email, first name, last name and favorites of user.
2. Add Favourites:
* user_id and a favourite category name will be sent.
* Should add the category to the list of favourites.
3. Remove Favourites:
* user_id and a favourit category name will be sent
* Should remove the category from the list of favourites
