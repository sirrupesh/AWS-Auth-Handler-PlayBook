# Use the native inference API to send a text message to Anthropic claude.
import boto3
import json
from botocore.exceptions import ClientError
from aws_auth_handler import AWSAuthenticator, AWSAuthenticationError

try:
    # Initialize with .env file
    auth = AWSAuthenticator(env_file='.env')
    # auth = AWSAuthenticator(profile_name='dev')

    # Check with credentials are loaded
    credentials = auth.get_credentials()
    print(f"Access Key: {credentials['aws_access_key_id']}")

    # Create an Amazon Bedrock Runtime client.
    brt = auth.get_client('bedrock-runtime', region_name='us-east-1')

    # Set the model ID. The unique identifier of the model to invoke to run inference.
    modelId = 'anthropic.claude-v2'
    # modelId = 'anthropic.claude-v2:1'

    # The desired MIME type of the inference body in the response. The default value is application/json.
    accept = 'application/json'
    # The MIME type of the input data in the request body. The supported MIME types for the input data are application/json.
    contentType = 'application/json'

    # Define the prompt for the model.
    prompt = 'Explain about The Big Bang Theory.'
    # prompt = 'How to react during the natural disaster in 100 words?'
    # prompt = "How to Respond to a Disaster?"

    # Format the request payload using the model's native structure.
    native_request = {
        'prompt': '\n\nHuman: ' + prompt + '\n\nAssistant:',
        'max_tokens_to_sample': 300,
        'temperature': 0.2,
        'top_k': 250,
        'top_p': 1,
        'stop_sequences': ['\n\nHuman:'],
        'anthropic_version': 'bedrock-2023-05-31'
    }

    # Convert the native request to JSON.
    request = json.dumps(native_request)

    try:
        # Invoke the model with the request.
        response = brt.invoke_model(
            body=request, modelId=modelId, accept=accept, contentType=contentType)

    except (ClientError, Exception) as e:
        print(f"ERROR: Can't invoke '{modelId}'. Reason: {e}")
        exit(1)

    # Decode the response body.
    response_body = json.loads(response.get('body').read())

    # Extract and print the response text.
    print(response_body.get('completion'))
except AWSAuthenticationError as e:
        print(f"Authentication failed: {e}")
except Exception as e:
        print(f"Error Occures: {e}")