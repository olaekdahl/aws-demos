import boto3

def list_ec2_instances():
    # Create an EC2 resource service client
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    
    print("Listing EC2 instances:")
    for instance in ec2.instances.all():
        print(f"ID: {instance.id}, State: {instance.state['Name']}, Type: {instance.instance_type}")

if __name__ == '__main__':
    list_ec2_instances()