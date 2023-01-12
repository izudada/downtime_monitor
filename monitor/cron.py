import requests
from .models import WebLog, Website
from django.conf import settings
import smtplib, ssl
import json


def send_email_to_user(receiver_email, message):
    """
        A function that sends email
        about a downtime or uptime
        of a website
    """
    smtp_server = settings.EMAIL_HOST
    port = 587  # For starttls
    sender_email = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 


def get_web_status():
    """
        A get request that runs every 1 hour
    """
    print("Start")
    #   email subject
    #   get all websites
    try:
        all_websites = Website.objects.all()
    except Exception as e:
        print(e)
    
    #   loop all websutes to check their status before sending mail
    for website in all_websites:

        print("Getting all websites")
        #   ping website with request library
        try:
            response = requests.get(website.url)
            ticker = "active"
        except Exception as e:
            print(e)
            ticker = "inactive"
        
        #   send email only if state of website has changed
        if ((ticker == "active" and website.state == "inactive") or
            (ticker == "inactive" != 200 and website.state == "active")):
            #   change website state
            website.state = ticker
            website.save()

            #   loop emails to send mail
            for email in website.emails.values():
                message = f"""
                        Subject: "Website Monitoring Status"
                            Dear csutomer,

                            This is to notify you that you website {website.name} 
                            with the ur "{website.url}" is {ticker}.
                            You can request for logs using our API
                        """
                try:
                    print(f"sending email to {email}")
                    send_email_to_user(email, message)
                except Exception as e:
                    print(e)
            #   saved data as log
            log_data = {
                    "name" : website.name,
                    "url": website.url,
                    "active": ticker,
                    "date": str(website.updated_at)
                }
            try:
                log = WebLog.objects.create(web=website, web_log=json.dumps(log_data))
                log.save()
                print(log)
            except Exception as e:
                print(e)

    print("Done")
