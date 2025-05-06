# AWS-Auth-Handler-PlayBook

Example project demonstrating the usage of [AWS-Auth-Handler](https://github.com/sirrupesh/AWS-Auth-Handler) package for AWS authentication and service interaction.

## Overview

This project showcases how to use the AWS-Auth-Handler package to:
- Authenticate with AWS using different methods
- List S3 buckets
- List Lambda functions
- Handle AWS credentials securely

## Prerequisites

- Python 3.13 or higher
- AWS credentials (access key, secret key, or profile)
- [AWS-Auth-Handler](https://github.com/sirrupesh/AWS-Auth-Handler) package installed

## Project Structure

```
AWS-Auth-Handler-PlayBook/
├── app.py           # Lambda functions listing example
├── main.py          # S3 buckets listing example
├── ai-model.py      # Amazon Bedrock with Claude example
├── .env.example     # Example environment variables
├── pyproject.toml   # Project configuration
└── README.md        # This file
```

## Setup

1. Clone this repository
2. Install dependencies using one of the following methods:

   Using pip:
   ```bash
   pip install aws-auth-handler
   ```

   Using uv (recommended):
   ```bash
   # Install uv if you haven't already
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Create virtual environment and install dependencies
   uv venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   uv pip install -e .
   ```

3. Configure AWS credentials:
   - Copy `.env.example` to `.env`
   - Add your AWS credentials to `.env`:
     ```bash
     AWS_ACCESS_KEY_ID=your_access_key_here
     AWS_SECRET_ACCESS_KEY=your_secret_key_here
     AWS_SESSION_TOKEN=your_session_token_here  # Optional
     AWS_DEFAULT_REGION=us-west-2              # Optional
     AWS_PROFILE=your_profile_name             # Optional
     ```

## Usage Examples

### List S3 Buckets

Run the S3 bucket listing example:

```bash
python main.py
```

This will:
- Initialize AWS authentication using credentials from `.env`
- Display your AWS access key ID
- List all available S3 buckets with creation dates

### List Lambda Functions

Run the Lambda functions listing example:

```bash
python app.py
```

This will:
- Initialize AWS authentication using credentials from `.env`
- Display your AWS access key ID
- List all Lambda functions in the us-west-2 region with details:
  - Function name
  - Memory allocation
  - Last modified date

### Amazon Bedrock with Claude AI

Run the AI model example using Amazon Bedrock:

```bash
python ai-model.py
```

This will:
- Initialize AWS authentication using credentials from `.env`
- Connect to Amazon Bedrock service
- Use Claude v2 model to generate responses
- Demonstrate text generation with configurable parameters:
  - Temperature
  - Max tokens
  - Top K/P sampling
  - Custom prompts

Requirements:
- AWS account with Bedrock access enabled
- Appropriate IAM permissions for Bedrock service
- Region where Bedrock and Claude model is available (default: us-east-1)

## Authentication Methods

The examples demonstrate using AWS-Auth-Handler with `.env` file authentication, but you can modify the code to use other authentication methods:

```python
# Using named AWS profile
auth = AWSAuthenticator(profile_name='development')

# Using default credentials
auth = AWSAuthenticator()

# Using environment variables directly
auth = AWSAuthenticator()  # Will automatically use AWS_* environment variables
```

## Error Handling

Both examples include error handling for:
- Authentication failures
- AWS service operation failures
- Invalid credentials

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.