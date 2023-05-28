
# Google Calendar API OAuth 2.0 for Web Server Applications Integration - Django Rest Framework

This project provides a Django application for integrating with Google Calendar using the Google Calendar API. It allows users to authenticate with their Google accounts and access their calendar events.



# Features

- User authentication with Google OAuth2
- Authorization and permission management
- Retrieving and displaying user's calendar events
# Install the project dependencies:

pip install -r requirements.txt


Configure OAuth2 credentials:

   - Create a new project in the Google Cloud Console.
   - Enable the Google Calendar API for your project.
   - Download the OAuth2 credentials JSON file and save it as `credentials.json` in the `secrets` directory.

## ENDPOINT

This view should start step 1 of the OAuth. Which will prompt user for his/her credentials

/rest/v1/calendar/init/ -> google_calendar_init_view()


<img width="960" alt="oop1" src="https://github.com/jeet142002/google-calendar-integration-using-django-rest-api/assets/87035185/9e1ba053-88af-4287-8acc-0a4fa426d454">



Then after logging into your email id you will be directed to the redirect url

/rest/v1/calendar/redirect/ -> google_calendar_redirect_view()


<img width="960" alt="oop" src="https://github.com/jeet142002/google-calendar-integration-using-django-rest-api/assets/87035185/710f8e27-6c50-4d6f-9148-d078a5e088b1">


## NOTE 
To run this assignment you need google account credentials which needs to save in the project directory and also add a redirect URL in your google cloud.
