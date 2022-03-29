from datetime import datetime
def handler(event, context):

utc = utc.replace(tzinfo=from_zone)
current_time = utc.astimezone(to_zone)
return {
    'statusCode': 200,
    'body': current_time,
}
