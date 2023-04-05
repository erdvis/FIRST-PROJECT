// Replace ACCESS_TOKEN with your Strava access token
const ACCESS_TOKEN = "c3a58af0fd13e83ab1166609561afd27be33ace1";

// Construct the API endpoint URL
const API_ENDPOINT = "https://www.strava.com/api/v3/athlete/activities";

// Set up the API request headers
const headers = {
  Authorization: `Bearer ${ACCESS_TOKEN}`,
};

// Make the API request using fetch()
fetch(API_ENDPOINT, { headers })
  .then((response) => response.json())
  .then((activities) => {
    // Loop through the retrieved activities and add them to the list
    activities.forEach((activity) => {
      const activityElement = document.createElement("li");
      activityElement.classList.add("activity");
      activityElement.innerHTML = `
        <h2>${activity.name}</h2>
        <p>${activity.distance / 1000} km</p>
      `;
      document.getElementById("activities").appendChild(activityElement);
    });
  })
  .catch((error) => {
    // Handle any errors that occur during the API request
    console.error(error);
  });
