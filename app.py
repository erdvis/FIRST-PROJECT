from flask import Flask, jsonify
import stravalib

app = Flask(__name__)

# Replace with your own Strava access token
access_token = 'c3a58af0fd13e83ab1166609561afd27be33ace1'

@app.route('/strava/activities')
def get_activities():
    client = stravalib.Client(access_token=access_token)
    activities = client.get_activities()
    activities_dict = [activity.to_dict() for activity in activities]
    return jsonify(activities_dict)