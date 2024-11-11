import time
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
from mailosaur.models.mailosaur_exception import MailosaurException
from conftest import CONFIG

api_key = CONFIG['MAILOSAUR_API_KEY'] # Replace with your API key
server_id = "ohladkcn"

# api_key = CONFIG["BACKUP_MAILOSAUR_API_KEY"]
# server_id = "hzvkcfrq"


def generate_random_email_address():
    """Generates a random Mailosaur email address."""
    random_string = str(int(time.time()))
    new_email = f"kev{random_string}@{server_id}.mailosaur.net"
    return new_email

def get_otp_from_email(email_address):
    """Retrieves the latest OTP from a Mailosaur email address."""
    mailosaur_client = MailosaurClient(api_key)
    
    # Initialize criteria inside the function
    criteria = SearchCriteria() 
    criteria.sent_to = email_address  

    # Wait for the email with the OTP
    while True:
        
        try:
            # Specify the criteria for retrieving the email
            email = mailosaur_client.messages.get(server_id, criteria)
            if email:  # Check if an email was found
                for code in email.html.codes:
                    if code.value:
                        otp = [char for char in code.value]
                        return otp
                
        except MailosaurException as e:  # General Mailosaur error
            print(f"Mailosaur API error: {e}")
        except Exception as e:  # Catch any other unexpected exceptions
            print(f"An unexpected error occurred: {e}")
        finally:
            time.sleep(2)  # Wait before retrying
            
    raise Exception("Email with the specified subject not found")