from aws_auth_handler import AWSAuthenticator, AWSAuthenticationError

def list_s3_buckets():
    try:
        # auth = AWSAuthenticator()
        
        # Initialize with a specific AWS profile
        # auth = AWSAuthenticator(profile_name='default')
        # auth = AWSAuthenticator(profile_name='staging')
        # auth = AWSAuthenticator(profile_name='development')
        # auth = AWSAuthenticator(profile_name='non-existent-profile')
        
        # Initialize with .env file
        # auth = AWSAuthenticator(env_file='.env')
        auth = AWSAuthenticator(env_file='.env')

        # Check with credentials are loaded
        credentials = auth.get_credentials()
        print(f"Access Key: {credentials['aws_access_key_id']}")

        # Get an S3 client
        s3_client = auth.get_client('s3')

        # Use the client to list buckets
        response = s3_client.list_buckets()
        
        # Print bucket list
        print("\nAvailable S3 Buckets:")
        print("-" * 20)
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")
            print(f"  Created: {bucket['CreationDate']}")

    except AWSAuthenticationError as e:
        print(f"Authentication failed: {e}")
    except Exception as e:
        print(f"Error listing buckets: {e}")
if __name__ == "__main__":
    list_s3_buckets()
