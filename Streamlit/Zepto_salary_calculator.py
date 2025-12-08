import streamlit as st
# stuploaded_file = st.file_uploader("csv uploaded")

col1 , col2 , col3 = st.columns(3)

average_no_of_raids_in_weekday = col1.number_input("Enter your number of raids per day in weekday:")

price_per_raid = col1.number_input("Enter the price per raid")

surge_amount = col2.number_input("Enter the surge price ")

# no_of_Raids_for_surge = col2.number_input("Enter the number of raids needed for surge ")


average_no_of_raids_in_weekend = col3.number_input("Enter your number of raids per day in weekdends:")

raids_needed_for_surge = st.number_input("Enter the number of raids needed for surge")

Days_month_dictionary =  {
    "January": 31,
    "February": 28,   
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}


required_month  = st.selectbox("Enter the month you want to calculate revenue" ,
                                ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
)

no_of_weekends_per_month =st.number_input("Enter the number of weekneds per month")


raid_count = 0  
surge_count = 1
total_amount_earned = 0                         
for i in range(Days_month_dictionary[required_month]):
    if (i+1) % 7 ==0:
        amount_earned = average_no_of_raids_in_weekend * price_per_raid
        surge_count +=average_no_of_raids_in_weekend
        no_of_surge = surge_count % raids_needed_for_surge
        amount_earned += surge_amount * no_of_surge
        raid_count +=average_no_of_raids_in_weekend
        total_amount_earned +=amount_earned
        surge_count = surge_count / raids_needed_for_surge
        st.write(f"Amount earned in day {i+1} is {amount_earned}")
    else:

        amount_earned = average_no_of_raids_in_weekday * price_per_raid
        surge_count +=average_no_of_raids_in_weekday
        no_of_surge = surge_count % raids_needed_for_surge
        amount_earned += surge_amount * no_of_surge
        raid_count +=average_no_of_raids_in_weekday
        total_amount_earned +=amount_earned
        surge_count = surge_count / raids_needed_for_surge
        st.write(f"Amount earned in day {i+1} is {amount_earned}")
    
st.success(f"Total amount earned in {required_month} is {total_amount_earned} and earned via {raid_count} raids")