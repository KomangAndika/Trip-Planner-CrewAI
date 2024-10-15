import streamlit as st
from crewai import Crew
from agents import TravelAgents
from tasks import TravelTasks
from dotenv import load_dotenv

load_dotenv()


class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        # Initialize the custom agents and tasks
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define the expert agents
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Define the tasks using the agents
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.date_range,
            self.interests
        )

        # Define the crew with agents and tasks
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# Streamlit App UI
def main():
    st.title("Trip Planner Crew")
    st.write("Plan your next trip using expert agents!")

    # Input fields for trip details
    origin = st.text_input("From where will you be traveling?")
    cities = st.text_area("What are the cities you are interested in visiting?", height=100)
    date_range = st.text_input("What is the date range for your travel?")
    interests = st.text_area("What are some of your interests and hobbies?", height=100)

    if st.button("Plan My Trip"):
        if origin and cities and date_range and interests:
            # Convert the cities and interests to proper formats if needed
            cities_list = [city.strip() for city in cities.split(",")]
            interest_list = [interest.strip() for interest in interests.split(",")]

            # Initialize the TripCrew with user inputs
            trip_crew = TripCrew(origin, cities_list, date_range, interest_list)
            result = trip_crew.run()

            st.write("## Your Trip Plan:")
            st.write(result)
        else:
            st.error("Please fill in all fields to plan your trip.")


if __name__ == "__main__":
    main()
