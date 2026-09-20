from database import create_connection
from interaction_repository import InteractionRepository
from follow_up_repository import FollowUpRepository

655
connection = create_connection()
interactino_repo = InteractionRepository(connection)
follow_up_repo = FollowUpRepository(connection)


print(interactino_repo.get_by_customer_id(1))
print(follow_up_repo.get_by_customer_id(1))
