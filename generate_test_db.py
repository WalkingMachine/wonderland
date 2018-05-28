from api.models import Entity, People

# Create Entity
e1 = Entity.objects.create(entityClass="dining room", entityContainer=None,
                           entityIsWaypoint=True, entityWaypointX=0, entityWaypointY=5)  # 1
e2 = Entity.objects.create(entityClass="bedroom", entityContainer=None, entityIsWaypoint=True,
                           entityWaypointX=12, entityWaypointY=15, entityWaypointYaw=2.3)  # 2
e3 = Entity.objects.create(entityClass="table", entityContainer=e1)  # 3
Entity.objects.create(entityClass="chair", entityContainer=e1, )  # 4
e5 = Entity.objects.create(entityClass="sideboard", entityContainer=e1)  # 5
Entity.objects.create(entityClass="cut", entityContainer=e3, )  # 6
Entity.objects.create(entityClass="apple", entityContainer=e3, entityCategory="fruit")  # 7
e8 = Entity.objects.create(entityClass="tray", entityContainer=e3, )  # 8
Entity.objects.create(entityClass="apple", entityContainer=e8, entityCategory="fruit")  # 9
Entity.objects.create(entityClass="glass", entityContainer=e5)  # 10
Entity.objects.create(entityClass="glass", entityContainer=e3)  # 11
Entity.objects.create(entityClass="bed", entityContainer=e2)  # 12
e13 = Entity.objects.create(entityClass="night table", entityContainer=e2)  # 13
Entity.objects.create(entityClass="clock", entityContainer=e13)  # 14
Entity.objects.create(entityClass="light", entityContainer=e13)  # 15
e16 = Entity.objects.create(entityClass="table", entityContainer=e2)  # 16
Entity.objects.create(entityClass="cut", entityContainer=e16)  # 17
Entity.objects.create(entityClass="pen", entityContainer=e16)  # 18
Entity.objects.create(entityClass="desk", entityContainer=e2,
                      entityIsWaypoint=True, entityWaypointX=-10, entityWaypointY=-15)  # 19
Entity.objects.create(entityClass="chair", entityContainer=e2)  # 20

# Create People
People.objects.create(peopleRecognitionId=1, peopleAge=15, peopleColor="blue", peoplePose="lying", peoplePoseAccuracy=12.3,
                      peopleGender="boy", peopleGenderAccuracy=100.0, peopleIsOperator=False, peopleName="Jeff")
People.objects.create(peopleRecognitionId=10, peopleAge=25, peopleColor="red", peoplePose="sitting", peoplePoseAccuracy=45.6,
                      peopleGender="girl", peopleGenderAccuracy=100.0, peopleIsOperator=True, peopleName="Julie")
People.objects.create(peopleRecognitionId=45, peopleAge=43, peopleColor="green", peoplePose="pointing left", peoplePoseAccuracy=78.9,
                      peopleGender="boy", peopleGenderAccuracy=100.0, peopleIsOperator=False, peopleName="Phil")
People.objects.create(peopleRecognitionId=20, peopleAge=18, peopleColor="green", peoplePose="standing", peoplePoseAccuracy=78.9,
                      peopleGender="girl", peopleGenderAccuracy=100.0, peopleIsOperator=True, peopleName="Vero")
