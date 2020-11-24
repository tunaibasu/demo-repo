from pymongo import MongoClient
client=MongoClient('localhost',27017)
print(client)

db=client.test_db
courses=db.courses
#print(courses)
# course={
#     'author':'Subhajit',
#     'course':'Python with Mongo',
#     'purpose':'practice'
#}
arr_courses=[
    {
    'author':'Subhajit',
    'course':'Python with Mongo',
    'purpose':'practice'
},
{
    'author':'Somenath',
    'course':'Project Management',
    'purpose':'PMP'
},
{
    'author':'Abhishek',
    'course':'How to Sale',
    'purpose':'selling'
},
{
    'author':'Kajal',
    'course':'Full Stack Development',
    'purpose':'practice'
}
]
results=courses.insert_many(arr_courses)
for object_id in results.inserted_ids:
    print("Course added",object_id)
#print(result)