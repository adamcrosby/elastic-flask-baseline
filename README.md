elastic-flask-baseline
======================

A baseline Flask application suitable for use on Amazon Elastic Beanstalk.

The code here is kept as minimal as possible, while still demonstrating the critical points/differences that running on Elastic Beanstalk requires.

Things you will need:

- Flask: http://flask.pocoo.org
- AWS 'eb' tool: http://aws.amazon.com/developertools/351/
- Your AWS API keys: https://aws-portal.amazon.com/gp/aws/securityCredentials
- Git: http://git-scm.com

Quickstart
-----------

1. Install the 'eb' tool.
2. Git clone this repository.
3. Run 'eb init' in the repository, and answer the questions, providing your API Key, etc.
4. Run 'eb start' in the repository, and wait for it to complete.
5. Run 'git aws.push' in the repository.
6. Run 'eb status' in the repository, and wait for it to return 'Green' status.
7. Browse to the URL reported by 'eb status', and be amazed at your autoscaling, crazy, cloud-based application!

For More Detailed Instructions
------------------------------
For more detailed information, and a step by step walkthrough of each command, etc., check out my [blog post](http://blog.uptill3.com/2012/08/31/flask-elastic-beanstalk-baseline.html)!.