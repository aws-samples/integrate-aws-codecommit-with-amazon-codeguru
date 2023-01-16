## Automate code reviews with Amazon CodeGuru Reviewer

A common problem in software development is accidentally or unintentionally merging code with bugs, defects, or security vulnerabilities into your main branch. Finding and mitigating these faulty lines of code deployed to the production environment can cause severe outages in running applications and can cost unnecessary time and effort to fix.

[Amazon CodeGuru Reviewer](https://aws.amazon.com/codeguru/) tackles this issue using automated code reviews, which allows developers to fix the issue based on automated CodeGuru recommendations before the code moves to production.

The following diagram illustrates the architecture of this solution.
![Architecture](/image/architecture.png)

The solution has three personas:

    Repository admin – Sets up the code repository in CodeCommit
    Developer – Develops the code and uses pull requests in the main branch to move the code to production
    Code approver – Completes the code review based on the recommendations from CodeGuru and either approves the code or asks for fixes for the issue

##Prerequisites
Before we get started, we create an AWS Cloud9 development environment, which we use to check in the Python code for this solution. The sample Python code for the exercise is available in the repository. Download the .py files to a local folder.

Complete the following steps to set up the prerequisite resources:

    Set up your AWS Cloud9 environment and access the bash terminal, preferably in the us-east-1 Region.
    Create three AWS Identity and Access Management (IAM) users and its roles for the repository admin, developer, and approver by running the AWS CloudFormation template.

Configuring IAM roles and users

    *Sign in to the AWS Management Console.
    *Download ‘Persona_Users.yaml’ from repository
    *Navigate to AWS CloudFormation and click on Create Stack drop down to choose With new resouces (Standard).
    *click on Upload a template file to upload file form local.
    *Enter a Stack Name such as ‘Automate-code-reviews-codeguru-blog’.
    *Enter IAM user’s temp password.
    *Click Next to all the other default options.
    *Check mark I acknowledge that AWS CloudFormation might create IAM resources with custom names. Click Create Stack.

This template creates three IAM users for Repository admin, Code Approver, Developer that are required at different steps while following this blog.


Clean up the resources

To avoid incurring future charges, remove the resources created by this solution by

    *[Deleting the stack from the AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html)
    *[Deleting AWS Cloud9 environment](https://docs.aws.amazon.com/cloud9/latest/user-guide/delete-environment.html)
    *[Deleting AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-delete-repository.html)


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

