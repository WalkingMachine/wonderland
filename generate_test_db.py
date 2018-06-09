from api.models import Entity, People

# Create Rooms
hallway = Entity.objects.create(entityClass="lobby", entityContainer=None, entityIsWaypoint=True, entityWaypointX=1.23, entityWaypointY=-5.62, entityWaypointYaw=0.15)                  # 1
kitchen = Entity.objects.create(entityClass="kitchen", entityContainer=None, entityIsWaypoint=True, entityWaypointX=4.795, entityWaypointY=-0.495, entityWaypointYaw=-2.250)            # 2
corridor = Entity.objects.create(entityClass="corridor", entityContainer=None, entityIsWaypoint=True, entityWaypointX=1.115, entityWaypointY=-1.09, entityWaypointYaw=-1.57)            # 3
bedroom = Entity.objects.create(entityClass="bedroom", entityContainer=None, entityIsWaypoint=True, entityWaypointX=3.99, entityWaypointY=-5.50, entityWaypointYaw=0)                   # 4
bathroom = Entity.objects.create(entityClass="bathroom", entityContainer=None, entityIsWaypoint=True, entityWaypointX=1.115, entityWaypointY=-1.09, entityWaypointYaw=-1.57)            # 5
lobby = Entity.objects.create(entityClass="lobby", entityContainer=None, entityIsWaypoint=True, entityWaypointX=3.47, entityWaypointY=2.63, entityWaypointYaw=-1.57)                    # 6

# Create main containers
table = Entity.objects.create(entityClass="table", entityContainer=hallway, entityIsWaypoint=True, entityWaypointX=4.27, entityWaypointY=2.63, entityWaypointYaw=-1.57)                 # 7
desk = Entity.objects.create(entityClass="desk", entityContainer=hallway, entityIsWaypoint=True, entityWaypointX=3.23, entityWaypointY=-0.02, entityWaypointYaw=-1.57)                  # 8
counter = Entity.objects.create(entityClass="counter", entityContainer=bathroom)                                                                                                        # 9
cupboard = Entity.objects.create(entityClass="cupboard", entityContainer=lobby)                                                                                                         # 10



# Create People

People.objects.create(peopleRecognitionId=1, peopleAge=15, peopleColor="blue", peoplePose="lying", peoplePoseAccuracy=12.3,
                      peopleGender="boy", peopleGenderAccuracy=100.0, peopleIsOperator=False, peopleName="Jeff")
People.objects.create(peopleRecognitionId=10, peopleAge=25, peopleColor="red", peoplePose="sitting", peoplePoseAccuracy=45.6,
                      peopleGender="girl", peopleGenderAccuracy=100.0, peopleIsOperator=True, peopleName="Annie-Anh")
People.objects.create(peopleRecognitionId=45, peopleAge=43, peopleColor="green", peoplePose="pointing left", peoplePoseAccuracy=78.9,
                      peopleGender="boy", peopleGenderAccuracy=100.0, peopleIsOperator=False, peopleName="Phil")
People.objects.create(peopleRecognitionId=20, peopleAge=18, peopleColor="green", peoplePose="standing", peoplePoseAccuracy=78.9,
                      peopleGender="girl", peopleGenderAccuracy=100.0, peopleIsOperator=True, peopleName="Vero")

