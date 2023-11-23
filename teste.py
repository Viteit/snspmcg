import boto3

def main():

    # Substitua pelas suas credenciais da AWS
    aws_access_key_id = 'AKIA2IFYBB2M4ZONXDVO'
    aws_secret_access_key = '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'

    # Inicialize o cliente SNS com suas credenciais
    sns = boto3.client(
        'sns',
        region_name='us-east-1',  # substitua pela sua região
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Substitua pelo ARN do seu tópico e sua mensagem
    topic_arn = 'arn:aws:sns:us-east-1:704760581785:sns_send_message_neighborhood_prod'
    message = 'Testando'

    sns.publish(
        TopicArn=topic_arn,
        Message=message  # substitua pela sua mensagem
    )

if __name__ == "__main__":
    main()
