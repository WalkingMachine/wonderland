from api.models import Entity, People

# Create Rooms
lobby = Entity.objects.create(entityClass="lobby", entityContainer=None, entityIsWaypoint=True, entityWaypointX=1.23, entityWaypointY=-5.62, entityWaypointYaw=0.15)                    # 1 ----
corridor = Entity.objects.create(entityClass="corridor", entityContainer=None, entityIsWaypoint=True, entityWaypointX=1.115, entityWaypointY=-1.09, entityWaypointYaw=-1.57)            # 2 ----
bedroom = Entity.objects.create(entityClass="bedroom", entityContainer=None, entityIsWaypoint=True, entityWaypointX=3.99, entityWaypointY=-5.50, entityWaypointYaw=0)                   # 3 ----
livingroom = Entity.objects.create(entityClass="living room", entityContainer=None, entityIsWaypoint=True, entityWaypointX=4.795, entityWaypointY=-0.495, entityWaypointYaw=-2.250)     # 4 ----
hall = Entity.objects.create(entityClass="hall", entityContainer=None, entityIsWaypoint=True, entityWaypointX=3.47, entityWaypointY=2.63, entityWaypointYaw=-1.57)                      # 5 ----



# Create People
People.objects.create(peopleRecognitionId=1, peopleColor="blue", peoplePose="seated", peoplePoseAccuracy=12.3, peopleGender="male", peopleGenderAccuracy=100.0, peopleIsOperator=False, peopleName="Jeff")
People.objects.create(peopleRecognitionId=10, peopleColor="red", peoplePose="standing", peoplePoseAccuracy=45.6, peopleGender="female", peopleGenderAccuracy=100.0, peopleIsOperator=True, peopleName="Julie")
People.objects.create(peopleRecognitionId=45, peopleColor="green", peoplePose="sleeping", peoplePoseAccuracy=78.9, peopleGender="male", peopleGenderAccuracy=100.0, peopleIsOperator=False, peopleName="Phil")
People.objects.create(peopleRecognitionId=20, peopleColor="green", peoplePose="sleeping", peoplePoseAccuracy=78.9, peopleGender="female", peopleGenderAccuracy=100.0, peopleIsOperator=True, peopleName="Vero")
