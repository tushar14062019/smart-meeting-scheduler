# **Case Study: Smart Meeting Scheduler**

## **Problem Statement**  
A corporate team wants an automated system to schedule meetings efficiently based on availability. The system should:  

1. Maintain a **calendar** for each team member.  
2. Define **working hours** (e.g., 9 AM to 5 PM).  
3. Allow users to schedule a **meeting on a future date**.  
4. Prevent overlapping meetings.  
5. Show **available slots** for scheduling new meetings.  
6. Allow users to view their **upcoming meetings**.  
7. Handle **public holidays and weekends** to prevent scheduling on non-working days.  

---

## **Implementation Details**
- Use Python’s `calendar` module to check weekends and holidays.  
- Use the `datetime` module for managing meeting times.  
- Store meetings in a dictionary where each user has a list of booked slots.  
- Provide a CLI-based or function-driven interaction.

---

## **Tasks to Implement**
### **1. Initialize the Scheduler**  
- Define working hours.  
- Store public holidays.  

### **2. Schedule a Meeting**  
- Check if the date is a **working day** (not a weekend or holiday).  
- Ensure the time slot is available.  
- Add the meeting to the schedule.  

### **3. Check Available Time Slots**  
- Show free slots for a given date.  

### **4. View Scheduled Meetings**  
- Display upcoming meetings for a user.  

### **5. Prevent Overlapping Meetings**  
- Ensure new meeting requests do not overlap existing ones.  

---

## **Example Usage**

### **User Input:**
- Schedule a meeting for **March 18, 2025**, from **10 AM to 11 AM**.
- Check available slots for **March 18, 2025**.

### **System Response:**
- **Meeting scheduled successfully.**
- **Available slots:**  
  - 9:00 AM – 10:00 AM  
  - 11:00 AM – 12:00 PM  
  - 1:00 PM – 5:00 PM  

---

