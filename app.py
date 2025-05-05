from aws_auth_handler import AWSAuthenticator, AWSAuthenticationError

def list_lambda_functions():
    try:
        # auth = AWSAuthenticator()
    
        # Initialize with a specific AWS profile
        # auth = AWSAuthenticator(profile_name='default')
        # auth = AWSAuthenticator(profile_name='staging')
        # auth = AWSAuthenticator(profile_name='development')
        # auth = AWSAuthenticator(profile_name='non-existent-profile')
        
        # Initialize with .env file
        auth = AWSAuthenticator(env_file='.env')

         # Check with credentials are loaded
        credentials = auth.get_credentials()
        print(f"Access Key: {credentials['aws_access_key_id']}")

        
        # Get Lambda client for a specific region
        lambda_client = auth.get_client('lambda', region_name='us-west-2')
        
        # List functions with pagination
        paginator = lambda_client.get_paginator('list_functions')
        
        print("\nAWS Lambda Functions:")
        print("-" * 50)
        
        for page in paginator.paginate():
            for function in page['Functions']:
                print(f"Function Name: {function['FunctionName']}")
                # print(f"Runtime: {function['Runtime']}")
                print(f"Memory: {function['MemorySize']} MB")
                print(f"Last Modified: {function['LastModified']}")
                print("-" * 50)

    except AWSAuthenticationError as e:
        print(f"Authentication failed: {e}")
    except Exception as e:
        print(f"Error listing Lambda functions: {e}")

if __name__ == "__main__":
    list_lambda_functions()