def student_details(name,student_id,course_enrollesd,Academic_year):
    result = (
        f"Student Name: {name}\n"
        f"Student ID: {student_id}\n"
        f"Course Enrolled: {course_enrollesd}\n"
        f"Grade: {Academic_year}\n"
    )
    return result

if __name__ == "__main__":
    name="nagaraj"
    student_id="S102"
    course_enrollesd="BCA"
    Academic_year="2025"
    print(student_details(name,student_id,course_enrollesd,Academic_year))
