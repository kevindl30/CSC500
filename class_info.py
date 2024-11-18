room_number = {
    'CSC101' : 3004,
    'CSC102' : 4501,
    'CSC103' : 6775,
    'NET110' : 1244,
    'COM241' : 1411
    }

instructors = {
    'CSC101' : 'Haynes',
    'CSC102' : 'Alvarado',
    'CSC103' : 'Rich',
    'NET110' : 'Burke',
    'COM241' : 'Lee'
    }  

meeting_time = {
    'CSC101' : '8:00 a.m.',
    'CSC102' : '9:00 a.m.',
    'CSC103' : '10:00 a.m.',
    'NET110' : '11:00 a.m.',
    'COM241' : '1:00 p.m.'
}

def class_info(course_number):
    if course_number in room_number:
        print(f"Room number: {room_number[course_number]}")
    if course_number in instructors:
        print(f"Instructor: {instructors[course_number]}")
    if course_number in meeting_time:
        print(f"Meeting time: {meeting_time[course_number]}")
    else:
        print("Invalid course number")

course_number = input("Enter a course number: ")
class_info(course_number)
