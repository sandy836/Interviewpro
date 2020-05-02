from collections import defaultdict
def courses_to_take(course_to_prereqs):
    #Apply topological sort
    graph = defaultdict(list)
    in_degree_count = {course:0 for course in course_to_prereqs.keys()}
    total_courses = len(course_to_prereqs)
    for course, prereqs_list in course_to_prereqs.items():
        for prereqs_course in prereqs_list:
            in_degree_count[course]  += 1
            graph[prereqs_course].append(course)
    queue, course_order, count= [], [], 0
    for key, value in in_degree_count.items():
        if value == 0:
            queue.append(key)
    while queue:
        poped_course = queue.pop(0)
        course_order.append(poped_course)
        for neighbour_node in graph[poped_course]:
            in_degree_count[neighbour_node] -= 1
            if in_degree_count[neighbour_node] == 0:
                queue.append(neighbour_node)
        count += 1
    if count == total_courses:
        return course_order
    return []
courses = {
  'CSC300': ['CSC200'], 
  'CSC200': [], 
  'CSC100': ['CSC300'],
  'CSC400': ['CSC200']
}
print(courses_to_take(courses))