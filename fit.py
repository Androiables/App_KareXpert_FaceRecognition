from datetime import datetime, timedelta
import requests
import pytz

# Define the API endpoint you want to access
api_url = 'https://fitness.googleapis.com/fitness/v1/users/me/dataset:aggregate'

# Replace 'YOUR_ACCESS_TOKEN' with your OAuth 2.0 access token
access_token = 'ya29.a0AfB_byDy8zKZeDvUBMLhnIL8dfTM0vAjg2Vczp5zryn0xPMNr2AwOpkA7_wiTRzDXNr5rT79K8bvvdoY7Qfg7c4sdEtwn46dpEUExoTFGGnlzX7D7V4KcITp-z5M427d3l1HjKAuazmot25ZLwGUvpZJOIG9Pec-GDTqaCgYKAfoSARASFQGOcNnCF5eJRYlteCLfKKAxuJ47UA0171'

# Define headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

# Define time zone
tz = pytz.timezone("Asia/Kolkata")

DATE_FORMAT = '%Y-%m-%d'
ONE_DAY_MS = 86400000
STEPS_DATASOURCE = "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps"
CALORIES_DATASOURCE = 'derived:com.google.calories.expended:com.google.android.gms:merge_calories_expended'

def get_calories(start_time, end_time):
    response = requests.post(api_url, headers=headers, json={
        "aggregateBy": [{
            "dataSourceId": CALORIES_DATASOURCE
        }],
        "bucketByTime": {"durationMillis": ONE_DAY_MS},
        "startTimeMillis": start_time,
        "endTimeMillis": end_time
    })

    calories = {}

    if response.status_code == 200:
        calories_data = response.json()
        for daily_calories_data in calories_data['bucket']:
            data_point = daily_calories_data['dataset'][0]['point']
            local_date = tz.localize(datetime.fromtimestamp(int(daily_calories_data['startTimeMillis']) / 1000))
            local_date_str = local_date.strftime(DATE_FORMAT)
            if data_point:
                count = data_point[0]['value'][0]['fpVal']
                calories[local_date_str] = {'value': count}
    return calories

def get_steps(start_time, end_time):
    response = requests.post(api_url, headers=headers, json={
        "aggregateBy": [{
            "dataSourceId": STEPS_DATASOURCE
        }],
        "bucketByTime": {"durationMillis": ONE_DAY_MS},
        "startTimeMillis": start_time,
        "endTimeMillis": end_time
    })

    steps = {}

    if response.status_code == 200:
        steps_data = response.json()
        for daily_step_data in steps_data['bucket']:
            data_point = daily_step_data['dataset'][0]['point']
            local_date = tz.localize(datetime.fromtimestamp(int(daily_step_data['startTimeMillis']) / 1000))
            local_date_str = local_date.strftime(DATE_FORMAT)
            if data_point:
                count = data_point[0]['value'][0]['intVal']
                steps[local_date_str] = {'value': count}
    return steps

if __name__ == "__main__":
    # Define the start and end times dynamically using timedelta
    end_time = datetime.now(tz)
    start_time = end_time - timedelta(days=30)  # Query data for the last 30 days

    # Convert start_time and end_time to Unix timestamps
    start_time_unix = int((start_time - datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds()) * 1000
    end_time_unix = int((end_time - datetime(1970, 1, 1, tzinfo=pytz.utc)).total_seconds()) * 1000

    # Call the functions to get steps and calories data
    steps_data = get_steps(start_time_unix, end_time_unix)
    calories_data = get_calories(start_time_unix, end_time_unix)

    # Print the results
    print("Steps data:")
    print(steps_data)
    print("Calories data:")
    print(calories_data)

