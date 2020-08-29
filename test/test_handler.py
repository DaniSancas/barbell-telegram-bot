import json

from handler import app


def test_app():
    request = {
        "resource": "/",
        "path": "/",
        "httpMethod": "POST",
        "headers": {
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json",
            "X-Forwarded-Port": "443",
            "X-Forwarded-Proto": "https"
        },
        "body": "{\"update_id\":123,\n\"message\":{\"message_id\":456,\"from\":{\"id\":789,\"is_bot\":false,\"first_name\":\"some\",\"last_name\":\"user\",\"username\":\"someuser\",\"language_code\":\"en\"},\"chat\":{\"id\":789,\"first_name\":\"some\",\"last_name\":\"user\",\"username\":\"someuser\",\"type\":\"private\"},\"date\":1234567890,\"text\":\"/eco some text\",\"entities\":[{\"offset\":0,\"length\":4,\"type\":\"bot_command\"}]}}",
        "isBase64Encoded": False
    }
    response = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({
            "method": "sendMessage",
            'text': "some text",
            'chat_id': 789,
            'reply_to_message_id': 456,
        })
    }

    assert app(request, None) == response
