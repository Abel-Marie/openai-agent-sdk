import os
import sib_api_v3_sdk
from .config import *

# --- Helper: Brevo Configuration ---
def get_brevo_api_instance():
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.environ.get('BREVO_API_KEY')
    return sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
