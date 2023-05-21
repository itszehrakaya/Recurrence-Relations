def maximum_attendees(start_times, end_times, attendees):
    # Sort talks by end time and relabel
    talks = sorted(zip(end_times, start_times, attendees))
    end_times, start_times, attendees = zip(*talks)
    n = len(start_times)
   
    

        
  
    
  
start_times = [1, 2, 4, 5]
end_times = [5, 3, 8, 7]
attendees = [2, 4, 6, 8]

result = maximum_attendees(start_times, end_times, attendees)
print("Maximum number of attendees:", result)
